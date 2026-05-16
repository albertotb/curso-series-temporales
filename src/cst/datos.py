"""Carga y descarga de datasets para la Sesión 1.

Cinco fuentes (ver `data/README.md` para detalles):

1. **CHD piezometría** (`PZ0267014`) — Excel local en `data/raw/`. Manual.
2. **CEDEX Anuario de Aforos** — CSV público (HTTP) con datos diarios de caudal
   y catálogo de estaciones del Guadalquivir (Pinos-Genil = `indroea` 5020,
   hasta 2020-12-31). Base reproducible para series largas.
3. **SAIH Guadalquivir** — Excel exportado a mano desde
   https://www.chguadalquivir.es/saih/DatosHistoricos.aspx (WebForm ASP.NET sin
   API pública). Contiene caudal `A20_211_X` y lluvia `A20_202` horarios desde
   2018, incluida la crecida de feb 2026. Si el Excel existe, las funciones lo
   prefieren al ROEA y lo resamplean a diario.
4. **Open-Meteo · ERA5 reanalysis** — HTTP gratis sin API key. Precipitación
   diaria por lat/lon (resolución ~25 km). Útil como sustituto cuando no hay
   estación cercana (p.ej. la piezometría del Duero) y para comparar
   modelo-vs-estación.
5. **AEMET OpenData** — HTTP con API key. Precipitación diaria oficial por
   estación (5530E Granada Aeropuerto, etc.). Serie larga (1971-presente),
   permite trends multidecadales. Requiere `AEMET_API_KEY` en `.env` o entorno.

Estructura de archivos esperada en `data/raw/` (sólo la piezometría es
obligatoria; el resto se descarga o se omite):

```
data/raw/
├── piezometria_chd_2024-12.xlsx         # manual (CHD · MITECO)
├── anuario_aforos/                       # auto: descargar_anuario_csv
│   ├── GUADALQUIVIR_afliq.csv            #   caudal diario
│   ├── GUADALQUIVIR_estaf.csv            #   catálogo de estaciones
│   └── GUADALQUIVIR_evap.csv             #   precip mensual evaporimétricas
├── saih_chg/
│   └── HistSAIH.xlsx                     # manual (SAIH-CHG) — caudal+lluvia
├── openmeteo/                            # auto: descargar_lluvia_openmeteo
│   └── era5_<lat>_<lon>_<rango>.csv
└── aemet/                                # auto: cargar_lluvia_aemet
    ├── <estacion>_<rango>.parquet
    └── <estacion>/chunk_<fecha>.json
```
"""

from __future__ import annotations

import os
import time
from datetime import datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.ssl_ import create_urllib3_context

RUTA_RAIZ = Path(__file__).resolve().parents[2]
RUTA_RAW = RUTA_RAIZ / "data" / "raw"
RUTA_ANUARIO = RUTA_RAW / "anuario_aforos"
RUTA_PIEZO_XLSX = RUTA_RAW / "piezometria_chd_2024-12.xlsx"

URL_ANUARIO_BASE = (
    "https://ceh-flumen64.cedex.es/anuarioaforos/anuario-2020-2021/{cuenca}/{archivo}"
)
URL_OPENMETEO = "https://archive-api.open-meteo.com/v1/archive"

# Coordenadas de referencia (lat, lon) para los dos puntos del curso.
COORDS_PINOS_GENIL = (37.1626, -3.4929)        # ROEA 5020, Granada
COORDS_PZ0267014 = (41.6601, -4.6295)          # CHD, Renedo de Esgueva (Valladolid)

# El servidor del CEDEX cierra la conexión si no llega un User-Agent realista.
HEADERS_HTTP = {
    "User-Agent": (
        "Mozilla/5.0 (curso-series-temporales/komorebi-ai) "
        "python-requests/educational-use"
    )
}


