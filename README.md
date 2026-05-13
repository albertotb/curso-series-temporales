# Curso: Series Temporales con Python (Hidrología e Hidrogeología)

## Información general

- **Duración:** 20 horas
- **Estructura:** 4 sesiones de 5 horas
- **Idioma:** Español
- **Enfoque:** Aplicado a series temporales hidrometeorológicas (caudales y piezometría)
- **Programa de referencia:** `Programa_curso_v3.docx`

> **Nota:** El programa actual (`v3`) indica sesiones de 4,5 h (total 18 h). El curso final será de **5 h por sesión / 20 h totales**, por lo que habrá que redistribuir tiempos al desarrollar los materiales.

## Objetivos

- Cubrir el _workflow_ completo en Python: descarga/carga de datos, preprocesamiento, modelado (estadístico, ML, DL) y evaluación.
- Aplicar los modelos a series hidrometeorológicas reales (aguas superficiales y subterráneas).
- Comparar la capacidad de distintos métodos para predecir eventos extremos (lluvia y sequía).

No es un curso de hidro(geo)logía, sino de modelos de series temporales **aplicados** a este dominio.

## Programa (resumen)

### Sesión 1 — Fundamentos, preprocesamiento y modelos estadísticos (Módulos 1 y 2)

- Teoría/ejemplos: conceptos básicos (estacionariedad, tendencia, estacionalidad, ruido), descomposición STL, autocorrelación y correlación cruzada, manejo de outliers y faltantes, agregación temporal, ARIMA, suavizado exponencial, funciones de respuesta a impulsos (Pastas).
- Práctica: carga, exploración, limpieza y visualización en Python (`pandas`, `Pastas`).

### Sesión 2 — Modelos estadísticos / Pastas (Módulo 2)

- Práctica completa: ajuste ARIMA y exponencial, modelos con `Pastas`, validación y comparación.

### Sesión 3 — Machine Learning / Deep Learning (Módulo 3, teoría)

- Introducción a ML supervisado para predicción.
- Regresión lineal, Random Forest, Gradient Boosting.
- Feature engineering para series temporales.
- Redes neuronales recurrentes (LSTM, GRU); mención a TCN y Transformers.
- Métricas y evaluación.

### Sesión 4 — Machine Learning / Deep Learning + Caso práctico (Módulos 3 y 5)

- Práctica con `scikit-learn` y `TensorFlow`/`PyTorch`.
- Variables retardadas, ventanas móviles, entrenamiento, evaluación e interpretación.
- Proyecto final: pipeline completo (preprocesamiento → modelado → evaluación).

## Datasets de ejemplo

- **Aguas superficiales (caudales):** río Genil — punto `A20_GENIL_TOCON`, captando la crecida de febrero 2026. Lluvia representativa asociada: `P82_D_MENCIA`. Fuente: CH Guadalquivir (SAIH), [Datos históricos → Versión clásica](https://www.chguadalquivir.es/saih/DatosHistoricos.aspx).
- **Aguas subterráneas (piezometría):** pozo `PZ0267014` cerca de Valladolid (cuenca del Duero), afectado por extracciones para regadío. Variable: `COTA PIEZOMÉTRICA` en la hoja `DATOS PIEZOMETRICOS` de `Datos_Piezometria_Red_Nivel_CHD (hasta diciembre 2024).xlsx`.
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
- **Gestión de dependencias:** [`uv`](https://docs.astral.sh/uv/). Python 3.11.
- **Librerías clave:** `pandas`, `numpy`, `matplotlib`, `statsmodels`, `pmdarima`, `pastas`, `scikit-learn`, `xgboost`, `lightgbm`, `torch`, `jupyterlab`. Lista completa en `pyproject.toml`.
- **Librerías candidatas a cubrir (a decidir al desarrollar los materiales):**
  - [`skforecast`](https://skforecast.org/) — convierte modelos `scikit-learn` (RF, XGBoost, LightGBM, CatBoost) en forecasters recursivos/directos. Tutoriales nativos en español (Joaquín Amat).
  - [`sktime`](https://www.sktime.net/) — marco unificado al estilo `scikit-learn` para forecasting, clasificación y clustering de series.
  - Suite **Nixtla**: [`statsforecast`](https://nixtlaverse.nixtla.io/statsforecast/) (clásicos: AutoARIMA, AutoETS, TBATS), [`mlforecast`](https://nixtlaverse.nixtla.io/mlforecast/) (features automáticas + ML global), [`neuralforecast`](https://nixtlaverse.nixtla.io/neuralforecast/) (NBEATS, NHITS, TFT, PatchTST, iTransformer).
  - [`prophet`](https://facebook.github.io/prophet/) — modelo aditivo bayesiano (tendencia + estacionalidad + holidays + changepoints). Buena baseline para series hidrológicas con estacionalidad anual fuerte; gestiona bien faltantes y outliers.
  - [`darts`](https://unit8co.github.io/darts/) — librería "todo en uno" con 60+ modelos (ARIMA, Prophet, N-BEATS, TFT, LSTM, XGBoost, Chronos, TimesFM) bajo una API tipo `scikit-learn`. Útil pedagógicamente para comparar familias de modelos con el mismo código.

## Estructura del repositorio

```text
curso_series_temporales/
├── README.md                    # Este archivo
├── CLAUDE.md                    # Notas mínimas para asistentes de IA
├── pyproject.toml               # Dependencias (uv)
├── .python-version              # 3.11
├── _quarto.yml                  # Config global de Quarto
├── Programa_curso_v3.docx       # Programa de referencia
├── Datos_Piezometria_*.xlsx     # Datos piezométricos
├── data/
│   ├── raw/                     # Datos crudos descargados (no versionados)
│   └── processed/               # Datos procesados (no versionados)
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
