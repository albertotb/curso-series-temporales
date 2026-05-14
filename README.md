# Curso: Series Temporales con Python (Hidrología e Hidrogeología)

## Información general

- **Duración:** 20 horas (4 sesiones × 5 h = 4,5 h de contenido + 0,5 h descanso por sesión)
- **Idioma:** Español
- **Enfoque:** Aplicado a series temporales hidrometeorológicas (caudales y piezometría)
- **Programa de referencia:** `docs/Programa_curso_v3.docx` (currículo detallado en `curriculum.md`)

## Objetivos

- Cubrir el _workflow_ completo en Python: descarga/carga de datos, preprocesamiento, modelado (estadístico, ML, DL) y evaluación.
- Aplicar los modelos a series hidrometeorológicas reales (aguas superficiales y subterráneas).
- Comparar la capacidad de distintos métodos para predecir eventos extremos (lluvia y sequía).

No es un curso de hidro(geo)logía, sino de modelos de series temporales **aplicados** a este dominio.

## Programa (resumen)

Detalle bloque a bloque, tiempos y notebooks en [`curriculum.md`](curriculum.md).

### Sesión 1 — Fundamentos y exploración (3 h teoría + 1,5 h práctica)

- Teoría: definición y tipos de series temporales hidrometeorológicas; componentes y estacionariedad; descomposición STL; autocorrelación (ACF/PACF) y correlación cruzada (CCF); limpieza de outliers, faltantes y agregación temporal.
- Práctica: carga, limpieza y exploración en Python de la serie de caudal del Genil y la piezometría del Duero (`pandas`, `statsmodels`).

### Sesión 2 — Modelos estadísticos y Pastas (1 h 15 min teoría + 3 h 15 min práctica)

- Teoría (1 h 15 min): AR/MA/ARMA/ARIMA/SARIMA/SARIMAX, Box–Jenkins, criterios de información, ETS, Prophet, Pastas (concepto).
- Notebooks: SARIMAX + ETS en caudal, Prophet como baseline, Pastas con lluvia+extracciones, validación walk-forward y comparación con métricas hidrológicas (NSE, KGE, error en pico).

### Sesión 3 — Machine Learning clásico, evaluación y splits (3 h teoría + 1,5 h práctica)

- Teoría: de serie temporal a problema supervisado; feature engineering (lags, rolling, calendario, Fourier); Ridge/Lasso, Random Forest, XGBoost, LightGBM con `skforecast`; estrategias multi-paso (recursive/direct); splits temporales y CV; métricas hidrológicas.
- Práctica: matriz de features + baseline lineal; RF y XGBoost con `skforecast`; backtesting y métricas sobre la crecida de febrero 2026.

### Sesión 4 — Deep Learning con demos + proyecto final (3 h DL guiado + 1,5 h proyecto)