class _LegacyCipherAdapter(HTTPAdapter):
    """Transport adapter que habilita cifrados RSA "legacy" (no ECDHE).

    El servidor del CEDEX (`ceh.cedex.es`) negocia `AES256-GCM-SHA384` puro,
    que OpenSSL 3.x excluye de la lista por defecto. Bajando `SECLEVEL` a 1
    el handshake TLS 1.2 vuelve a funcionar (sigue siendo HTTPS válido).
    """

    def init_poolmanager(self, *args, **kwargs):
        ctx = create_urllib3_context()
        ctx.set_ciphers("DEFAULT@SECLEVEL=1")
        kwargs["ssl_context"] = ctx
        return super().init_poolmanager(*args, **kwargs)


def _sesion_cedex() -> requests.Session:
    s = requests.Session()
    s.headers.update(HEADERS_HTTP)
    adapter = _LegacyCipherAdapter()
    s.mount("https://", adapter)
    return s

# -----------------------------------------------------------------------------
# 1. CHD — Piezometría
# -----------------------------------------------------------------------------


def cargar_piezometria(codigo: str = "PZ0267014") -> pd.Series:
    """Cota piezométrica del pozo `codigo` (m s.n.m.) indexada por fecha."""
    df = pd.read_excel(RUTA_PIEZO_XLSX, sheet_name="DATOS PIEZOMETRICOS")
    df.columns = [c.strip().replace("\n", " ").replace("  ", " ") for c in df.columns]
    col_cod = next(c for c in df.columns if c.startswith("CODIGO"))
    col_cota = next(c for c in df.columns if c.startswith("COTA PIEZOM"))

    sub = df[df[col_cod].astype(str).str.strip() == codigo].copy()
    sub["FECHA"] = pd.to_datetime(sub["FECHA"], errors="coerce")
    sub = sub.dropna(subset=["FECHA"]).sort_values("FECHA")

    serie = pd.Series(
        sub[col_cota].astype(float).values,
        index=pd.DatetimeIndex(sub["FECHA"].values, name="fecha"),
        name=f"cota_{codigo}",
    )
    return serie.groupby(serie.index).mean()


# -----------------------------------------------------------------------------
# 2. CEDEX — Anuario de Aforos (datos históricos)
# -----------------------------------------------------------------------------


def descargar_anuario_csv(
    archivo: str,
    cuenca: str = "GUADALQUIVIR",
    forzar: bool = False,
) -> Path:
    """Descarga un CSV del Anuario de Aforos a `data/raw/anuario_aforos/`.

    Archivos típicos: `afliq.csv` (caudal diario), `estaf.csv` (catálogo de
    estaciones), `evap.csv` (datos evaporación/precipitación mensual),
    `mensual_a.csv` (caudal mensual). Lista completa: ver índice de
    https://ceh.cedex.es/anuarioaforos/demarcaciones.asp.
    """
    RUTA_ANUARIO.mkdir(parents=True, exist_ok=True)
    destino = RUTA_ANUARIO / f"{cuenca}_{archivo}"
    if destino.exists() and not forzar:
        return destino

    url = URL_ANUARIO_BASE.format(cuenca=cuenca, archivo=archivo)
    with _sesion_cedex() as s:
        resp = s.get(url, timeout=120)
    resp.raise_for_status()
    destino.write_bytes(resp.content)
    return destino


def cargar_anuario_caudal(indroea: int) -> pd.Series:
    """Caudal diario (m³/s) de la estación `indroea` desde el Anuario de Aforos.

    Descarga `afliq.csv` si no está en local. Filtra por `indroea` y devuelve
    una `Series` con índice diario regular (rellena las fechas ausentes con
    NaN para reflejar gaps reales).
    """
    ruta = descargar_anuario_csv("afliq.csv")
    df = pd.read_csv(ruta, sep=";", decimal=".", encoding="latin-1")
    df.columns = [c.strip().lower() for c in df.columns]

    sub = df[df["indroea"] == int(indroea)].copy()
    if sub.empty:
        raise ValueError(f"No hay registros para indroea={indroea} en {ruta.name}")

    sub["fecha"] = pd.to_datetime(sub["fecha"], format="%d/%m/%Y", errors="coerce")
    sub = sub.dropna(subset=["fecha"]).sort_values("fecha")

    serie = pd.Series(
        pd.to_numeric(sub["caudal"], errors="coerce").values,
        index=pd.DatetimeIndex(sub["fecha"].values, name="fecha"),
        name=f"caudal_ROEA_{indroea}",
    )
    serie = serie.groupby(serie.index).mean()

    idx_completo = pd.date_range(serie.index.min(), serie.index.max(), freq="D", name="fecha")
    return serie.reindex(idx_completo)


