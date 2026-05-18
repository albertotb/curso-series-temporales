# Currículo extendido — Curso de Series Temporales con Python

> Versión detallada del programa resumido en `README.md`. Pensada como guía para preparar slides y notebooks, no como material entregable.
>
> **Duración:** 20 h (4 sesiones × 5 h). Distribución indicativa: ~3 h teoría/ejemplos + ~2 h práctica guiada por sesión.
> **Idioma:** español.
> **Datasets de referencia:**
>
> - Caudal: `A20_GENIL_TOCON` (río Genil — CH Guadalquivir), foco en la crecida de **febrero 2026**.
> - Lluvia: `A20_202` (mismo SAIH).
> - Piezometría: `PZ0267014` (cuenca del Duero) — `COTA PIEZOMÉTRICA`.
> - Meteo: nodo AEMET asociado al pozo.

---

## Sesión 1 — Fundamentos y exploración (5 h = 3 h teoría + 1,5 h práctica + 0,5 h descanso)

**Objetivo.** Que el alumno sepa cargar series hidrometeorológicas reales, explorarlas, limpiarlas y describirlas estadísticamente; y entienda los bloques conceptuales que justifican los modelos posteriores.

### Teoría — 3 h

#### Bloque 1.1 · ¿Qué es una serie temporal? (30 min)

- Definición: $\{y_t\}_{t=1}^{T}$, dependencia temporal.
- Frecuencias típicas en hidro: horaria, diaria, mensual, irregular.
- Diferencias frente a datos i.i.d.: por qué el train/test aleatorio **no** vale.
- Tipos de problemas: descripción, predicción puntual, predicción probabilística, detección de anomalías.
- Caso del curso: predicción de caudal y de cota piezométrica, énfasis en eventos extremos.

#### Bloque 1.2 · Componentes y estacionariedad (1 h)

- Descomposición conceptual: tendencia + estacionalidad + ciclo + ruido (modelos aditivo y multiplicativo).
- Estacionariedad débil vs estricta. Por qué importa.
- Tests: ADF, KPSS (interpretación, no demostración).
- Transformaciones para estacionarizar: diferenciación, logaritmo, Box-Cox.
- **Descomposición STL** (`statsmodels.tsa.seasonal.STL`): robustez frente a outliers, ventana estacional.

#### Bloque 1.3 · Autocorrelación y correlación cruzada (45 min)

- ACF y PACF: definición, lectura visual, intervalos de confianza.
- Cross-correlation (CCF): rezago lluvia → caudal como ejemplo canónico.
- Lag plots y diagramas de dispersión retardada.

#### Bloque 1.4 · Limpieza de datos (45 min)

- **Outliers**: causas físicas (fallos de sensor, derivas) vs eventos reales (crecida). Métodos: z-score robusto (mediana/MAD), Hampel, IQR.
- **Faltantes**: tipos (MCAR, MAR, MNAR aplicado a hidro), métodos sencillos: forward-fill, interpolación lineal, interpolación estacional, imputación con modelo.
- Cuándo **no** rellenar (gaps largos en piezometría).
- Agregación temporal: `resample` (mean/sum/max), reglas distintas para lluvia (suma) y caudal/piezometría (media).

> La teoría de modelos estadísticos clásicos (ARIMA y variantes, ETS, Prophet, Pastas) se imparte al inicio de la Sesión 2 (Bloque 2.1, 1 h 15 min).

### Práctica — 1,5 h · `notebooks/sesion1/`

1. **01_carga_y_exploracion.ipynb** _(30 min)_
   - Cargar `A20_GENIL_TOCON` y `A20_202` desde el CSV/Excel del SAIH.
   - Inspeccionar `pd.DataFrame.info`, rango temporal, gaps, frecuencia real vs nominal.
   - Plots básicos: serie completa, año 2026, ventana de crecida.
