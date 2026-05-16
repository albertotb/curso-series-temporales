# `data/` — datos del curso

Estructura:

- `data/raw/` — **versionado en git**. Datos crudos tal y como salen de cada
  fuente, sin transformar.
- `data/processed/` — **no versionado**. Salidas intermedias regenerables.

Toda la lógica de carga vive en [`src/cst/datos.py`](../src/cst/datos.py); los
notebooks acceden con `from cst import datos as ud`.

---

## Fuentes (5)

### 1. CHD · Piezometría (`piezometria_chd_2024-12.xlsx`)

- **Qué:** cota piezométrica (m s.n.m.) de ~600 pozos de la cuenca del Duero,
  con mediciones manuales (mensuales o irregulares). El curso usa el pozo
  `PZ0267014` (Renedo de Esgueva, Valladolid).
- **Fuente:** Red Oficial de Seguimiento Piezométrico de la CH del Duero, vía
  MITECO. Descarga manual desde
  [Red de seguimiento piezométrico (MITECO)](https://www.miteco.gob.es/es/agua/temas/evaluacion-de-los-recursos-hidricos/red-oficial-seguimiento/red-seguimiento-piezometrico.html).
- **Formato:** Excel multi-hoja; usamos la hoja `DATOS PIEZOMETRICOS`.
- **Acceso:** `ud.cargar_piezometria("PZ0267014")`.

### 2. CEDEX · Anuario de Aforos (`anuario_aforos/`)

- **Qué:** registros oficiales de la red ROEA (Red Oficial de Estaciones de
  Aforo). Tres CSV por demarcación:
  - `GUADALQUIVIR_afliq.csv` — caudal medio diario, todas las estaciones.
  - `GUADALQUIVIR_estaf.csv` — catálogo (coordenadas, código SAIH equivalente).
  - `GUADALQUIVIR_evap.csv` — precipitación y evaporación mensual en
    estaciones evaporimétricas (en embalses).
- **Fuente:** CEDEX-CEH, [Anuario de Aforos](https://ceh.cedex.es/anuarioaforos/).
  Cobertura hasta el año hidrológico **2020-21**.
- **Acceso:** `ud.descargar_anuario_csv(...)` (HTTP, cacheado),
  `ud.cargar_anuario_caudal(indroea=5020)`,
  `ud.cargar_anuario_precip_mensual(ref_evap=5001)`,
  `ud.cargar_anuario_estaciones()`.
- **Nota técnica:** el servidor del CEDEX requiere un `HTTPAdapter` con
  `SECLEVEL=1` (cifrado TLS heredado). Ya está implementado en `datos.py`.

### 3. SAIH-CHG · Datos históricos (`saih_chg/HistSAIH.xlsx`)

- **Qué:** caudal `A20_211_X` (m³/s, media horaria) y precipitación `A20_202`
  (l/m² ≈ mm, acumulado horario) en el cluster A20 (Genil-Tocón). Cobertura
  2018-01-01 → presente, incluida la crecida de feb 2026.
- **Fuente:** [Datos Históricos SAIH-CHG](https://www.chguadalquivir.es/saih/DatosHistoricos.aspx).
  WebForm ASP.NET sin API: descarga **manual** (ver
  [`notebooks/sesion1/00_descarga_datos.ipynb`](../notebooks/sesion1/00_descarga_datos.ipynb)
  para los pasos exactos: cluster A20 → Dato = Caudal + Precipitación →
  Formato = Excel).
- **Formato:** Excel con dos hojas (`Info` con metadatos, `Datos` con la tabla
  horaria + un bloque "Estadísticas" al final que las funciones descartan).
  Leído con engine `calamine` (openpyxl falla con este fichero).
- **Acceso:** `ud.cargar_caudal_genil()` y `ud.cargar_lluvia_genil()` —
  resamplean a media diaria (caudal) y suma diaria (lluvia).

### 4. Open-Meteo · ERA5 reanalysis (`openmeteo/`)

- **Qué:** precipitación diaria (mm) en cualquier coordenada (lat, lon)
  obtenida del reanálisis ERA5 (~25 km de resolución). Cubre 1970-presente.
- **Fuente:** [Open-Meteo Archive API](https://open-meteo.com/en/docs/historical-weather-api).
  HTTP gratis, sin API key.
- **Acceso:** `ud.descargar_lluvia_openmeteo(lat, lon, ...)` (con caché en
  CSV). Atajos: `ud.cargar_lluvia_genil_diaria()` (Pinos-Genil) y
  `ud.cargar_lluvia_duero_diaria()` (PZ0267014).
- **Cuándo usarla:** como sustituto regional cuando no hay estación cercana
  (p.ej. la piezometría del Duero), o para comparar fuente modelo vs estación.

### 5. AEMET OpenData (`aemet/`)

- **Qué:** precipitación diaria oficial (mm) por estación. Estaciones útiles
  para el curso: `5530E` Granada Aeropuerto (1971-presente, serie larga),
  `5103E` Camarate (Sierra Nevada, datos limitados).
- **Fuente:** [AEMET OpenData](https://opendata.aemet.es/centrodedescargas/inicio).
  HTTP con **API key** gratuita (registro → email con la key).
- **Acceso:** `ud.cargar_lluvia_aemet(estacion="5530E", ...)`. La key se lee
  de `AEMET_API_KEY` (variable de entorno o `.env` en la raíz del repo).
- **Cuándo usarla:** trends multidecadales en lluvia oficial. Maneja peculiares
  de calidad real: `Ip` (inappreciable, < 0.1 mm) y `Acum` (acumulada en otro
  día, → NaN). Descarga paginada en chunks de 90 días, con reintentos para
  el rate-limit y backoff exponencial.