def cargar_anuario_precip_mensual(ref_evap: int) -> pd.Series:
    """Precipitación mensual (mm) en la estación pluvio-evaporativa `ref_evap`.

    Fuente: `evap.csv` del Anuario. Columna `prectotmes` (mm/mes).
    Útil como input de CCF a escala mensual cuando no se tiene SAIH/AEMET.
    """
    ruta = descargar_anuario_csv("evap.csv")
    df = pd.read_csv(ruta, sep=";", decimal=".", encoding="latin-1")
    df.columns = [c.strip().lower() for c in df.columns]

    sub = df[df["ref_evap"] == int(ref_evap)].copy()
    if sub.empty:
        raise ValueError(f"No hay registros para ref_evap={ref_evap} en {ruta.name}")

    sub["fecha"] = pd.to_datetime(sub["anomes"].astype(str), format="%Y%m", errors="coerce")
    sub = sub.dropna(subset=["fecha"]).sort_values("fecha")

    serie = pd.Series(
        pd.to_numeric(sub["prectotmes"], errors="coerce").values,
        index=pd.DatetimeIndex(sub["fecha"].values, name="fecha"),
        name=f"precip_mensual_evap_{ref_evap}",
    )
    return serie.groupby(serie.index).mean()


def cargar_anuario_estaciones() -> pd.DataFrame:
    """Catálogo de estaciones de aforo del Guadalquivir (`estaf.csv`)."""
    ruta = descargar_anuario_csv("estaf.csv")
    df = pd.read_csv(ruta, sep=";", decimal=".", encoding="latin-1")
    df.columns = [c.strip().lower() for c in df.columns]
    for c in df.select_dtypes(include="object").columns:
        df[c] = df[c].str.strip()
    return df


# -----------------------------------------------------------------------------
# 3. SAIH Guadalquivir — descarga manual (opcional)
# -----------------------------------------------------------------------------

RUTA_SAIH_XLSX = RUTA_RAW / "saih_chg" / "HistSAIH.xlsx"

# Columnas tal y como las exporta el SAIH (cluster A20 — Genil-Tocón).
_SAIH_COL_CAUDAL = "A20_211_X"   # caudal m³/s, media horaria
_SAIH_COL_LLUVIA = "A20_202"     # precipitación l/m² (≈ mm), acumulado horario


def _cargar_saih_excel_horario() -> pd.DataFrame:
    """Lee la hoja `Datos` del export Excel del SAIH (formato horario).

    La exportación oficial del SAIH (https://www.chguadalquivir.es/saih/) tiene
    dos hojas: `Info` con metadatos y `Datos` con la tabla. Tras el último dato
    horario hay una fila vacía y un bloque de "Estadísticas" (Mínimo, Máximo,
    Media, Total, Número) que descartamos parseando FECHA como datetime y
    eliminando filas con NaT.

    Usamos el engine `calamine` porque `openpyxl` 3.1.5 falla al leer este
    fichero (atributo `defaultColWidthPt` que la librería no reconoce).
    """
    df = pd.read_excel(RUTA_SAIH_XLSX, sheet_name="Datos", engine="calamine")
    df["FECHA"] = pd.to_datetime(df["FECHA"], errors="coerce")
    df = df.dropna(subset=["FECHA"]).set_index("FECHA").sort_index()
    df.index.name = "fecha"
    return df


