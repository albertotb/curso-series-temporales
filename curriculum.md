# Currículo extendido — Curso de Series Temporales con Python

> Versión detallada del programa resumido en `README.md`. Pensada como guía para preparar slides y notebooks, no como material entregable.
>
> **Duración:** 20 h (4 sesiones × 5 h). Distribución indicativa: ~3 h teoría/ejemplos + ~2 h práctica guiada por sesión.
> **Idioma:** español.
> **Datasets de referencia:**
>
> - Caudal: `A20_GENIL_TOCON` (río Genil — CH Guadalquivir), foco en la crecida de **febrero 2026**.
> - Lluvia: `P82_D_MENCIA` (mismo SAIH).
> - Piezometría: `PZ0267014` (cuenca del Duero) — `COTA PIEZOMÉTRICA`.
> - Meteo: nodo AEMET asociado al pozo.

---

## Sesión 1 — Fundamentos y exploración (5 h)

**Objetivo.** Que el alumno sepa cargar series hidrometeorológicas reales, explorarlas, limpiarlas y describirlas estadísticamente; y entienda los bloques conceptuales que justifican los modelos posteriores.

### Bloque 1.1 · ¿Qué es una serie temporal? (45 min)

- Definición: $\{y_t\}_{t=1}^{T}$, dependencia temporal.
- Frecuencias típicas en hidro: horaria, diaria, mensual, irregular.
- Diferencias frente a datos i.i.d.: por qué el train/test aleatorio **no** vale.
- Tipos de problemas: descripción, predicción puntual, predicción probabilística, detección de anomalías.
- Caso del curso: predicción de caudal y de cota piezométrica, énfasis en eventos extremos.

### Bloque 1.2 · Componentes y estacionariedad (1 h)

- Descomposición conceptual: tendencia + estacionalidad + ciclo + ruido (modelos aditivo y multiplicativo).
- Estacionariedad débil vs estricta. Por qué importa.
- Tests: ADF, KPSS (interpretación, no demostración).
- Transformaciones para estacionarizar: diferenciación, logaritmo, Box-Cox.
- **Descomposición STL** (`statsmodels.tsa.seasonal.STL`): robustez frente a outliers, ventana estacional.

### Bloque 1.3 · Autocorrelación y correlación cruzada (45 min)

- ACF y PACF: definición, lectura visual, intervalos de confianza.
- Cross-correlation (CCF): rezago lluvia → caudal como ejemplo canónico.
- Lag plots y diagramas de dispersión retardada.

### Bloque 1.4 · Limpieza de datos (45 min)

- **Outliers**: causas físicas (fallos de sensor, derivas) vs eventos reales (crecida). Métodos: z-score robusto (mediana/MAD), Hampel, IQR.
- **Faltantes**: tipos (MCAR, MAR, MNAR aplicado a hidro), métodos sencillos: forward-fill, interpolación lineal, interpolación estacional, imputación con modelo.
- Cuándo **no** rellenar (gaps largos en piezometría).
- Agregación temporal: `resample` (mean/sum/max), reglas distintas para lluvia (suma) y caudal/piezometría (media).

### Bloque 1.5 · Modelos estadísticos clásicos — visión general (1 h 30 min)

> Teoría ligera; la práctica intensa va en la Sesión 2.

- Ruido blanco y paseo aleatorio.
- AR(p), MA(q), ARMA, ARIMA, SARIMA (intuición + cuándo cada uno).
- Suavizado exponencial: simple, Holt, Holt-Winters.
- Introducción a **Pastas**: idea de respuesta a impulsos para piezometría (lluvia → nivel, bombeo → nivel).

### Práctica 1 — `notebooks/sesion1/`

1. **01_carga_y_exploracion.ipynb**
   - Cargar `A20_GENIL_TOCON` y `P82_D_MENCIA` desde el CSV/Excel del SAIH.
   - Inspeccionar `pd.DataFrame.info`, rango temporal, gaps, frecuencia real vs nominal.
   - Plots básicos: serie completa, año 2026, ventana de crecida.
