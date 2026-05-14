"""Carga y descarga de datasets para la Sesión 1.

Tres fuentes:

1. **CHD piezometría** (`PZ0267014`) — Excel local en `data/raw/`.
2. **CEDEX Anuario de Aforos** — CSV público para datos históricos diarios de
   caudal y estaciones del Guadalquivir (Pinos-Genil = `indroea` 5020 hasta
   2020-12-31). Usamos esta fuente como base reproducible.
3. **SAIH Guadalquivir** — para datos recientes (p.ej. la crecida de feb 2026).
   El portal es un WebForm ASP.NET sin API pública: la descarga se hace **a
   mano** desde https://www.chguadalquivir.es/saih/DatosHistoricos.aspx y los
   CSV se colocan en `data/raw/` con los nombres convenidos. Si el archivo
   existe, las funciones lo cargan; si no, devuelven la serie ROEA equivalente.

Estructura de archivos esperada en `data/raw/` (todos opcionales salvo el de
piezometría):

```
data/raw/
├── piezometria_chd_2024-12.xlsx
├── anuario_aforos/                       # se crea con descargar_anuario_csv
│   ├── GUADALQUIVIR_afliq.csv
│   ├── GUADALQUIVIR_estaf.csv
│   └── GUADALQUIVIR_evap.csv
├── saih_A20_GENIL_TOCON.csv              # manual desde SAIH (opcional)
└── saih_P82_D_MENCIA.csv                 # manual desde SAIH (opcional)
```
"""

from __future__ import annotations

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

RUTA_SAIH_GENIL = RUTA_RAW / "saih_A20_GENIL_TOCON.csv"
RUTA_SAIH_MENCIA = RUTA_RAW / "saih_P82_D_MENCIA.csv"


def _cargar_saih_csv(ruta: Path, columna_valor: str, nombre_serie: str) -> pd.Series:
    """Lector genérico para los CSV exportados manualmente desde el SAIH.

    El SAIH exporta tablas con cabecera tipo:

        Fecha;Hora;<estacion> (unidades)
        12/02/2026;00:00;12.34
        ...

    Esta función es tolerante a pequeñas variaciones (separador `;` o `,`,
    decimal `,` o `.`, columna fecha+hora combinada o separada).
    """
    df = pd.read_csv(ruta, sep=None, engine="python", decimal=",", encoding="latin-1")
    df.columns = [c.strip() for c in df.columns]

    if "Fecha" in df.columns and "Hora" in df.columns:
        fechas = pd.to_datetime(
            df["Fecha"].astype(str) + " " + df["Hora"].astype(str),
            format="%d/%m/%Y %H:%M",
            errors="coerce",
        )
    else:
        col_fecha = next(c for c in df.columns if "fecha" in c.lower())
        fechas = pd.to_datetime(df[col_fecha], dayfirst=True, errors="coerce")

    col_valor = next((c for c in df.columns if columna_valor.lower() in c.lower()), df.columns[-1])
    valores = pd.to_numeric(
        df[col_valor].astype(str).str.replace(",", ".", regex=False), errors="coerce"
    )

    serie = pd.Series(valores.values, index=pd.DatetimeIndex(fechas, name="fecha"), name=nombre_serie)
    serie = serie.dropna(how="all")
    serie = serie.groupby(serie.index).mean()
    return serie.sort_index()


def cargar_caudal_genil(
    indroea_fallback: int = 5020,
) -> pd.Series:
    """Caudal del Genil.

    Prefiere el CSV manual del SAIH (`A20_GENIL_TOCON`) si está disponible;
    en su defecto, devuelve la serie de la estación ROEA indicada
    (Pinos-Genil 5020 por defecto, datos hasta 2020-12-31).
    """
    if RUTA_SAIH_GENIL.exists():
        return _cargar_saih_csv(RUTA_SAIH_GENIL, "caudal", "caudal_A20_GENIL_TOCON")
    return cargar_anuario_caudal(indroea_fallback)


def cargar_lluvia_mencia(ref_evap_fallback: int = 5001) -> pd.Series:
    """Lluvia diaria en P82_D_MENCIA si está descargada; si no, mensual en
    Iznájar (ref_evap=5001) del Anuario como sustituto."""
    if RUTA_SAIH_MENCIA.exists():
        return _cargar_saih_csv(RUTA_SAIH_MENCIA, "precip", "lluvia_P82_D_MENCIA")
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
# 5. AEMET OpenData (placeholder)
# -----------------------------------------------------------------------------


def cargar_lluvia_aemet(
    estacion: str,
    fecha_inicio: str,
    fecha_fin: str,
    api_key: str | None = None,
) -> pd.Series:
    """Lluvia diaria desde AEMET OpenData.

    *No implementado todavía*: AEMET OpenData requiere API key (gratis tras
    registro en https://opendata.aemet.es/centrodedescargas/altaUsuario). El
    endpoint de valores climatológicos diarios es:

        GET https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/
            datos/fechaini/{fechaIniStr}/fechafin/{fechaFinStr}/estacion/{idema}

    Devuelve un JSON con una URL `datos` desde la que se descarga el array final.

    Cuando se complete: añadir cliente en este módulo y reemplazar
    `cargar_lluvia_genil_diaria` / `cargar_lluvia_duero_diaria` para preferir
    AEMET si la clave está disponible.
    """
    raise NotImplementedError(
        "AEMET OpenData necesita API key. Regístrate gratis en "
        "https://opendata.aemet.es y pasa la clave en `api_key=`. "
        "Mientras tanto, usa `cargar_lluvia_*_diaria()` (Open-Meteo)."
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