- Demos teoría-código en vivo (alumno reproduce en paralelo): RNN/LSTM/GRU; LSTM sobre el caudal del Genil con `tensorflow` + `keras` (preparación de ventanas, callbacks, regularización); comparación final estadísticos vs ML vs DL; demo de [`neuralhydrology`](https://neuralhydrology.readthedocs.io/) como referente del DL hidrológico moderno; interpretabilidad y análisis de errores.
- Proyecto final guiado: pipeline completo sobre caudal o piezometría con elección libre de modelos.

## Datasets de ejemplo

- **Aguas superficiales (caudales):** río Genil — punto `A20_GENIL_TOCON`, captando la crecida de febrero 2026. Lluvia representativa asociada: `P82_D_MENCIA`. Fuente: CH Guadalquivir (SAIH), [Datos históricos → Versión clásica](https://www.chguadalquivir.es/saih/DatosHistoricos.aspx).
- **Aguas subterráneas (piezometría):** pozo `PZ0267014` cerca de Valladolid (cuenca del Duero), afectado por extracciones para regadío. Variable: `COTA PIEZOMÉTRICA` en la hoja `DATOS PIEZOMETRICOS` de `piezometria_chd_2024-12.xlsx`.
- **Meteorología:** nodo correspondiente de la rejilla AEMET. Coordenadas del nodo en la hoja `LISTADO_PUNTOS` del mismo Excel.

## Fuentes de datos (referencia general)

### Escala nacional

- **MITECO**
  - Piezometría: <https://www.miteco.gob.es/es/agua/temas/evaluacion-de-los-recursos-hidricos/red-oficial-seguimiento/red-seguimiento-piezometrico.html>
  - Manantiales: <https://www.miteco.gob.es/es/agua/temas/evaluacion-de-los-recursos-hidricos/red-oficial-seguimiento/red-de-seguimiento-hidrometrico-de-manantiales.html>
  - Aforos: <https://www.miteco.gob.es/es/cartografia-y-sig/ide/descargas/agua/anuario-de-aforos.html>
  - SAIH: <https://www.miteco.gob.es/es/agua/temas/evaluacion-de-los-recursos-hidricos/saih.html>
- **AEMET (rejilla):** <https://www.aemet.es/es/serviciosclimaticos/cambio_climat/datos_diarios?w=1>
- **SARAI (IGME):** <https://sarai-data.igme.es/>
- **Escenarios climáticos**
  - AdapteCCa: <https://escenarios.adaptecca.es/>
  - ECMWF (seasonal): <https://www.ecmwf.int/en/forecasts/documentation-and-support/seasonal>

### Escala europea

- **WISE / EEA:** <https://sdi.eea.europa.eu/>
- **IGRAC (GGIS / GGMN):** <https://ggis.un-igrac.org/>

## Bibliografía

- Hyndman & Athanasopoulos, _Forecasting: Principles and Practice_ (3rd ed., `fpp3`): <https://otexts.com/fpp3/>

## Stack técnico

- **Slides teóricas:** [Quarto](https://quarto.org) (`.qmd`) renderizado a **reveal.js (HTML)**. Tema corporativo Komorebi en `slides/_theme/komorebi.scss`.
- **Prácticas:** Jupyter notebooks (`.ipynb`).
- **Gestión de dependencias:** [`uv`](https://docs.astral.sh/uv/). Python ≥3.12.
- **Librerías por sesión** (decisión tras la comparación documentada en `curriculum.md` §A):
  - **Sesión 1 (fundamentos):** `pandas`, `numpy`, `matplotlib`, `statsmodels` (STL, ACF/PACF, tests).
  - **Sesión 2 (modelos estadísticos + Pastas):** `statsmodels` (ARIMA/SARIMA/ETS + diagnóstico de residuos), [`prophet`](https://facebook.github.io/prophet/) (baseline aditivo con estacionalidad/holidays/changepoints), [`pastas`](https://pastas.readthedocs.io/) (modelos de respuesta a impulsos para piezometría).
  - **Sesión 3 (ML + forecasting):** `scikit-learn`, `xgboost`, `lightgbm`, [`skforecast`](https://skforecast.org/) (convierte regresores sklearn en forecasters; **docs nativas en español** de Joaquín Amat), `shap` (interpretabilidad).
  - **Sesión 4 (DL):** `tensorflow` + [`keras`](https://keras.io/) (LSTM/GRU con API de alto nivel y tutorial oficial de TS); [`neuralhydrology`](https://neuralhydrology.readthedocs.io/) como **demo de referencia** del DL hidrológico (Kratzert et al., JKU Linz) — se ejecuta vía YAML, no como librería de práctica.
- Lista completa en `pyproject.toml`.

Librerías evaluadas y **descartadas** (razonadas en `curriculum.md` §A.3): `pmdarima`, `statsforecast`, `mlforecast`, `neuralforecast`, `sktime`, `darts`, `torch`/`pytorch-lightning`, `tsai`.

## Estructura del repositorio

```text
curso_series_temporales/
├── README.md                    # Este archivo
├── CLAUDE.md                    # Notas mínimas para asistentes de IA
├── pyproject.toml               # Dependencias (uv)
├── .python-version              # 3.11
├── _quarto.yml                  # Config global de Quarto
├── Programa_curso_v3.docx       # Programa de referencia
├── data/
│   ├── raw/                     # Datos crudos (versionados): aforos, piezometría, lluvia
│   └── processed/               # Datos procesados (no versionados, regenerables)
├── slides/
│   ├── _theme/
│   │   └── komorebi.scss        # Tema Quarto reveal.js (paleta Komorebi)
│   ├── sesion1/sesion1.qmd
│   ├── sesion2/sesion2.qmd
│   ├── sesion3/sesion3.qmd
│   └── sesion4/sesion4.qmd
└── notebooks/
    ├── sesion1/                 # Carga, exploración, ACF/CCF
    ├── sesion2/                 # ARIMA, ETS, Pastas
    ├── sesion3/                 # ML/DL teoría aplicada
    └── sesion4/                 # ML/DL práctica + proyecto final
```

## Puesta en marcha

```bash
# 1. Instalar uv (una sola vez) — ver https://docs.astral.sh/uv/
# macOS/Linux:   curl -LsSf https://astral.sh/uv/install.sh | sh
# Windows:       powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# 2. Crear entorno e instalar dependencias
uv sync

# 3. Arrancar Jupyter para prácticas
uv run jupyter lab

# 4. Renderizar / previsualizar slides (requiere Quarto instalado: https://quarto.org/docs/get-started/)
quarto render slides/sesion1/sesion1.qmd
quarto preview slides/sesion1/sesion1.qmd
```
