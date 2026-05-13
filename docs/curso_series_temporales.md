# Curso de Series Temporales con Python (Hidrología e Hidrogeología)

## Información general

- **Duración:** 20 h (4 sesiones × 5 h)
- **Estructura por sesión:** 4 h 30 min de contenido (teoría + práctica) + 30 min de descanso
- **Enfoque:** aplicado a series temporales hidrometeorológicas (caudales y piezometría)
- **Objetivo:** cubrir el _workflow_ completo en Python — descarga/carga de datos, preprocesamiento, modelado estadístico, machine learning y deep learning, evaluación — aplicado a series hidrometeorológicas reales y a la predicción de eventos extremos.

## Preparación previa

### Requisitos

Python ≥ 3.12 con las siguientes librerías instaladas:

- **Manipulación y visualización:** `pandas`, `numpy`, `scipy`, `matplotlib`, `seaborn`, `plotly`, `openpyxl`.
- **Series temporales clásicas:** `statsmodels`, `pastas`, `prophet`.
- **Machine learning:** `scikit-learn`, `xgboost`, `lightgbm`, `skforecast`, `shap`.
- **Deep learning:** `tensorflow`, `keras`.
- **Notebook:** `jupyterlab`, `ipykernel`, `ipywidgets`.

## Programa por sesiones

### Sesión 1 — Fundamentos y exploración

Teoría ~3h / práctica ~1h 30min

#### Bloque 1.1 · ¿Qué es una serie temporal?

- Definición y dependencia temporal.
- Frecuencias típicas en hidro: horaria, diaria, mensual, irregular.
- Diferencias frente a datos i.i.d.
- Tipos de problemas: descripción, predicción puntual, predicción probabilística, detección de anomalías.

#### Bloque 1.2 · Componentes y estacionariedad

- Descomposición conceptual: tendencia + estacionalidad + ciclo + ruido (modelos aditivo y multiplicativo).
- Estacionariedad débil vs estricta. Por qué importa.
- Tests: ADF, KPSS.
- Transformaciones para estacionarizar: diferenciación, logaritmo, Box-Cox.
- Descomposición STL.

#### Bloque 1.3 · Autocorrelación y correlación cruzada

- ACF y PACF: definición, lectura visual, intervalos de confianza.
- Cross-correlation (CCF): rezago lluvia → caudal como ejemplo canónico.
- Lag plots y diagramas de dispersión retardada.

#### Bloque 1.4 · Limpieza de datos

- Outliers: causas físicas (fallos de sensor, derivas) vs eventos reales (crecida). Métodos: z-score robusto, Hampel, IQR.
- Faltantes: tipos (MCAR, MAR, MNAR aplicado a hidro), métodos sencillos (forward-fill, interpolación, imputación con modelo).
- Agregación temporal.

### Sesión 2 — Modelos estadísticos y Pastas

Teoría ~1h 15min / práctica ~3h 15min

#### Bloque 2.1 · Modelos estadísticos clásicos

- **AR(p), MA(q), ARMA(p,q):** procesos estacionarios, intuición y formulación.
- **ARIMA(p,d,q):** integración por diferenciación; cómo elegir `d`.
- **SARIMA(p,d,q)(P,D,Q,s):** estacionalidad multiplicativa; cuándo hace falta.
- **SARIMAX:** covariables exógenas (lluvia → caudal).
- **Metodología Box–Jenkins:** identificación con ACF/PACF, estimación, diagnóstico de residuos (Ljung-Box, normalidad, heterocedasticidad).
- Criterios de selección: AIC, BIC, AICc. `auto_arima` por dentro.
- **Suavizado exponencial (ETS):** simple, Holt, Holt-Winters; cuándo elegir ETS sobre ARIMA.
- **Prophet:** modelo aditivo (tendencia por tramos + estacionalidad Fourier + holidays).
- **Pastas (introducción conceptual):** filosofía de respuesta a impulsos para piezometría.

### Sesión 3 — Machine Learning clásico, evaluación y splits temporales

Teoría ~3h / práctica ~1h 30min

#### Bloque 3.1 · De serie temporal a problema supervisado

- Sliding window: variables retardadas como features.
- Feature engineering específica para series: lags y diferencias, estadísticos móviles (rolling), variables de calendario, variables de Fourier para estacionalidad, variables exógenas.

#### Bloque 3.2 · Modelos clásicos de ML

- Regresión lineal regularizada (Ridge, Lasso) como baseline serio.
- Árboles y ensembles: Random Forest.
- Gradient Boosting: XGBoost, LightGBM.
- Interpretabilidad: importancia de variables, SHAP.

#### Bloque 3.3 · Estrategias de predicción multi-paso

- Recursive (autoregresiva), Direct (un modelo por horizonte), DirRec, MIMO.
- Trade-offs: precisión vs acumulación de error vs coste de entrenamiento.

#### Bloque 3.4 · Splits temporales y validación cruzada

- Split simple train/val/test respetando el orden.
- Walk-forward / expanding window.
- `sklearn.model_selection.TimeSeriesSplit`, blocked CV.
- Backtesting.

#### Bloque 3.5 · Métricas y evaluación en hidrología

- MAE, RMSE, MAPE, sMAPE: ventajas y trampas.
- Métricas hidrológicas: NSE, KGE, PBIAS, error en pico, percentil 95.
- Evaluación específica de **eventos extremos**: crecida y sequía.

### Sesión 4 — Deep Learning con demos y proyecto final

Teoría ~1h 15min / práctica ~3h 15min

#### Bloque 4.1 · Redes neuronales para series temporales

- MLP con features de lag.
- **RNN**: idea de estado oculto, problema de gradientes.
- **LSTM**: gates (input, forget, output), arquitectura típica, intuición de la "memoria larga".
- **GRU**: simplificación con menos gates; cuándo prefiere uno u otro.
- 1D-CNN y **TCN** (causal dilated convolutions): mención y comparación con LSTM.
- **Transformers** para series (mención): atención, Informer/Autoformer/PatchTST.

## Fuentes de datos

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