2. **02_limpieza.ipynb** _(30 min)_
   - Detectar outliers en caudal (z-score robusto) y discutir si conservarlos.
   - Rellenar faltantes cortos en lluvia (interpolación) y dejar gaps largos en piezometría.
   - Resamplear a diario y mensual; comprobar diferencias caudal vs lluvia.
3. **03_descomposicion_y_correlacion.ipynb** _(30 min)_
   - STL de la serie de caudal y de cota piezométrica.
   - ACF/PACF de caudal y residuos de STL.
   - CCF lluvia ↔ caudal: identificar rezago dominante.

---

## Sesión 2 — Modelos estadísticos en profundidad y Pastas (5 h = 1 h 15 min teoría + 3 h 15 min práctica + 0,5 h descanso)

**Objetivo.** Que el alumno entienda los modelos estadísticos clásicos (ARIMA y variantes, ETS, Prophet, Pastas), los ajuste y diagnostique sobre series hidrométricas reales, y compare sus predicciones. La sesión arranca con un bloque teórico denso de ARIMA y variantes; los notebooks aplican.

### Teoría — 1 h 15 min

#### Bloque 2.1 · Modelos estadísticos clásicos (1 h 15 min)

- **AR(p), MA(q), ARMA(p,q):** procesos estacionarios, intuición y formulación.
- **ARIMA(p,d,q):** integración por diferenciación; cómo elegir `d`.
- **SARIMA(p,d,q)(P,D,Q,s):** estacionalidad multiplicativa; cuándo hace falta.
- **SARIMAX:** covariables exógenas (lluvia → caudal).
- **Metodología Box–Jenkins:** identificación con ACF/PACF, estimación, diagnóstico de residuos (Ljung-Box, normalidad, heterocedasticidad).
- Criterios de selección: AIC, BIC, AICc. `auto_arima` por dentro.
- **Suavizado exponencial (ETS):** simple, Holt, Holt-Winters; descomposición Error/Trend/Seasonal; cuándo elegir ETS sobre ARIMA.
- **Prophet:** modelo aditivo (tendencia por tramos + estacionalidad Fourier + holidays); cuándo gana frente a ARIMA.
- **Pastas (introducción conceptual):** filosofía de respuesta a impulsos para piezometría — se profundiza en el notebook correspondiente.

### Práctica — 3 h 15 min · `notebooks/sesion2/`

#### 1. **01_arima_ets_caudal.ipynb** _(1 h)_

- SARIMAX sobre caudal diario del Genil con `statsmodels`.
- Ajuste manual vs automático; estacionalidad anual.
- Diagnóstico de residuos (Ljung-Box, normalidad).
- Forecast 30 días con bandas de confianza; superponer con la crecida real de febrero 2026.
- ETS sobre la misma serie; comparación rápida ARIMA vs ETS.

#### 2. **02_prophet_baseline.ipynb** _(30 min)_

- Ajuste de Prophet sobre caudal con `extra_regressors` (lluvia).
- Componentes (trend, yearly, weekly).
- Comparación con ARIMA y ETS del notebook anterior.

#### 3. **03_pastas_piezometria.ipynb** _(1 h 15 min)_

> Mini-intro (15 min): filosofía de respuesta a impulsos (estímulos → nivel); `StressModel`/`RechargeModel`/modelos de bombeo; calibración e intervalos de confianza.

- Modelo Pastas para `PZ0267014` con lluvia (AEMET) como input.
- Añadir un `StressModel` ficticio de extracciones para discutir.
- Visualizar contribuciones individuales (lluvia vs bombeo).
- Limitaciones: linealidad, estacionariedad de la respuesta.

#### 4. **04_validacion_y_comparacion.ipynb** _(30 min)_

> Mini-intro (10 min): split temporal (train/val/test no aleatorio); walk-forward / expanding window; métricas hidrológicas (NSE, KGE, error en pico); Diebold-Mariano (mención).