def cargar_caudal_genil(indroea_fallback: int = 5020) -> pd.Series:
    """Caudal diario del Genil en `A20_GENIL_TOCON`.

    Prefiere el Excel manual del SAIH si está disponible (resamplea las medias
    horarias a media diaria); en su defecto, devuelve la serie ROEA indicada
    (Pinos-Genil 5020 por defecto, datos hasta 2020-12-31).
    """
    if RUTA_SAIH_XLSX.exists():
        horario = _cargar_saih_excel_horario()[_SAIH_COL_CAUDAL]
        diario = horario.resample("D").mean()
        diario.name = "caudal_A20_GENIL_TOCON"
        return diario
    return cargar_anuario_caudal(indroea_fallback)


def cargar_lluvia_genil(ref_evap_fallback: int = 5001) -> pd.Series:
    """Lluvia diaria (mm) del pluviómetro SAIH `A20_202` (cluster Genil-Tocón).

    Lee el Excel del SAIH y suma los acumulados horarios a total diario. Si el
    Excel no está disponible, devuelve como sustituto la precipitación mensual
    en Iznájar (ref_evap=5001) del Anuario de Aforos.
    """
    if RUTA_SAIH_XLSX.exists():
        horario = _cargar_saih_excel_horario()[_SAIH_COL_LLUVIA]
        diario = horario.resample("D").sum(min_count=1)
        diario.name = "lluvia_A20_202"
        return diario
    return cargar_anuario_precip_mensual(ref_evap_fallback)


# -----------------------------------------------------------------------------
# 4. Open-Meteo · ERA5 reanalysis (lluvia diaria por lat/lon)
# -----------------------------------------------------------------------------

RUTA_OPENMETEO = RUTA_RAW / "openmeteo"


def descargar_lluvia_openmeteo(
    lat: float,
    lon: float,
    fecha_inicio: str = "1970-01-01",
    fecha_fin: str = "2024-12-31",
    nombre_cache: str | None = None,
    forzar: bool = False,
) -> pd.Series:
    """Precipitación diaria (mm) en (lat, lon) desde ERA5 vía Open-Meteo.

    - Gratis, sin API key. Resolución ERA5 ≈ 25 km, daily precipitation_sum.
    - Cachea en `data/raw/openmeteo/<nombre_cache>.csv` para no rebajar la API.

    Parámetros
    ----------
    lat, lon : coordenadas WGS84.
    fecha_inicio, fecha_fin : 'YYYY-MM-DD'.
    nombre_cache : nombre del fichero local. Si `None`, se genera de las coords.
    """
    RUTA_OPENMETEO.mkdir(parents=True, exist_ok=True)
    if nombre_cache is None:
        nombre_cache = f"era5_{lat:.3f}_{lon:.3f}_{fecha_inicio}_{fecha_fin}"
    destino = RUTA_OPENMETEO / f"{nombre_cache}.csv"

    if destino.exists() and not forzar:
        df = pd.read_csv(destino, parse_dates=["fecha"])
    else:
        params = {
            "latitude": lat, "longitude": lon,
            "start_date": fecha_inicio, "end_date": fecha_fin,
            "daily": "precipitation_sum",
            "timezone": "Europe/Madrid",
        }
        r = requests.get(URL_OPENMETEO, params=params, timeout=120)
        r.raise_for_status()
        data = r.json()["daily"]
        df = pd.DataFrame({"fecha": pd.to_datetime(data["time"]),
                           "precip_mm": data["precipitation_sum"]})
        df.to_csv(destino, index=False)

    return pd.Series(
        pd.to_numeric(df["precip_mm"], errors="coerce").values,
        index=pd.DatetimeIndex(df["fecha"].values, name="fecha"),
        name=f"lluvia_era5_{lat:.3f}_{lon:.3f}",
    )


def cargar_lluvia_genil_diaria(**kwargs) -> pd.Series:
    """Lluvia diaria (ERA5) sobre Pinos-Genil (Granada)."""
    lat, lon = COORDS_PINOS_GENIL
    return descargar_lluvia_openmeteo(lat, lon, nombre_cache="pinos_genil", **kwargs)


def cargar_lluvia_duero_diaria(**kwargs) -> pd.Series:
    """Lluvia diaria (ERA5) sobre PZ0267014 (Valladolid)."""
    lat, lon = COORDS_PZ0267014
    return descargar_lluvia_openmeteo(lat, lon, nombre_cache="pz0267014", **kwargs)