2. **02_limpieza.ipynb**
   - Detectar outliers en caudal (z-score robusto) y discutir si conservarlos.
   - Rellenar faltantes cortos en lluvia (interpolación) y dejar gaps largos en piezometría.
   - Resamplear a diario y mensual; comprobar diferencias caudal vs lluvia.
3. **03_descomposicion_y_correlacion.ipynb**
   - STL de la serie de caudal y de cota piezométrica.
   - ACF/PACF de caudal y residuos de STL.
   - CCF lluvia ↔ caudal: identificar rezago dominante.

---

## Sesión 2 — Modelos estadísticos en profundidad y Pastas (5 h)

**Objetivo.** Que el alumno ajuste, diagnostique y compare modelos ARIMA/ETS y construya un modelo de respuesta a impulsos con Pastas sobre piezometría real.

### Bloque 2.1 · Metodología Box–Jenkins (45 min)

- Pasos: identificación → estimación → diagnóstico → predicción.
- Selección de órdenes con ACF/PACF y con criterios de información (AIC, BIC, AICc).
- `pmdarima.auto_arima`: qué hace por dentro, qué controlar (estacionalidad, transformaciones).

### Bloque 2.2 · ARIMA y SARIMA en caudales (1 h 15 min)

- Ajuste manual vs automático.
- Estacionalidad en hidro: anual evidente en caudal, semanal en piezometría con bombeo.
- Diagnóstico de residuos: Ljung-Box, normalidad, heterocedasticidad.
- Predicción puntual y bandas de confianza.

### Bloque 2.3 · Suavizado exponencial (45 min)

- ETS (Error/Trend/Seasonal): qué configuración elegir para caudal y piezometría.
- Comparación rápida ARIMA vs ETS sobre la misma serie.

### Bloque 2.4 · Modelado con Pastas (1 h 30 min)

- Filosofía: el nivel piezométrico responde a estímulos (lluvia, bombeo, recarga) vía funciones de impulso.
- `StressModel`, `RechargeModel`, modelos de bombeo.
- Calibración, intervalos de confianza, decomposición de contribuciones.
- Limitaciones: linealidad, estacionariedad de la respuesta.

### Bloque 2.5 · Validación y comparación (45 min)

- Split temporal: train / validation / test (no aleatorio).
- Walk-forward / expanding window.
- Métricas: RMSE, MAE, NSE (Nash-Sutcliffe), KGE, error en pico (relevante para crecidas).
- Test estadístico para comparar modelos: Diebold-Mariano (mención).

### Práctica 2 — `notebooks/sesion2/`

1. **01_arima_caudal.ipynb**
   - `auto_arima` sobre caudal diario del Genil.
   - Forecast 30 días con bandas; superponer con la crecida real de febrero 2026.
   - Análisis de residuos.
2. **02_ets_y_comparacion.ipynb**
   - ETS sobre piezometría mensual.
   - Comparación ARIMA vs ETS con métricas hidrológicas (NSE, KGE).
3. **03_pastas_piezometria.ipynb**
   - Modelo Pastas para `PZ0267014` con lluvia (AEMET) como input.
   - Añadir un `StressModel` ficticio de extracciones para discutir.
   - Visualizar contribuciones individuales.

---

## Sesión 3 — Machine Learning y Deep Learning (teoría aplicada) (5 h)

**Objetivo.** Que el alumno entienda cómo se reformula una serie temporal como problema supervisado, qué modelos clásicos de ML aplicar, y qué aportan (y qué no) las redes recurrentes/transformers.

### Bloque 3.1 · De serie temporal a problema supervisado (45 min)

- Sliding window: variables retardadas como features.
- Feature engineering específica para series:
  - Lags y diferencias.
  - Estadísticos móviles (rolling mean/std/min/max).
  - Variables de calendario (dayofyear, mes, día de la semana).
  - Variables de Fourier para estacionalidad continua.
  - Variables exógenas: lluvia agregada en ventanas, índices climáticos.
- Pitfall clásico: **fuga de información** (rolling windows que ven el futuro, escaladores ajustados con test).

### Bloque 3.2 · Modelos clásicos de ML (1 h 15 min)

- Regresión lineal regularizada (Ridge, Lasso) como baseline serio.
- Árboles y ensembles: Random Forest.
- Gradient Boosting: XGBoost, LightGBM (cuál preferir y por qué).
- Interpretabilidad: importancia de variables, SHAP (vista rápida).
- Validación cruzada temporal: `TimeSeriesSplit`, blocked CV.