- Walk-forward sobre la serie de caudal.
- Tabla comparativa final: SARIMAX vs ETS vs Prophet con RMSE, MAE, NSE, KGE y error en pico (foco en crecida feb 2026).

---

## Sesión 3 — Machine Learning clásico, evaluación y splits temporales (5 h = 3 h teoría + 1,5 h práctica + 0,5 h descanso)

**Objetivo.** Que el alumno entienda cómo se reformula una serie temporal como problema supervisado, aplique modelos clásicos de ML (RF, XGBoost, LightGBM) con `skforecast`, y domine los splits temporales y métricas hidrológicas. La parte de redes neuronales/DL se cubre en la Sesión 4.

### Bloque 3.1 · De serie temporal a problema supervisado (45 min)

- Sliding window: variables retardadas como features.
- Feature engineering específica para series:
  - Lags y diferencias.
  - Estadísticos móviles (rolling mean/std/min/max).
  - Variables de calendario (dayofyear, mes, día de la semana).
  - Variables de Fourier para estacionalidad continua.
  - Variables exógenas: lluvia agregada en ventanas, índices climáticos.
- Pitfall clásico: **fuga de información** (rolling windows que ven el futuro, escaladores ajustados con test).

### Bloque 3.2 · Modelos clásicos de ML (45 min)

- Regresión lineal regularizada (Ridge, Lasso) como baseline serio.
- Árboles y ensembles: Random Forest.
- Gradient Boosting: XGBoost, LightGBM (cuál preferir y por qué).
- Interpretabilidad: importancia de variables, SHAP (vista rápida).
- Wrappers para forecasting: `skforecast` (recursive, direct, DirRec) — docs en español.

### Bloque 3.3 · Estrategias de predicción multi-paso (30 min)

- Recursive (autoregresiva), Direct (un modelo por horizonte), DirRec, MIMO.
- Trade-offs: precisión vs acumulación de error vs coste de entrenamiento.

### Bloque 3.4 · Splits temporales y validación cruzada (30 min)

- Split simple train/val/test (no aleatorio, respetando el orden).
- Walk-forward / expanding window.
- `sklearn.model_selection.TimeSeriesSplit`, blocked CV.
- Backtesting en `skforecast`.

### Bloque 3.5 · Métricas y evaluación en hidrología (30 min)

- MAE, RMSE, MAPE, sMAPE: ventajas y trampas.
- Métricas hidrológicas: NSE, KGE, PBIAS, error en pico, percentil 95.
- Evaluación específica de **eventos extremos**: crecida y sequía.
- Predicción probabilística (mención): cuantiles, conformal prediction.

### Práctica — 1,5 h · `notebooks/sesion3/`

1. **01_features_y_baseline.ipynb** _(30 min)_
   - Construir matriz de features (lags + rolling + calendario + lluvia retardada) para caudal del Genil.
   - Baseline persistencia y baseline regresión lineal con `skforecast`.
2. **02_rf_y_xgboost.ipynb** _(45 min)_
   - Random Forest y XGBoost vía `skforecast`.
   - Feature importance y SHAP.
   - Comparación con ARIMA/Prophet de la Sesión 2.
3. **03_backtesting_y_metricas.ipynb** _(15 min)_
   - Walk-forward / expanding window con `skforecast.backtesting`.
   - Métricas hidrológicas (NSE, KGE, error en pico) sobre la crecida de febrero 2026.

---

## Sesión 4 — Deep Learning y proyecto final (5 h = 1 h teoría + 2 h práctica + 1 h 30 min proyecto + 0,5 h descanso)

**Objetivo.** Que el alumno construya su primera LSTM/GRU sobre datos hidrológicos reales con `tensorflow`/`keras`, entienda los pitfalls del DL aplicado a series, y cierre el curso con un proyecto final que compare modelos estadísticos vs ML vs DL. Sesión de formato **mixto teoría-código en vivo**: el instructor explica concepto y muestra código, los alumnos reproducen en su Jupyter a la par. La separación teoría / práctica es estructural; en sala se intercalan.