# -----------------------------------------------------------------------------
# 5. AEMET OpenData (precipitación diaria por estación)
# -----------------------------------------------------------------------------

URL_AEMET_DAILY = (
    "https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos"
    "/fechaini/{ini}/fechafin/{fin}/estacion/{idema}"
)
RUTA_AEMET = RUTA_RAW / "aemet"


def _leer_api_key_aemet(api_key: str | None) -> str:
    """Resuelve la API key: argumento → env var → .env del repo."""
    if api_key:
        return api_key
    if v := os.environ.get("AEMET_API_KEY"):
        return v
    env_path = RUTA_RAIZ / ".env"
    if env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            if line.startswith("AEMET_API_KEY="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise RuntimeError(
        "Falta API key de AEMET. Pásala como `api_key=`, define la variable "
        "de entorno `AEMET_API_KEY`, o añádela a `.env` en la raíz del repo."
    )


def _parse_prec_aemet(v) -> float:
    """Parsea valor de precipitación AEMET → float en mm.

    - "8,4"   → 8.4   (decimal coma)
    - "Ip"    → 0.05  (lluvia inappreciable, < 0.1 mm)
    - "Acum"  → NaN   (acumulada en otro día)
    - None / "" → NaN
    """
    if v is None or v == "":
        return float("nan")
    if v == "Ip":
        return 0.05
    if v == "Acum":
        return float("nan")
    try:
        return float(str(v).replace(",", "."))
    except ValueError:
        return float("nan")


def _aemet_get(url: str, api_key: str, max_retries: int = 8) -> list:
    """Realiza el flujo en dos pasos (meta → datos) con reintentos.

    Reintenta con backoff exponencial en errores transitorios:
    429 (rate limit), 5xx, y errores de red (`ConnectionError`, `Timeout`).
    Devuelve `[]` si AEMET responde 404 (sin datos para ese rango).
    """
    transitorias = (
        requests.exceptions.ConnectionError,
        requests.exceptions.Timeout,
        requests.exceptions.ChunkedEncodingError,
    )
    for attempt in range(max_retries):
        backoff = min(60, 2 ** attempt)  # 1, 2, 4, 8, 16, 32, 60, 60
        try:
            r = requests.get(url, params={"api_key": api_key}, timeout=60)
        except transitorias:
            time.sleep(backoff)
            continue
        if r.status_code in (429, 500, 502, 503, 504):
            time.sleep(backoff)
            continue
        if r.status_code == 404:
            return []  # estación sin datos para ese rango
        r.raise_for_status()
        meta = r.json()
        estado = meta.get("estado")
        if estado in (429, 500, 502, 503, 504):
            time.sleep(backoff)
            continue
        if estado == 404:
            return []
        if estado != 200:
            raise RuntimeError(f"AEMET error: {meta}")
        time.sleep(0.5)
        try:
            r2 = requests.get(meta["datos"], timeout=120)
        except transitorias:
            time.sleep(backoff)
            continue
        if r2.status_code in (429, 500, 502, 503, 504):
            time.sleep(backoff)
            continue
        r2.raise_for_status()
        return r2.json()
    raise RuntimeError(f"Demasiados reintentos para {url}")


def _chunks_6_meses(fecha_inicio: str, fecha_fin: str):
    """Yield (fechaIniStr, fechaFinStr) en chunks de 90 días.

    AEMET admite hasta 6 meses por petición, pero chunks más pequeños son
    más fiables (menos timeouts en series largas).
    """
    ini = datetime.fromisoformat(fecha_inicio)
    fin = datetime.fromisoformat(fecha_fin)
    paso = timedelta(days=90)
    cursor = ini
    while cursor <= fin:
        chunk_fin = min(cursor + paso - timedelta(days=1), fin)
        yield (
            cursor.strftime("%Y-%m-%dT00:00:00UTC"),
            chunk_fin.strftime("%Y-%m-%dT23:59:59UTC"),
        )
        cursor = chunk_fin + timedelta(days=1)


def cargar_lluvia_aemet(
    estacion: str = "5103E",
    fecha_inicio: str = "1995-01-01",
    fecha_fin: str = "2020-12-31",
    api_key: str | None = None,
    forzar: bool = False,
) -> pd.Series:
    """Precipitación diaria (mm) desde AEMET OpenData para `estacion`.

    Devuelve una `pd.Series` con índice diario regular (NaN en huecos).

    Cachea de dos formas:
    - Resultado final: `data/raw/aemet/<estacion>_<ini>_<fin>.parquet`.
    - **Por chunk** (resumible): `data/raw/aemet/<estacion>/chunk_<ini>.json`,
      uno por trozo de 90 días. Si el proceso falla por rate-limit, basta con
      volver a llamar a la función para que continúe donde lo dejó.

    Estaciones útiles para el curso (cuenca del Genil / Granada):

    - **5530E**: GRANADA AEROPUERTO (valle, serie larga 1971–presente)
    - 5514: GRANADA BASE AÉREA (similar)
    - 5103E: CAMARATE 2, P.N. Sierra Nevada (datos limitados)

    API key: pásala como argumento, define `AEMET_API_KEY` en el entorno, o
    añádela a `.env` en la raíz del repo.
    """
    import json

    RUTA_AEMET.mkdir(parents=True, exist_ok=True)
    destino = RUTA_AEMET / f"{estacion}_{fecha_inicio}_{fecha_fin}.parquet"

    if destino.exists() and not forzar:
        df = pd.read_parquet(destino)
        return pd.Series(
            df["prec"].values,
            index=pd.DatetimeIndex(df["fecha"].values, name="fecha"),
            name=f"lluvia_aemet_{estacion}",
        )

    chunk_dir = RUTA_AEMET / estacion
    chunk_dir.mkdir(parents=True, exist_ok=True)
    key = _leer_api_key_aemet(api_key)

    registros: list = []
    chunks = list(_chunks_6_meses(fecha_inicio, fecha_fin))
    for i, (ini, fin) in enumerate(chunks, 1):
        chunk_file = chunk_dir / f"chunk_{ini[:10]}.json"
        if chunk_file.exists() and not forzar:
            registros.extend(json.loads(chunk_file.read_text(encoding="utf-8")))
            continue
        url = URL_AEMET_DAILY.format(ini=ini, fin=fin, idema=estacion)
        data = _aemet_get(url, key)
        chunk_file.write_text(json.dumps(data), encoding="utf-8")
        registros.extend(data)
        # Sleep proportionally to staying under AEMET's ~50 req/min budget.
        # Each chunk makes 2 requests (meta + datos), so 3 s/chunk ≈ 40 req/min.
        time.sleep(3.0)

    df = pd.DataFrame({
        "fecha": [pd.Timestamp(r["fecha"]) for r in registros],
        "prec": [_parse_prec_aemet(r.get("prec")) for r in registros],
    })
    df = df.drop_duplicates(subset="fecha").sort_values("fecha")

    idx = pd.date_range(fecha_inicio, fecha_fin, freq="D", name="fecha")
    df = df.set_index("fecha").reindex(idx).reset_index().rename(columns={"index": "fecha"})
    df.to_parquet(destino, index=False)

    return pd.Series(
        df["prec"].values,
        index=pd.DatetimeIndex(df["fecha"].values, name="fecha"),
        name=f"lluvia_aemet_{estacion}",
    )


# -----------------------------------------------------------------------------
# Helpers diagnóstico
# -----------------------------------------------------------------------------


def resumen(serie: pd.Series) -> pd.Series:
    """Resumen compacto para inspección rápida."""
    return pd.Series(
        {
            "n": len(serie),
            "n_validos": int(serie.notna().sum()),
            "n_nan": int(serie.isna().sum()),
            "inicio": serie.index.min(),
            "fin": serie.index.max(),
            "media": float(np.nanmean(serie.values)),
            "mediana": float(np.nanmedian(serie.values)),
            "min": float(np.nanmin(serie.values)),
            "max": float(np.nanmax(serie.values)),
        }
    )