### Bloque 3.3 · Estrategias de predicción multi-paso (30 min)

- Recursive (autoregresiva), Direct (un modelo por horizonte), DirRec, MIMO.
- Trade-offs: precisión vs acumulación de error vs coste de entrenamiento.

### Bloque 3.4 · Métricas y evaluación en hidrología (30 min)

- MAE, RMSE, MAPE, sMAPE: ventajas y trampas.
- Métricas hidrológicas: NSE, KGE, PBIAS, error en pico, percentil 95.
- Evaluación específica de **eventos extremos**: crecida y sequía.
- Predicción probabilística (mención): cuantiles, conformal prediction.

### Bloque 3.5 · Redes neuronales para series (1 h 30 min)

- MLP con features de lag: cuándo ya basta.
- **RNN**: idea de estado oculto, problema de gradientes.
- **LSTM** y **GRU**: motivación intuitiva (gates), arquitectura típica.
- 1D-CNN y **TCN** (causal dilated convolutions): mención y comparación con LSTM.
- **Transformers** para series (mención): atención, Informer/Autoformer/PatchTST.
- Cuándo usar DL y cuándo _no_ (regla práctica: pocas series cortas → ML; muchas series largas o multi-variadas → DL).

### Práctica 3 — `notebooks/sesion3/`

> Sesión más teórica; práctica corta para fijar conceptos.

1. **01_features_y_baseline.ipynb**
   - Construir matriz de features (lags + rolling + calendario + lluvia retardada) para caudal del Genil.
   - Baseline persistencia y baseline regresión lineal.
2. **02_rf_y_xgboost.ipynb**
   - Random Forest y XGBoost sobre las mismas features.
   - Feature importance y SHAP.
   - Comparación con ARIMA de la Sesión 2.
3. **03_intro_lstm.ipynb** _(opcional / demo)_
   - LSTM muy simple en PyTorch para predicción a 1 día.
   - Foco en preparar el `DataLoader` correctamente (escalado por train, ventanas no solapadas en test).

---

## Sesión 4 — Práctica end-to-end y proyecto final (5 h)

**Objetivo.** Que el alumno construya un pipeline completo, lo evalúe con criterio hidrológico y compare modelos estadísticos vs ML vs DL sobre los mismos datos.

### Bloque 4.1 · Diseño del pipeline (45 min)

- Estructura de un proyecto de TS reproducible.
- Carga → limpieza → features → split → train → eval → reporte.
- Reproducibilidad: semillas, versionado de datos, `freeze` en notebooks.

### Bloque 4.2 · Deep Learning práctico (1 h 30 min)

- LSTM/GRU multi-paso para caudal:
  - Preparación de tensores (B, T, F).
  - Normalización por train.
  - Loop de entrenamiento, early stopping, scheduler de LR.
  - Sobreajuste y regularización (dropout, weight decay).
- Visualización: predicción vs observado, residuos por horizonte.

### Bloque 4.3 · Comparación honesta de modelos (45 min)

- Mismo split, mismas métricas.
- Múltiples semillas en DL (medias y desviaciones).
- Test pareado para diferencias.
- Discusión: ¿en qué casos gana DL? ¿En qué casos ARIMA/RF basta?

### Bloque 4.4 · Interpretabilidad y errores (45 min)

- SHAP en modelos de árbol (revisión rápida).
- Análisis de errores por régimen: estiaje vs crecida.
- Foco específico en la **crecida de febrero 2026** y en la **bajada de cota** por extracciones en piezometría.

### Bloque 4.5 · Proyecto final guiado (1 h 15 min)

- Cada alumno (o equipo) construye un pipeline completo sobre uno de los dos datasets:
  - **A.** Caudal del Genil — predicción a 7 días con foco en la crecida.
  - **B.** Cota piezométrica `PZ0267014` — predicción a 1 mes con foco en bajadas por extracción.
- Entregable: notebook reproducible + breve reporte de comparación (ARIMA vs RF/XGB vs LSTM) con métricas hidrológicas.