### Teoría — 1 h

#### Bloque 4.1 · Redes neuronales para series temporales (1 h 15 min)

- MLP con features de lag: cuándo ya basta.
- **RNN**: idea de estado oculto, problema de gradientes.
- **LSTM**: gates (input, forget, output), arquitectura típica, intuición de la "memoria larga".
- **GRU**: simplificación con menos gates; cuándo prefiere uno u otro.
- 1D-CNN y **TCN** (causal dilated convolutions): mención y comparación con LSTM.
- **Transformers** para series (mención): atención, Informer/Autoformer/PatchTST.

### Práctica — 1 h 45 min· `notebooks/sesion4/`

1. **01_lstm_caudal_keras.ipynb** _(1 h)_

   > Mini-intro (15 min): pipeline DL en Keras — `keras.utils.timeseries_dataset_from_array`, normalización por train, ventanas no solapadas en test, callbacks (`EarlyStopping`, `ReduceLROnPlateau`), regularización (dropout, weight decay).
   - LSTM/GRU multi-paso para caudal del Genil con `tensorflow` + `keras`.
   - Preparación de ventanas (B, T, F) y normalización.
   - Modelo `Sequential` y entrenamiento con `model.fit()` + callbacks.
   - Visualización: predicción vs observado, residuos por horizonte.

2. **02_comparacion_y_neuralhydrology.ipynb** _(30 min)_

   > Mini-intro (10 min): comparación honesta — mismo split, mismas métricas (recap de S3), múltiples semillas en DL (medias y desviaciones).
   - Tabla comparativa ARIMA/Prophet (S2) vs RF/XGBoost (S3) vs LSTM (S4) con mismo split y mismas métricas (RMSE, NSE, KGE, error en pico).
   - Discusión: ¿en qué casos gana DL? ¿en qué casos ARIMA/RF basta?
   - Demo de [NeuralHydrology](https://neuralhydrology.readthedocs.io/) con archivo YAML sobre CAMELS-ES — referente del DL hidrológico moderno (Kratzert et al., JKU Linz). Sin pedir al alumno que lo reproduzca.

3. **03_interpretabilidad_y_errores.ipynb** _(15 min)_

   > Mini-intro (5 min): SHAP recap rápido desde S3 aplicado al LSTM (limitaciones).
   - SHAP en los modelos de árbol (revisión desde S3).
   - Análisis de errores por régimen: estiaje vs crecida.
   - Foco en la **crecida de febrero 2026** y en la **bajada de cota** por extracciones en piezometría.

### Proyecto final — 1 h 30 min · `notebooks/sesion4/proyecto_final/`

Cada alumno (o equipo) construye un pipeline completo sobre uno de los dos datasets:

- **A.** Caudal del Genil — predicción a 7 días con foco en la crecida.
- **B.** Cota piezométrica `PZ0267014` — predicción a 1 mes con foco en bajadas por extracción.

**Entregable:** notebook reproducible + breve reporte de comparación (estadísticos vs ML vs DL) con métricas hidrológicas. Si no da tiempo a terminar, el alumno lo cierra en casa.

> El instructor acompaña: resuelve dudas, da pistas. La plantilla `proyecto_final/` ya tiene el esqueleto (carga, splits, métricas) — el alumno aporta su elección de modelos y la interpretación.

---

## Apéndices

### A. Librerías por sesión

#### A.1 Catálogo de librerías candidatas

Listado completo de las librerías consideradas para el curso (núcleo + alternativas). La elección final se hace en A.3 tras la comparación de A.2.

| Librería                                                                                      | Tipo                                          | Encaje natural en el curso                                                                                                                                                                 |
| --------------------------------------------------------------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [`pandas`](https://pandas.pydata.org/)                                                        | Manipulación de datos tabulares y temporales  | **Sesiones 1–4** (transversal): índices temporales, resampling, joins. Base de todo el curso.                                                                                              |
| [`numpy`](https://numpy.org/)                                                                 | Arrays y álgebra numérica                     | **Sesiones 1–4** (transversal): dependencia implícita del resto del stack.                                                                                                                 |
| [`matplotlib`](https://matplotlib.org/)                                                       | Visualización estática                        | **Sesiones 1–4** (transversal): plots de series, ACF/PACF, descomposición, comparativas de modelos.                                                                                        |
| [`statsmodels`](https://www.statsmodels.org/)                                                 | Estadística y modelado clásico                | **Sesión 1** (STL, ACF/PACF, tests ADF/KPSS/Ljung-Box) y **Sesión 2** (ARIMA, SARIMA, SARIMAX, ETS).                                                                                       |
| [`pmdarima`](https://alkaline-ml.com/pmdarima/)                                               | Wrapper de `statsmodels` con `auto_arima`     | **Sesión 2** (opcional): mención breve para selección automática de órdenes ARIMA si `statsmodels` lo requiere a mano.                                                                     |
| [`prophet`](https://facebook.github.io/prophet/)                                              | Modelo aditivo bayesiano                      | **Sesión 2** como alternativa/baseline a ARIMA y ETS — encaja por estacionalidad anual fuerte (caudal, piezometría) y por tolerar faltantes/outliers.                                      |
| [`pastas`](https://pastas.readthedocs.io/)                                                    | Respuesta a impulsos para piezometría         | **Sesión 2** (núcleo): único framework maduro para modelar piezometría con `StressModel`/`RechargeModel`.                                                                                  |
| [`scikit-learn`](https://scikit-learn.org/)                                                   | ML clásico de propósito general               | **Sesión 3** (núcleo): regresión, RF, splits, métricas, `TimeSeriesSplit`.                                                                                                                 |
| [`xgboost`](https://xgboost.readthedocs.io/) / [`lightgbm`](https://lightgbm.readthedocs.io/) | Gradient Boosting                             | **Sesión 3**: modelos tree-boosting punteros sobre las features de lag/rolling.                                                                                                            |
| [`shap`](https://shap.readthedocs.io/)                                                        | Interpretabilidad de modelos                  | **Sesión 3**: importancia de variables y explicaciones locales para los modelos tree-based.                                                                                                |
| [`skforecast`](https://skforecast.org/)                                                       | Wrapper sobre `scikit-learn` para forecasting | **Sesión 3** — puente natural entre ML clásico y forecasting: convierte RF/XGBoost/LightGBM en forecasters recursivos/directos. Docs en español.                                           |
| [`sktime`](https://www.sktime.net/)                                                           | Marco unificado tipo `scikit-learn`           | **Sesión 3** (alternativa a `skforecast`) — API homogénea para forecasting, clasificación y CV temporal.                                                                                   |
| [`statsforecast`](https://nixtlaverse.nixtla.io/statsforecast/) (Nixtla)                      | Clásicos rápidos en `numba`                   | **Sesión 2** (alternativa a `statsmodels` + `pmdarima`) — AutoARIMA/ETS/TBATS muy rápidos, misma API que el resto de la suite Nixtla.                                                      |
| [`mlforecast`](https://nixtlaverse.nixtla.io/mlforecast/) (Nixtla)                            | ML "global" con features automáticas          | **Sesión 3** — feature engineering automático (lags, rolling, fechas) + cualquier modelo sklearn. Útil si predecimos varias estaciones a la vez.                                           |
| [`tensorflow`](https://www.tensorflow.org/) + [`keras`](https://keras.io/)                    | Deep learning framework                       | **Sesión 4** (núcleo): LSTM/GRU con API de alto nivel (`keras.Sequential`). Tutoriales oficiales de TS (weather forecasting) y abundante material en español.                              |
| [`torch`](https://pytorch.org/) + [`pytorch-lightning`](https://lightning.ai/)                | Deep learning framework alternativo           | **Sesión 4** (alternativa a TF/Keras) — estándar en research de hidrología (NeuralHydrology, Kratzert et al.), más boilerplate, menos tutoriales TS oficiales.                             |
| [`neuralforecast`](https://nixtlaverse.nixtla.io/neuralforecast/) (Nixtla)                    | DL (PyTorch) con API uniforme                 | **Sesión 4** — NBEATS, NHITS, TFT, PatchTST, iTransformer bajo API uniforme. Alternativa a escribir LSTM "a mano" en PyTorch.                                                              |
| [`tsai`](https://timeseriesai.github.io/tsai/)                                                | DL (PyTorch + fastai) de alto nivel           | **Sesión 4** — colección de modelos SOTA para series (InceptionTime, ROCKET, MiniRocket, TST, PatchTST, TSiT, XCM) con API estilo fastai. Mantenedor hispanohablante (Ignacio Oguiza).     |
| [`neuralhydrology`](https://neuralhydrology.readthedocs.io/)                                  | DL (PyTorch) específico para hidrología       | **Sesión 4** — librería de referencia del DL hidrológico (Kratzert et al., JKU Linz). LSTM/EA-LSTM/MTS-LSTM para rainfall-runoff con CAMELS. Configuración por YAML, sin código de modelo. |
| [`darts`](https://unit8co.github.io/darts/)                                                   | "Todo en uno" (stats + ML + DL + foundation)  | **Transversal** — su valor pedagógico está en comparar familias de modelos con el mismo código. Podría usarse en Sesión 4 para la comparación final.                                       |

#### A.2 Comparación lado a lado

Datos de GitHub a fecha **2026-05-13**. Funcionalidades verificadas en la documentación de cada librería.

| Criterio                              | `statsmodels` + `pmdarima`     | `statsforecast`          | `prophet`          | `skforecast`                  | `sktime`                         | `mlforecast`            | `neuralforecast`               | `darts`                           |
| ------------------------------------- | ------------------------------ | ------------------------ | ------------------ | ----------------------------- | -------------------------------- | ----------------------- | ------------------------------ | --------------------------------- |
| Cubre clásicos (ARIMA/ETS)            | Sí (núcleo)                    | Sí (Auto\*, TBATS)       | Sí (modelo propio) | No (integra `statsmodels`)    | Sí (incluye Auto-ARIMA)          | No                      | No                             | Sí (ARIMA, ETS, Theta)            |
| Cubre ML (XGBoost/LightGBM)           | No                             | No                       | No                 | Sí (núcleo)                   | Sí (vía `make_reduction`)        | Sí (núcleo)             | No                             | Sí (`RegressionModel`)            |
| Cubre DL (LSTM/TFT/PatchTST)          | No                             | No                       | No                 | Parcial (`ForecasterRnn`)     | Parcial (wraps neuralforecast)   | No                      | Sí (núcleo: TFT/PatchTST/iTr)  | Sí (RNN/TFT/N-BEATS/TiDE)         |
| Multi-paso recursivo y directo        | Recursivo                      | Recursivo + directo      | Directo (fechas)   | Recursivo + Directo + DirRec  | Recursivo + Directo + MIMO       | Recursivo + Directo     | Directo (multi-output)         | Recursivo + Directo               |
| Covariables exógenas (lluvia)         | Sí (SARIMAX)                   | Sí                       | Sí (regressors)    | Sí (`exog`)                   | Sí (`X` en fit/predict)          | Sí                      | Sí (futr/hist/stat exog)       | Sí (past/future/static, muy rico) |
| Intervalos / probabilístico           | Sí (paramétricos)              | Sí (param + conformal)   | Sí (MCMC)          | Sí (bootstrap, conformal)     | Sí (interval framework)          | Sí (conformal)          | Sí (quantile, distribucional)  | Sí (probabilístico nativo)        |
| CV temporal (walk-forward)            | Manual                         | Sí (`cross_validation`)  | Sí (helper)        | Sí (backtesting muy completo) | Sí (Sliding/Expanding splitters) | Sí (`cross_validation`) | Sí (`cross_validation`)        | Sí (`historical_forecasts`)       |
| Documentación / tutoriales en español | No oficial (apuntes UC3M, UCM) | Parcial (equipo hispano) | No oficial         | **Sí (cienciadedatos.net)**   | No                               | Parcial                 | Parcial                        | No                                |
| Curva de aprendizaje                  | Media-alta                     | Baja                     | Muy baja           | Baja-media (API sklearn-like) | Media-alta                       | Media                   | Media-alta                     | Media                             |
| Mantenimiento (2024-2026)             | Activo                         | Muy activo               | Activo (Meta)      | Muy activo                    | Muy activo                       | Muy activo              | Muy activo                     | Muy activo                        |
| Encaje hidrológico (casos publicados) | Sí (estándar)                  | Parcial (lib reciente)   | Sí (varios papers) | Parcial (algún caso en docs)  | Parcial (más industrial)         | No documentado          | Sí (análogo a NeuralHydrology) | Sí (varios papers)                |
| **GitHub stars**                      | 11.4k / 1.7k                   | 4.8k                     | 20.2k              | 1.5k                          | 9.8k                             | 1.2k                    | 4.1k                           | 9.4k                              |
| **Contribuidores**                    | 484 / 24                       | 62                       | 191                | 29                            | 573                              | 24                      | 62                             | 156                               |
| **Última release**                    | 2025-12 / 2025-11              | 2025-10                  | 2026-01            | 2026-04                       | 2025-11                          | 2026-03                 | 2026-05                        | 2026-05                           |
| **Cadencia de releases**              | ~2-3 / año                     | ~trimestral              | ~semestral         | mensual                       | mensual                          | mensual+                | mensual+                       | mensual                           |
| **Licencia**                          | BSD-3 / MIT                    | Apache-2.0               | MIT                | BSD-3                         | BSD-3                            | Apache-2.0              | Apache-2.0                     | Apache-2.0                        |

#### A.3 Conclusiones y recomendación

**Lectura rápida de la tabla:**

- **Más populares (stars):** `prophet` (20.2k) > `statsmodels` (11.4k) > `sktime` (9.8k) ≈ `darts` (9.4k) > `statsforecast` (4.8k) > `neuralforecast` (4.1k). Pero stars ≠ idoneidad pedagógica.
- **Mejor mantenimiento:** la suite Nixtla (`statsforecast` / `mlforecast` / `neuralforecast`), `skforecast`, `sktime` y `darts` publican mensualmente. `statsmodels` y `prophet` van más lentos pero son estables.
- **Comunidad más grande (contribuidores):** `sktime` (573) y `statsmodels` (484). Las demás tienen equipos pequeños pero activos.
- **Única con docs nativas en español:** `skforecast` (Joaquín Amat / cienciadedatos.net). Diferencial fuerte para nuestra audiencia.
- **Más completas en un solo paquete:** `darts` y `sktime` cubren clásicos + ML + DL; el resto son especializadas.

**Propuesta de subconjunto mínimo (a validar):**

| Rol                                 | Librería elegida                      | Justificación                                                                                                                                                                                                |
| ----------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Manipulación, EDA, descomposición   | `pandas` + `statsmodels`              | Estándar de facto; STL y ACF/PACF están en `statsmodels`.                                                                                                                                                    |
| Clásicos (ARIMA/ETS) — Sesión 2     | `statsmodels`                         | Ya está en Sesión 1 para STL/ACF/PACF/tests; reutilizarla para ARIMA/ETS evita introducir una API más. Es el estándar de facto (11.4k stars, 484 contribuidores, 15 años).                                   |
| Modelo de respuesta a impulsos      | `pastas`                              | Sin alternativa real para piezometría.                                                                                                                                                                       |
| Baseline alternativo                | `prophet`                             | Bloque corto en Sesión 2: estacionalidad + holidays/extracciones + outliers. Muy poco coste de enseñanza.                                                                                                    |
| ML (RF/XGBoost/LightGBM) — Sesión 3 | `skforecast`                          | Docs en español, API sklearn-like, backtesting muy completo. Encaja con el perfil del alumno y con el idioma del curso.                                                                                      |
| Interpretabilidad                   | `shap`                                | Como ya estaba.                                                                                                                                                                                              |
| DL (LSTM) — Sesión 4                | `tensorflow` + `keras`                | API de alto nivel (LSTM en ~10 líneas), tutoriales oficiales de TS (`tf` weather forecasting) y abundante material didáctico en español. Sin coste cognitivo extra de un wrapper.                            |
| Demo / referencia hidrológica       | `neuralhydrology` _(demo, no código)_ | Se muestra como referencia "así se hace en research" (Kratzert et al.) y se corre un experimento mediante archivos YAML. No se enseña a programar con ella — toda la configuración va en YAML, no en Python. |

**Descartar (por ahora):**

- `statsforecast` — solapa con `statsmodels` justo donde más importa (ARIMA/ETS) y obligaría a introducir una API más en Sesión 2. `statsmodels` ya está en Sesión 1 para STL/ACF/tests y es el estándar Python (11.4k stars vs 4.8k).
- `pmdarima` — `statsmodels` cubre ARIMA/SARIMA; si necesitamos `auto_arima` se puede mencionar `pmdarima` brevemente, pero no usarlo como librería vertebral.
- `sktime` y `mlforecast` — solapan con `skforecast` sin aportar diferencial claro para nuestra audiencia. Mencionarlos en una slide de "ecosistema" pero no usarlos en práctica.
- `torch` / `pytorch-lightning` — descartados a favor de `tensorflow`/`keras`: Keras tiene API de alto nivel para LSTM en ~10 líneas, tutorial oficial de TS (`tf` weather forecasting), decenas de tutoriales Machine Learning Mastery y abundante material en español (Codificando Bits, Aprende ML). Lightning sigue requiriendo `LightningModule` con `training_step`/`validation_step` — más boilerplate del que cabe en 1,5 h de clase. PyTorch domina la literatura de DL hidrológico pero nuestra audiencia no necesita leer papers, sino entrenar una LSTM.
- `neuralforecast` — sin la suite Nixtla en el resto del curso, no compensa introducir una API nueva solo para Sesión 4. Además es PyTorch-based; si elegimos TF/Keras, no encaja.
- `tsai` — modelos SOTA (PatchTST, TSiT, InceptionTime…). Fuera del scope del curso, que cubre modelos "true and tested" (LSTM, GRU, baseline DL).
- `neuralhydrology` — librería **muy relevante temáticamente** (Kratzert et al., el referente del DL hidrológico moderno), pero **mala como herramienta didáctica**: toda la configuración va en archivos YAML, no en código Python. El alumno no escribe modelos ni training loops, solo edita YAML. Útil como **demo/referencia** ("así se hace en research") y como punto de partida para quien quiera ir más allá del curso, pero no como librería de práctica.
- `darts` — solo si el bloque de comparación final lo justifica; si no, queda como referencia. Además es PyTorch-based, lo que choca con la elección TF/Keras.

**Stack final propuesto por sesión:**

| Sesión | Librerías                                                   |
| ------ | ----------------------------------------------------------- |
| 1      | `pandas`, `numpy`, `matplotlib`, `statsmodels` (STL/ACF)    |
| 2      | `statsmodels` (ARIMA/ETS + residuos), `prophet`, `pastas`   |
| 3      | `scikit-learn`, `xgboost`, `lightgbm`, `skforecast`, `shap` |
| 4      | `tensorflow` + `keras` (LSTM/GRU)                           |