### Práctica 4 — `notebooks/sesion4/`

1. **01_pipeline_features.ipynb** — reutiliza el de Sesión 3, refinado.
2. **02_lstm_multiscale.ipynb** — LSTM multi-paso, entrenado con cuidado.
3. **03_comparacion_final.ipynb** — tabla y gráficos comparativos ARIMA/RF/XGB/LSTM con NSE, KGE y error en pico.
4. **proyecto_final/** — plantilla a rellenar por el alumno.

---

## Apéndices

### A. Librerías por sesión

#### A.1 Núcleo (estable, decidido)

| Sesión | Núcleo                                | Específicas                   |
| ------ | ------------------------------------- | ----------------------------- |
| 1      | `pandas`, `numpy`, `matplotlib`       | `statsmodels` (STL, ACF/PACF) |
| 2      | `statsmodels`, `pmdarima`             | `pastas`                      |
| 3      | `scikit-learn`, `xgboost`, `lightgbm` | `shap`, `torch` (intro)       |
| 4      | `torch`, `scikit-learn`               |                               |

#### A.2 Candidatas a integrar (a decidir tras comparación)

Estas librerías aparecen en la investigación como referentes; aún no están asignadas a una sesión. Se elegirán entre ellas (no necesariamente todas) tras una comparación lado a lado — ver tabla en A.3.

| Librería                                                                   | Tipo                                         | Encaje natural en el curso                                                                                                                            |
| -------------------------------------------------------------------------- | -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`prophet`](https://facebook.github.io/prophet/)                           | Modelo aditivo bayesiano                     | **Sesión 2** como alternativa/baseline a ARIMA y ETS — encaja por estacionalidad anual fuerte (caudal, piezometría) y por tolerar faltantes/outliers. |
| [`skforecast`](https://skforecast.org/)                                    | Wrapper sobre `scikit-learn`                 | **Sesión 3** — puente natural entre ML clásico y forecasting: convierte RF/XGBoost/LightGBM en forecasters recursivos/directos. Docs en español.      |
| [`sktime`](https://www.sktime.net/)                                        | Marco unificado tipo `scikit-learn`          | **Sesión 3** (alternativa a `skforecast`) — API homogénea para forecasting, clasificación y CV temporal.                                              |
| [`statsforecast`](https://nixtlaverse.nixtla.io/statsforecast/) (Nixtla)   | Clásicos rápidos                             | **Sesión 2** (alternativa a `statsmodels` + `pmdarima`) — AutoARIMA/ETS/TBATS muy rápidos, misma API que el resto de la suite Nixtla.                 |
| [`mlforecast`](https://nixtlaverse.nixtla.io/mlforecast/) (Nixtla)         | ML "global" con features automáticas         | **Sesión 3** — feature engineering automático (lags, rolling, fechas) + cualquier modelo sklearn. Útil si predecimos varias estaciones a la vez.      |
| [`neuralforecast`](https://nixtlaverse.nixtla.io/neuralforecast/) (Nixtla) | DL (PyTorch)                                 | **Sesión 4** — NBEATS, NHITS, TFT, PatchTST, iTransformer bajo API uniforme. Alternativa a escribir LSTM "a mano" en PyTorch.                         |
| [`darts`](https://unit8co.github.io/darts/)                                | "Todo en uno" (stats + ML + DL + foundation) | **Transversal** — su valor pedagógico está en comparar familias de modelos con el mismo código. Podría usarse en Sesión 4 para la comparación final.  |

#### A.3 Comparación lado a lado

Datos de GitHub a fecha **2026-05-13**. Funcionalidades verificadas en la documentación de cada librería.

| Criterio                                  | `statsmodels` + `pmdarima`     | `statsforecast`         | `prophet`           | `skforecast`                  | `sktime`                       | `mlforecast`            | `neuralforecast`              | `darts`                          |
| ----------------------------------------- | ------------------------------ | ----------------------- | ------------------- | ----------------------------- | ------------------------------ | ----------------------- | ----------------------------- | -------------------------------- |
| Cubre clásicos (ARIMA/ETS)                | Sí (núcleo)                    | Sí (Auto*, TBATS)       | Sí (modelo propio)  | No (integra `statsmodels`)    | Sí (incluye Auto-ARIMA)        | No                      | No                            | Sí (ARIMA, ETS, Theta)           |
| Cubre ML (XGBoost/LightGBM)               | No                             | No                      | No                  | Sí (núcleo)                   | Sí (vía `make_reduction`)      | Sí (núcleo)             | No                            | Sí (`RegressionModel`)           |
| Cubre DL (LSTM/TFT/PatchTST)              | No                             | No                      | No                  | Parcial (`ForecasterRnn`)     | Parcial (wraps neuralforecast) | No                      | Sí (núcleo: TFT/PatchTST/iTr) | Sí (RNN/TFT/N-BEATS/TiDE)        |
| Multi-paso recursivo y directo            | Recursivo                      | Recursivo + directo     | Directo (fechas)    | Recursivo + Directo + DirRec  | Recursivo + Directo + MIMO     | Recursivo + Directo     | Directo (multi-output)        | Recursivo + Directo              |
| Covariables exógenas (lluvia)             | Sí (SARIMAX)                   | Sí                      | Sí (regressors)     | Sí (`exog`)                   | Sí (`X` en fit/predict)        | Sí                      | Sí (futr/hist/stat exog)      | Sí (past/future/static, muy rico)|
| Intervalos / probabilístico               | Sí (paramétricos)              | Sí (param + conformal)  | Sí (MCMC)           | Sí (bootstrap, conformal)     | Sí (interval framework)        | Sí (conformal)          | Sí (quantile, distribucional) | Sí (probabilístico nativo)       |
| CV temporal (walk-forward)                | Manual                         | Sí (`cross_validation`) | Sí (helper)         | Sí (backtesting muy completo) | Sí (Sliding/Expanding splitters)| Sí (`cross_validation`)| Sí (`cross_validation`)       | Sí (`historical_forecasts`)      |
| Documentación / tutoriales en español     | No oficial (apuntes UC3M, UCM) | Parcial (equipo hispano)| No oficial          | **Sí (cienciadedatos.net)**   | No                             | Parcial                 | Parcial                       | No                               |
| Curva de aprendizaje                      | Media-alta                     | Baja                    | Muy baja            | Baja-media (API sklearn-like) | Media-alta                     | Media                   | Media-alta                    | Media                            |
| Mantenimiento (2024-2026)                 | Activo                         | Muy activo              | Activo (Meta)       | Muy activo                    | Muy activo                     | Muy activo              | Muy activo                    | Muy activo                       |
| Encaje hidrológico (casos publicados)     | Sí (estándar)                  | Parcial (lib reciente)  | Sí (varios papers)  | Parcial (algún caso en docs)  | Parcial (más industrial)       | No documentado          | Sí (análogo a NeuralHydrology)| Sí (varios papers)               |
| **GitHub stars**                          | 11.4k / 1.7k                   | 4.8k                    | 20.2k               | 1.5k                          | 9.8k                           | 1.2k                    | 4.1k                          | 9.4k                             |
| **Contribuidores**                        | 484 / 24                       | 62                      | 191                 | 29                            | 573                            | 24                      | 62                            | 156                              |
| **Última release**                        | 2025-12 / 2025-11              | 2025-10                 | 2026-01             | 2026-04                       | 2025-11                        | 2026-03                 | 2026-05                       | 2026-05                          |
| **Cadencia de releases**                  | ~2-3 / año                     | ~trimestral             | ~semestral          | mensual                       | mensual                        | mensual+                | mensual+                      | mensual                          |
| **Licencia**                              | BSD-3 / MIT                    | Apache-2.0              | MIT                 | BSD-3                         | BSD-3                          | Apache-2.0              | Apache-2.0                    | Apache-2.0                       |

#### A.4 Conclusiones y recomendación

**Lectura rápida de la tabla:**

- **Más populares (stars):** `prophet` (20.2k) > `statsmodels` (11.4k) > `sktime` (9.8k) ≈ `darts` (9.4k) > `statsforecast` (4.8k) > `neuralforecast` (4.1k). Pero stars ≠ idoneidad pedagógica.
- **Mejor mantenimiento:** la suite Nixtla (`statsforecast` / `mlforecast` / `neuralforecast`), `skforecast`, `sktime` y `darts` publican mensualmente. `statsmodels` y `prophet` van más lentos pero son estables.
- **Comunidad más grande (contribuidores):** `sktime` (573) y `statsmodels` (484). Las demás tienen equipos pequeños pero activos.
- **Única con docs nativas en español:** `skforecast` (Joaquín Amat / cienciadedatos.net). Diferencial fuerte para nuestra audiencia.
- **Más completas en un solo paquete:** `darts` y `sktime` cubren clásicos + ML + DL; el resto son especializadas.

**Propuesta de subconjunto mínimo (a validar):**

| Rol                                  | Librería elegida                                | Justificación                                                                                                                              |
| ------------------------------------ | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Manipulación, EDA, descomposición    | `pandas` + `statsmodels`                        | Estándar de facto; STL y ACF/PACF están en `statsmodels`.                                                                                  |
| Clásicos (ARIMA/ETS) — Sesión 2      | `statsforecast`                                 | Más rápido y moderno que `pmdarima`; AutoARIMA/AutoETS con la misma API que el resto de Nixtla; encaja con `mlforecast`/`neuralforecast`.  |
| Modelo de respuesta a impulsos       | `pastas`                                        | Sin alternativa real para piezometría.                                                                                                     |
| Baseline alternativo                 | `prophet`                                       | Bloque corto en Sesión 2: estacionalidad + holidays/extracciones + outliers. Muy poco coste de enseñanza.                                  |
| ML (RF/XGBoost/LightGBM) — Sesión 3  | `skforecast`                                    | Docs en español, API sklearn-like, backtesting muy completo. Encaja con el perfil del alumno y con el idioma del curso.                    |
| Interpretabilidad                    | `shap`                                          | Como ya estaba.                                                                                                                            |
| DL (LSTM/TFT) — Sesión 4             | `neuralforecast` + `torch` (vista a bajo nivel) | `torch` para la demo de LSTM "a mano" (entender por dentro); `neuralforecast` para comparar TFT/PatchTST con poco código.                 |
| Comparación final de modelos         | `darts` *(opcional)*                            | Solo si la comparación ARIMA vs RF vs LSTM se vuelve pesada con APIs distintas — `darts` unifica todas bajo una misma interfaz.            |

**Descartar (por ahora):**

- `pmdarima` — superado por `statsforecast` para `AutoARIMA` (mismo concepto, mejor mantenimiento y API).
- `sktime` y `mlforecast` — solapan con `skforecast` y `statsforecast` sin aportar diferencial claro para nuestra audiencia. Mencionarlos en una slide de "ecosistema" pero no usarlos en práctica.
- `darts` — solo si el bloque de comparación final lo justifica; si no, queda como referencia.

**Stack final propuesto por sesión (a validar):**

| Sesión | Librerías principales                                       | Específicas                                  |
| ------ | ----------------------------------------------------------- | -------------------------------------------- |
| 1      | `pandas`, `numpy`, `matplotlib`, `statsmodels` (STL/ACF)    | —                                            |
| 2      | `statsforecast` (Auto-ARIMA, Auto-ETS), `prophet`, `pastas` | `statsmodels` (residuos, Ljung-Box)          |
| 3      | `scikit-learn`, `xgboost`, `lightgbm`, `skforecast`         | `shap`                                       |
| 4      | `torch` (LSTM didáctica), `neuralforecast` (TFT/PatchTST)   | `darts` *(opcional para comparación final)*  |

### B. Riesgos / cosas que pueden no caber en 5 h

- Sesión 1: la parte de Pastas puede pasarse a Sesión 2 si la limpieza/STL come tiempo.
- Sesión 3: si la práctica de LSTM no entra, dejarla como demo y trasladar a Sesión 4.
- Sesión 4: el proyecto final puede convertirse en **tarea para casa** si la comparación de modelos se alarga.

### C. Posibles extensiones (fuera de las 20 h)

- Predicción probabilística (conformal, quantile regression).
- Causalidad: Granger, transfer entropy.
- Detección de cambio (changepoint detection) para identificar regímenes hidrológicos.
- Escenarios climáticos (AdapteCCa) como input a los modelos.
