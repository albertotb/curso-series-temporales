# Investigación de cursos y materiales similares

## 1. Plataformas MOOC / cursos online

### Coursera

#### [Sequences, Time Series and Prediction (DeepLearning.AI / TensorFlow in Practice)](https://www.coursera.org/learn/tensorflow-sequences-time-series-and-prediction)

- **Proveedor:** DeepLearning.AI — Laurence Moroney (parte del TensorFlow Developer Professional Certificate)
- **Duración:** ~20 horas (4 semanas, 5 h/semana)
- **Idioma:** inglés (subtítulos en 25 idiomas)
- **Coste:** gratis para auditar; certificado requiere suscripción
- **Python:** sí (TensorFlow / Keras)
- **Contenido principal:**
  - Semana 1: secuencias, particiones train/val/test, métricas, medias móviles y diferenciación
  - Semana 2: preparación de features (ventanas deslizantes), DNN para series
  - Semana 3: RNN, LSTM, ajuste dinámico del learning rate
  - Semana 4: CNN 1D, LSTMs bidireccionales, predicción de manchas solares (sunspots)
- **Notas:** referencia obligada en DL para series temporales. Solo DL, no cubre ARIMA/Prophet. Útil para inspirar la parte de redes profundas. Duración encaja casi exactamente con 20 h.

#### [Practical Time Series Analysis (SUNY)](https://www.coursera.org/learn/practical-time-series-analysis)

- **Proveedor:** The State University of New York — Tural Sadigov, William Thistleton
- **Duración:** ~26 horas
- **Idioma:** inglés (subtítulos en 22 idiomas)
- **Coste:** gratis para auditar; certificado de pago
- **Python:** no (código en R)
- **Contenido principal:**
  - Estadística básica y regresión lineal
  - Visualización de series, ACF, MA(q)
  - Estacionariedad, backward shift, AR(p), Yule-Walker
  - PACF, ajuste de modelos, AIC, ARMA, ARIMA
  - Estacionalidad, SARIMA, suavizado exponencial, forecasting
- **Notas:** rigor matemático alto. Usa rainfall y sunspots como datasets, relevante temáticamente, pero el código es R.

#### [Time Series Mastery: Forecasting with ETS, ARIMA, Python (Starweaver)](https://www.coursera.org/learn/time-series-mastery-forecasting-with-ets-arima-python)

- **Proveedor:** Starweaver — Diogo Resende
- **Duración:** ~2 horas
- **Idioma:** inglés (5 idiomas)
- **Coste:** gratis para auditar
- **Python:** sí
- **Contenido principal:** introducción, ETS y descomposición estacional, ARIMA/SARIMA/SARIMAX, evaluación
- **Notas:** muy compacto. Sirve como referencia minimalista de "pipeline ETS+ARIMA en Python".

#### [A Practical Approach to Timeseries Forecasting Using Python (Packt)](https://www.coursera.org/learn/packt-a-practical-approach-to-timeseries-forecasting-using-python-kd3kj)

- **Proveedor:** Packt
- **Duración:** ~20 horas (2 semanas a 10 h)
- **Idioma:** inglés (3 idiomas)
- **Coste:** Coursera Plus / compra individual
- **Python:** sí
- **Contenido principal:** fundamentos; manipulación, visualización; estacionariedad, descomposición, denoising; ARIMA/SARIMA; RNN (LSTM, BiLSTM, GRU); proyectos COVID-19, MSFT, natalidad
- **Notas:** la mejor coincidencia "estadístico + DL" en Coursera. Estructura tipo bootcamp — útil como referencia de plan de 20 h.

#### [Time Series Forecasting with Facebook Prophet in Python (Packt)](https://www.coursera.org/learn/packt-time-series-forecasting-with-facebook-prophet-in-python-7sw5w)

- **Proveedor:** Packt
- **Duración:** ~4 horas
- **Idioma:** inglés
- **Python:** sí
- **Contenido:** métricas y baselines (naive, walk-forward), Prophet, holidays, regresores exógenos, CV, changepoints, estacionalidad multiplicativa, outliers
- **Notas:** útil si dedicamos un bloque a Prophet (muy adecuado para series hidrológicas con estacionalidad anual y eventos).

#### [Demand Forecasting Using Time Series (LearnQuest)](https://www.coursera.org/learn/demand-prediction-using-time-series)

- **Proveedor:** LearnQuest (Machine Learning for Supply Chains Specialization)
- **Duración:** ~9 horas
- **Idioma:** **doblado al español** (AI Dubbing); 21 idiomas
- **Coste:** gratis para auditar
- **Python:** sí
- **Contenido:** estacionariedad/tendencia/ciclicidad/estacionalidad; datetime y plots con Pandas; ACF/PACF; regresión lineal y con lags, AR, ARIMA; proyecto final ARIMA
- **Notas:** uno de los pocos en Coursera disponible doblado al **español**. Pedagogía "introducción → ARIMA" en ~9 h.

#### [Specialized Models: Time Series and Survival Analysis (IBM)](https://www.coursera.org/learn/time-series-survival-analysis)

- **Proveedor:** IBM — Mark J Grover, Miguel Maldonado
- **Duración:** ~12 horas
- **Idioma:** inglés
- **Python:** sí
- **Contenido:** descomposición, estacionariedad, suavizado, ARMA/ARIMA/SARIMA, DL para forecasting + análisis de supervivencia
- **Notas:** parte de IBM Machine Learning Professional Certificate. Cubre DL pero la parte de survival no es relevante para hidrología.

#### [Python: Apply & Evaluate Sales Forecasting with Time Series (EDUCBA)](https://www.coursera.org/learn/python-apply-evaluate-sales-forecasting-time-series)

- **Proveedor:** EDUCBA
- **Duración:** ~5 horas
- **Idioma:** inglés
- **Python:** sí
- **Contenido:** preprocesado, feature engineering, descomposición, SARIMA, Prophet, comparación de modelos
- **Notas:** muy business-y, pero buen ejemplo de pipeline corto.

#### [Modelos predictivos con aprendizaje automático — Universidad de los Andes](https://www.coursera.org/learn/modelos-predictivos-con-aprendizaje-automatico)

- **Idioma:** **español**
- **Notas:** incluye módulo de series de tiempo y predicción con ML.

#### [Modelos predictivos con Machine Learning — Universidad Anáhuac](https://www.coursera.org/learn/modelos-predictivos-con-machine-learning)

- **Idioma:** **español**
- **Notas:** implementación de modelos predictivos con Python.

#### [Predicción de Ventas Pronosticando Tendencias (Coursera, project)](https://www.coursera.org/projects/prediccion-de-ventas-pronosticando-tendencias-en-google-sheets)

- **Idioma:** **español**
- **Notas:** project-based corto.

#### [Gestión de Ingresos — Universidad de Palermo](https://www.coursera.org/learn/gestion-de-ingresos)

- **Idioma:** **español**
- **Contenido:** demand forecasting + pricing.

---

### edX

#### [Predictive Analytics for Business Planning: Time-Series Forecasting (IE University)](https://www.edx.org/learn/data-analysis/ie-university-predictive-analytics-for-business-planning-time-series-forecasting-2)

- **Proveedor:** IE University (Madrid)
- **Duración:** ~30–40 h en el certificado completo
- **Idioma:** inglés (instructores españoles)
- **Coste:** gratis para auditar; certificado de pago
- **Python:** parcial
- **Notas:** universidad española — referencia de "cómo un instructor hispanohablante presenta el tema en inglés".

#### [Learning Time Series with Interventions (MITx, MicroMasters)](https://www.edx.org/learn/data-analysis-statistics/massachusetts-institute-of-technology-learning-time-series-with-interventions)

- **Proveedor:** MIT (Statistics and Data Science MicroMasters)
- **Duración:** ~13 semanas
- **Idioma:** inglés
- **Python:** sí
- **Notas:** nivel muy avanzado (postgrado MIT). Referencia académica, no template.

#### [SP18: Time Series Analysis (Georgia Tech, ISYE 6402)](https://www.classcentral.com/course/edx-sp18-time-series-analysis-10171)

- **Proveedor:** Georgia Tech
- **Duración:** semestre universitario
- **Python:** no (R)
- **Contenido:** regresión para series, ARMA/ARIMA, (G)ARCH, VAR, forecasting, identificación y diagnóstico
- **Notas:** referencia académica rigurosa, código R.

---

### Udemy

#### [Python for Time Series Data Analysis (Jose Portilla / Pierian Data)](https://www.udemy.com/course/python-for-time-series-data-analysis/)

- **Duración:** ~15 h 21 min
- **Idioma:** inglés (subtítulos en español disponibles)
- **Rating:** 4.7/5, 8200+ ratings
- **Contenido:** NumPy/Pandas; visualización; resampling; Statsmodels (ETS/ARIMA/SARIMA); Prophet; DL con Keras
- **Notas:** referente del catálogo Udemy. Pipeline completo, pedagogía clara.

#### [Time Series Analysis, Forecasting, and Machine Learning (Lazy Programmer)](https://www.udemy.com/course/time-series-analysis/)

- **Duración:** ~23 horas
- **Rating:** 4.7/5
- **Contenido:** clásicos (ETS, ARIMA, VARMA); ML (SVR, RF); DL (RNN, LSTM, GRU, CNN); GARCH; anomalía; clasificación
- **Notas:** el más "DL-heavy" del catálogo.

#### [Master Time Series Analysis and Forecasting with Python 2026 (Marco Peixeiro)](https://www.udemy.com/course/forecasting-python/)

- **Duración:** ~13–15 h
- **Contenido:** ETS, Holt-Winters; ARIMA/SARIMA/SARIMAX; Prophet, SilverKite, Amazon Chronos; TFT, N-BEATS, NHITS; TSMixer; Darts (re-grabado sep 2025); series intermitentes, clasificación
- **Notas:** el más actualizado (incluye foundation models). Excelente referencia "estado del arte 2025-2026".

#### [Complete Time Series Forecasting Bootcamp in Python (2025)](https://www.udemy.com/course/complete-time-series-forecasting-bootcamp-in-python-2025/)

- **Duración:** ~12 horas
- **Contenido:** clásicos (ARIMA/SARIMA/SARIMAX); suavizado, TBATS, Theta; Prophet; DL (NHITS, TSMixer, iTransformer, TimeGPT); 14+ proyectos hands-on
- **Notas:** usa **NeuralForecast / StatsForecast de Nixtla**. Bueno como benchmark.

#### [Applied Time Series Analysis in Python (Marco Peixeiro)](https://www.udemy.com/course/applied-time-series-analysis-in-python/)

- **Duración:** 6 h 56 min
- **Contenido:** ADF, estacionariedad; ARMA/ARIMA/SARIMA(X); VAR/VARMA(X); DL (linear, DNN, LSTM, CNN, ResNet); Prophet
- **Notas:** versión más corta del curso "Master..." del mismo autor.

#### [Curso avanzado de Series Temporales con R y Python (Juan Gabriel Gomila)](https://www.udemy.com/course/series-temporales/)

- **Duración:** >14 horas
- **Idioma:** **español**
- **Python:** parcial (R y Python)
- **Notas:** uno de los pocos cursos serios en **español** sobre series temporales. Audiencia objetivo casi idéntica a la nuestra.

#### [Curso de series temporales multivariantes con R y Python](https://www.udemy.com/course/curso-de-series-temporales-multivariantes-con-r-y-python/)

- **Duración:** >15 horas
- **Idioma:** **español**
- **Contenido:** VAR, VECM, cointegración, 10+ casos prácticos
- **Notas:** complemento al anterior.

#### [Forecasting con Python: ARIMA y Prophet para Negocios](https://www.udemy.com/course/forecasting-con-python-arima-y-prophet-para-negocios/)

- **Idioma:** **español**
- **Contenido:** fundamentos (tendencia, estacionalidad, ruido); limpieza; ARIMA (auto_arima, validación); Prophet (exógenas, changepoints, holidays); MAPE/RMSE/AIC/BIC; presentar forecasts al negocio; automatización (pickle, scripts)
- **Notas:** muy práctico, en español. Buena referencia de "cómo explicar ARIMA + Prophet en castellano".

#### [Pronósticos (Forecasting) de Series de Tiempo con Python](https://www.udemy.com/course/pronosticos-de-series-de-tiempo-con-python/)

- **Idioma:** **español**
- **Contenido:** medias móviles, descomposición estacional, ARIMA — learning by doing

#### [Curso Python: Series Temporales con Pandas](https://www.udemy.com/course/curso-python-series-temporales-con-pandas/)

- **Idioma:** **español**
- **Contenido:** foco en Pandas, indexación temporal, resampling
- **Notas:** no cubre modelos.

#### [Utilizar Redes Neuronales para predecir Series Temporales](https://www.udemy.com/course/utilizar-redes-neuronales-para-predecir-series-temporales/)

- **Idioma:** **español**
- **Notas:** orientación industrial.

---

### DataCamp

#### [Time Series with Python Track](https://www.datacamp.com/tracks/time-series-with-python)

- **Duración:** ~20 horas en total (5 cursos)
- **Cursos incluidos:**
  - Manipulating Time Series Data in Python (Stefan Jansen, ~5 h)
  - Time Series Analysis in Python (Rob Reider, ~4 h)
  - Visualizing Time Series Data in Python (Thomas Vincent, ~4 h)
  - ARIMA Models in Python (James Fulton, ~4 h)
  - Machine Learning for Time Series Data in Python (Chris Holdgraf, ~4 h)
- **Notas:** **muy alineado con nuestra duración objetivo (~20 h)**. Estructura modular — sirve como **principal referencia estructural** para nuestro curso. James Fulton (ARIMA) es "Climate Informatics Researcher" — temática afín a hidrología.

#### [ARIMA Models in Python](https://www.datacamp.com/courses/arima-models-in-python)

- **Proveedor:** James Fulton (Climate Informatics Researcher)
- **Datasets:** candy production, **CO2**, Amazon stock, milk, **earthquakes**
- **Notas:** instructor con perfil climate science — relevancia para hidrología.

#### [Time Series Analysis in Python](https://www.datacamp.com/courses/time-series-analysis-in-python)

- **Proveedor:** Rob Reider (Quantopian / NYU)
- **Case study:** temperaturas NYC (cambio climático)
- **Notas:** dataset climático perfecto para audiencia hidrológica.

#### [Manipulating Time Series Data in Python](https://www.datacamp.com/courses/manipulating-time-series-data-in-python)

- **Contenido:** DateTimeIndex, resampling, rolling/expanding; capstone: índice bursátil
- **Notas:** base "Pandas para series temporales".

#### [Machine Learning for Time Series Data in Python](https://www.datacamp.com/courses/machine-learning-for-time-series-data-in-python)

- **Proveedor:** Chris Holdgraf (Berkeley)
- **Contenido:** envelopes, espectrogramas, derivadas; CV temporal
- **Notas:** más orientado a clasificación (audio/EEG) que forecasting.

#### [Visualizing Time Series Data in Python](https://www.datacamp.com/courses/visualizing-time-series-data-in-python)

- **Case study:** desempleo USA 2000-2010
- **Notas:** muy útil como referencia EDA.

---

### Udacity

#### [Time Series Forecasting (ud980)](https://www.udacity.com/course/time-series-forecasting--ud980)

- **Coste:** **gratis**
- **Python:** **no** (Alteryx)
- **Notas:** **no usa Python** sino Alteryx. Útil solo como referencia conceptual de la pedagogía.

---

### Kaggle Learn

#### [Time Series (Kaggle Learn)](https://www.kaggle.com/learn/time-series)

- **Proveedor:** Kaggle — Ryan Holbrook
- **Duración:** ~5 horas
- **Coste:** **gratis** con certificación
- **Contenido:** Linear Regression with Time Series; Trend; Seasonality; Time Series as Features (lag embedding); Hybrid Models; Forecasting With Machine Learning (4 estrategias)
- **Notas:** muy concentrado, enfoque ML-puro. Buen ejemplo de "feature engineering para series".

---

### Fast.ai

#### [tsai — Time Series AI library (fastai/PyTorch)](https://github.com/timeseriesAI/tsai)

- **Proveedor:** comunidad fastai — Ignacio Oguiza
- **Idioma:** inglés (Ignacio Oguiza es **hispanohablante**)
- **Coste:** **gratis** (open source)
- **Contenido:** PatchTST, InceptionTime, MiniRocket, TST, RNN+Attention; tutoriales en notebooks; sklearn-style pipelines; walk-forward CV
- **Notas:** fast.ai no tiene un curso oficial de series temporales, pero `tsai` es el recurso de referencia de la comunidad. Foro: [forums.fast.ai — Time Series Forecasting](https://forums.fast.ai/t/time-series-forecasting/66416).

---

### LinkedIn Learning

#### [Python for Time Series Forecasting](https://www.linkedin.com/learning/python-for-time-series-forecasting)

- **Proveedor:** Jesus Lopez (**hispanohablante**)
- **Duración:** 4 h 19 min
- **Python:** sí (Statsmodels, Prophet)
- **Contenido:** fundamentos; visualización (Plotly); descomposición; baselines; ARIMA/SARIMA; estacionariedad; transformaciones; métricas; suavizado exponencial; Prophet; train-test split; walk-forward (TimeSeriesSplit)
- **Repo:** <https://github.com/LinkedInLearning/python-for-time-series-forecasting-5246009>
- **Notas:** Jesús López, hispanohablante. Pipeline muy completo en 4 h con datos Fed/EIA.

#### [Real-Time Data Forecasting with AI and Python](https://github.com/LinkedInLearning/real-time-data-forecasting-with-ai-and-python-4565024)

- **Proveedor:** Tobias Zwingmann
- **Notas:** más orientado a operacionalización / deployment.

---

### 365DataScience

#### [Time Series Analysis with Python](https://365datascience.com/courses/time-series-analysis-with-python/)

- **Proveedor:** Viktor Mehandzhiyski
- **Duración:** 7 horas
- **Rating:** 4.9/5 (870 reviews)
- **Contenido:** fundamentos; white noise/random walks; ACF/PACF; AR/MA/ARMA/ARIMA/ARIMAX/SARIMAX; ARCH/GARCH; Auto ARIMA; forecasting; business case automoción; examen final
- **Notas:** muy completo en estadística clásica. **No cubre DL**.

#### [Time Series Forecasting with Python — Advanced Techniques and Machine Learning](https://365datascience.com/courses/forecasting-with-advanced-techniques-and-machine-learning/)

- **Proveedor:** Egor Howell (Deliveroo/DoorDash)
- **Duración:** 6 horas
- **Contenido:** Dynamic Regression, Dynamic Harmonic Regression; regresión no lineal, GAMs, Prophet, VAR, VECM; KNN, tree-based, NN; RNN, LSTM, GRU
- **Notas:** continuación lógica del anterior. Cubre **GAMs y VECM**, raros en otros cursos.

---

### DeepLearning.AI

#### [Sequences, Time Series and Prediction](https://www.coursera.org/learn/tensorflow-sequences-time-series-and-prediction)

_(Ya listado en Coursera — curso 4 del TensorFlow Developer Professional Certificate)_. DeepLearning.AI **no tiene curso stand-alone específico de series temporales** fuera de este.

---

## 2. Cursos universitarios

### Universidades en habla inglesa

#### [STATS 207/307 — Introduction to Time Series Analysis — Stanford](https://stanford-stats207.github.io/fall2022/)

- **Profesor:** Emily B. Fox
- **Duración / créditos:** trimestre; 3 unidades
- **Python:** sí (preferido)
- **Contenido:** estacionariedad y fundamentos; preprocesado; ARIMA/SARIMA; espacio de estados, Kalman; DL (RNN, CNN); Granger; procesos gaussianos; switching dynamical systems
- **Bibliografía:** Shumway & Stoffer; Lütkepohl
- **URLs adicionales:** [Web del curso](https://stats207.github.io/); [Catálogo Stanford](https://bulletin.stanford.edu/courses/1254251); [perfil profesora](https://emilybfox.su.domains/teaching/)
- **Notas:** sin contenido hidrológico, pero syllabus excelente para combinar clásicos + DL.

#### [14.384 Time Series Analysis — MIT OCW](https://ocw.mit.edu/courses/14-384-time-series-analysis-fall-2013/)

- **Profesor:** Anna Mikusheva (Econometrics)
- **Contenido:** univariantes estacionarios y no estacionarios; VAR; dominio frecuencial; series persistentes; cambios estructurales
- **Bibliografía:** Hamilton (1994) + Stock & Watson
- **URLs adicionales:** [Syllabus](https://ocw.mit.edu/courses/14-384-time-series-analysis-fall-2013/pages/syllabus/); [Notas](https://ocw.mit.edu/courses/economics/14-384-time-series-analysis-fall-2013/lecture-notes/)

#### [18.S096 Topics in Mathematics with Applications in Finance — MIT OCW](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/resources/lecture-8-time-series-analysis-i/)

- **Contenido:** ARMA estacionarios; multivariantes; cointegración; VAR; espacio-estado; Kalman
- **URLs adicionales:** [Lec 11](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/resources/lecture-11-time-series-analysis-ii/); [Lec 12](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/resources/lecture-12-time-series-analysis-iii/)

#### [STAT 153 / 248 — Introduction to Time Series — UC Berkeley](https://stat153.berkeley.edu/)

- **Profesor:** Liberty Hamilton (Spring 2026); previo Ryan Tibshirani, Peter Bartlett
- **Python:** sí (Spring 2026 es Python; otros años R)
- **Contenido:** dependencia; regresión lineal/no lineal/regularizada; análisis espectral y tiempo-frecuencia; AR/ARMA/ARIMA; espacio de estados; CNN/RNN; self-supervised learning
- **URLs adicionales:** [Fall 2024](https://stat153.berkeley.edu/fall-2024/); [Ryan Tibshirani 2023](https://www.stat.berkeley.edu/~ryantibs/timeseries-f23/)
- **Notas:** ejemplos en neurociencia, astronomía, epidemiología, habla — enfoque "señales y series" similar al hidrológico.

#### [36-618 Experimental Design and Time Series — CMU](https://benjaminleroy.github.io/documents/syllabi/618syllabus.pdf)

- **Profesor:** Benjamin LeRoy
- **URLs adicionales:** [Catálogo CMU Statistics](http://coursecatalog.web.cmu.edu/schools-colleges/dietrichcollegeofhumanitiesandsocialsciences/departmentofstatistics/courses/); [36-467/667 Data over Space and Time, C. Shalizi](https://www.stat.cmu.edu/~cshalizi/dst/18/) (procesos espacio-temporales — relevante para hidrogeología)

#### [46-929 Financial Time Series Analysis — CMU MSCF](https://www.cmu.edu/mscf/academics/curriculum/46929-financial-time-series-analysis.html)

- **Contenido:** ARMA/ARIMA, GARCH, multivariantes, volatilidad estocástica
- **Notas:** enfoque financiero.

#### [STSCI 4550 — Time Series Analysis — Cornell](https://classes.cornell.edu/browse/roster/SP25/subject/STSCI)

- **Contenido:** modelado lineal y no lineal, estacionales, multivariantes, financieras
- **URLs adicionales:** [STSCI 4550 SP20](https://classes.cornell.edu/browse/roster/SP20/class/STSCI/4550); [Catálogo STSCI](https://courses.cornell.edu/courses/stsci/)

#### [ORF 405 — Regression and Applied Time Series — Princeton](https://orfe.princeton.edu/courses/fall-2021/regression-and-applied-time-series)

- **Profesores:** René Carmona, Ludovic Tangpi, Jason Klusowski
- **Python:** sí
- **Contenido:** regresión lineal/no lineal/no paramétrica; kernels, NN, árboles; series aplicadas

#### [Time Series — Oxford Statistics (Hilary Term)](https://www.stats.ox.ac.uk/~reinert/time/notesht10short.pdf)

- **Profesor:** Gesine Reinert
- **Python:** no (R)
- **Contenido:** visualización y descomposición; estacionariedad y diferenciación; ARMA/ARIMA; análisis espectral
- **URLs adicionales:** [MSc Statistical Science](https://www.ox.ac.uk/admissions/graduate/courses/msc-statistical-science)

#### [MATH60046 Time Series Analysis — Imperial College London](https://www.imperial.ac.uk/computing/current-students/courses/math60046/)

- **Profesor:** Dr R. Nuermaimaiti
- **Contenido:** procesos estocásticos en tiempo discreto; detrending; representación espectral, aliasing, filtros lineales; ajuste paramétrico; incertidumbre
- **URLs adicionales:** [MSc Statistics Module Guide 2025-26](https://www.imperial.ac.uk/media/imperial-college/faculty-of-natural-sciences/department-of-mathematics/statistics/2025-26-MSc-Statistics-Module-Guide.pdf); [Group TS & Spatial Stats](https://www.imperial.ac.uk/statistics/research/time-series-spatial-statistics-and-signal-processing/)

#### [MATH33800 Time Series Analysis — University of Bristol](https://www.studocu.com/en-gb/course/university-of-bristol/time-series-analysis/2041950)

- **Python:** no (R)
- **Contenido:** procesos estacionarios, ARMA/ARIMA, predicción, espectral
- **URLs adicionales:** [School of Geographical Sciences — Hydrology](https://www.bristol.ac.uk/geography/research/hydrology/); [Hydrological Modelling CENGM0022](https://www.bris.ac.uk/unit-programme-catalogue/UnitDetails.jsa?ayrCode=20/21&unitCode=CENGM0022)
- **Notas:** Bristol es referencia internacional en hidrología.

#### [METEO 820 — Time Series Analytics for Meteorological Data — Penn State](https://www.e-education.psu.edu/meteo820/syllabus)

- **Duración:** 3 créditos; 8 lecciones (~2 sem c/u)
- **Python:** no (R)
- **Contenido:** estadísticos univariantes/multivariantes; análisis de tendencia; espectral; multivariantes; ARIMA clima
- **URLs adicionales:** [METEO 810](https://www.e-education.psu.edu/meteo810/syllabus); [METEO 830](https://www.e-education.psu.edu/meteo830/syllabus)
- **Notas:** muy aplicable como referencia para hidrología (mismo tipo de datos).

#### [GEOSC 452 Hydrogeology — Penn State](https://bulletins.psu.edu/university-course-descriptions/undergraduate/geosc/)

- **Contenido:** ocurrencia, movimiento, calidad de agua subterránea; análisis de datos hidrogeológicos
- **URLs adicionales:** [Contaminant Hydrogeology EnvSE 408](https://personal.ems.psu.edu/~fkd/courses/geoee408/cm/index.html)

#### [Time Series Analysis (401-4623) — ETH Zurich](https://www.vvz.ethz.ch/Vorlesungsverzeichnis/lerneinheit.view?lerneinheitId=173039&semkez=2023W&ansicht=LEHRVERANSTALTUNGEN&lang=en)

- **Python:** no (R)
- **Contenido:** estacionarios, ARMA, espectral, predicción, ARIMA, GARCH
- **URLs adicionales:** [AS20](https://stat.ethz.ch/lectures/as20/timeseries.php); [Applied TS SS17](https://stat.ethz.ch/lectures/ss17/applied-time-series.php); [Hydrology bachelor — ETH](https://hyd.ifu.ethz.ch/education/bachelor-courses/hydrology.html)

#### [Hydrology of catchments, rivers and deltas — TU Delft OCW](https://ocw.tudelft.nl/courses/hydrology-of-catchments-rivers-and-deltas/)

- **Python:** parcial
- **URLs adicionales:** [MOOC Introduction to Water and Climate](https://online-learning.tudelft.nl/courses/introduction-to-water-and-climate/); [Pre-knowledge Civil Engineering](https://tudelft-citg.github.io/pre-for-cem/contents/home.html)
- **Notas:** la programación de TU Delft enfatiza notebooks Jupyter.

#### [MSc Hydrology and Water Resources — Wageningen](https://www.wur.nl/en/education-programmes/master/msc-programmes/msc-earth-and-environment/specialisations/hydrology-and-water-resources.htm)

- **Profesor:** Hydrology and Environmental Hydraulics Group
- **URLs adicionales:** [Cursos HWM](https://www.wur.nl/en/research-results/chair-groups/environmental-sciences/hydrology-and-environmental-hydraulics-group/education/courses.htm); [Catchment & land surface hydrology](https://www.wur.nl/en/research-results/chair-groups/environmental-sciences/hydrology-and-environmental-hydraulics-group/research/catchment-and-land-surface-hydrology.htm)

#### [CE 215 Stochastic Hydrology — IISc Bangalore (NPTEL)](https://nptel.ac.in/courses/105108079)

- **Profesor:** Prof. P. P. Mujumdar
- **Duración:** ~40 vídeos (curso abierto NPTEL)
- **Coste:** **gratis**
- **Contenido:** probabilidad/distribuciones hidrología; estimación; series temporales hidrológicas; ARMA/ARIMA Box-Jenkins; generación sintética; Markov; frecuencias (avenidas, sequías); casos reales (cuencas indias)
- **URLs adicionales:** [Syllabus IISc](https://iisc.ac.in/wp-content/uploads/2017/12/CE215.pdf); [Vídeos](http://www.infocobuild.com/education/audio-video-courses/architectural-and-civil-engineering/stochastic-hydrology-iisc-bangalore.html)
- **Notas:** **ALTÍSIMA relevancia para Komorebi** — referente abierto más cercano al curso que queremos diseñar.

#### [CE 5500 Stochastic Hydrology — University of Virginia](https://digitalcommons.usu.edu/ecstatic_all/80/)

- **Profesor:** Julianne D. Quinn
- **Python:** sí (notebooks)
- **Contenido:** análisis estocástico aplicado a sistemas hídricos; incertidumbre; generación sintética
- **Notas:** material en eCSTATIC (Utah).

#### [Stochastic Hydrology — Oregon State (Babbar-Sebens)](https://digitalcommons.usu.edu/ecstatic_all/58/)

- **Notas:** otro recurso eCSTATIC.

---

### Universidades de habla hispana

#### [Métodos Estadísticos en Hidrología (250MAG008) — UPC Barcelona](https://ocw-camins.upc.edu/ocw/assignatura/250MAG008/2025/temari?_lang=es)

- **Duración:** 125 horas (4–5 ECTS) — máster Hidrología Subterránea
- **Idioma:** **español**
- **Python:** **sí — Jupyter + NumPy + SciPy + Pandas + Matplotlib**
- **Contenido principal:**
  - Repaso probabilidad e inferencia (8 h 20 m)
  - Análisis estadístico con Python (25 h)
  - Series temporales, distribuciones de extremos, predicción, PCA (41 h 40 m)
  - Geoestadística: variogramas, kriging, simulación espacial hidrogeología (50 h)
- **URLs adicionales:** [Master in Subsurface Hydrology](https://camins.upc.edu/en/Studies/master/subsurface-hydrology/msdsh); [Grupo Hidrología Subterránea](https://h2ogeo.upc.edu/es/investigacion-hidrologia-subterrania/docencia-hidrologia-subterrania)
- **Notas:** **REFERENCIA PRINCIPAL.** Es el curso más alineado: español + Python + hidrología + estadística + geoestadística. Inspeccionarlo en detalle.

#### [Series Temporales (2231131) — Grado en Estadística, UGR](https://grados.ugr.es/estadistica/docencia/plan-estudios/series-temporales/guia-docente)

- **Profesores:** F. J. Alonso Morales; Gustavo Rivas Gervilla
- **Duración:** 6 ECTS
- **Idioma:** **español**
- **Python:** no (R)
- **Contenido:** procesos estocásticos; Box-Jenkins; ARMA/ARIMA; estacionales; regresión dinámica e intervención; espectral
- **Notas:** UGR comparte la cuenca del Guadalquivir con nuestro caso de estudio.

#### [Máster en Geología Aplicada a la Obra Civil y los Recursos Hídricos — UGR](https://masteres.ugr.es/georhid/pages/master)

- **Idioma:** **español**
- **Contenido:** prospección hidrogeológica, captación, modelado de acuíferos
- **URLs adicionales:** [Hidrogeología — Instituto del Agua UGR](https://institutodelagua.ugr.es/investigacion/secciones/hidrogeologia); [Hidrogeología Ciencias Ambientales](https://grados.ugr.es/ramas/ciencias/grado-ciencias-ambientales/hidrogeologia/guia-docente); [Procesos Hidrológicos Superficiales — Máster IdeA](https://ecologia.ugr.es/en/teaching/postgraduates/master-universitario-tecnicas-y-ciencias-la-calidad-del-agua-idea/course-guide/M96/56/1/1)

#### [Máster MUIHMA — UPV Valencia / IIAMA](https://www.upv.es/estudios/master/muihma/en/home/)

- **Idioma:** **español**
- **Contenido:** _Hidrología Estocástica_, _Modelación Hidrológica y Ambiental Distribuida_
- **URLs adicionales:** [IIAMA Training](https://iiama.webs.upv.es/en/training/); [Grupo GIMHA](https://iiama.webs.upv.es/en/research/research-groups/hydrological-and-environmental-modelling/)
- **Notas:** referente español de primer nivel.

#### [Máster en Ingeniería Civil — UPM Caminos](https://caminos.upm.es/master-universitario-en-ingenieria-civil-hidraulica-energia-y-medio-ambiente/)

- **Idioma:** **español**
- **Contenido:** especialidad Hidráulica; gestión de recursos; avenidas y sequías; adaptación al cambio climático
- **URLs adicionales:** [Programa Académico](https://caminos.upm.es/programa-academico-de-ingeniero-a-de-caminos-canales-y-puertos/); [Guías docentes T1](https://caminos.upm.es/wp-content/uploads/2023/08/04AG_2023-24_TOMO_I_V2AED.pdf); [Tesis: integración espacio-temporal de aportaciones, régimen natural](https://oa.upm.es/1227/)

#### [Análisis de Series Temporales — Máster Investigación en Economía, UNED](https://www.uned.es/universidad/inicio/en/estudios/masteres/master-universitario-en-investigacion-en-economia/asignaturas.html?codAsignatura=25503380&codTitulacion=250301)

- **Idioma:** **español**
- **Python:** no (R)
- **Contenido:** componentes; AR/MA/ARMA; ARIMA; identificación, estimación, diagnóstico, predicción
- **URLs adicionales:** [IEF en UNED](https://www.uned.es/universidad/inicio/en/estudios/formacion-permanente/cursos/experto-metodos-avanzados/programa/analisis-series-temporales.html); [Estadística Aplicada — Formación Permanente](https://formacionpermanente.uned.es/tp_actividad/idactividad/7703)

#### [Análisis de Series Temporales (14245) — UC3M Madrid](https://aplicaciones.uc3m.es/cpa/generaFicha?est=224&asig=14245&idioma=1)

- **Idioma:** **español**
- **Python:** no (R)
- **Contenido:** Box-Jenkins; AR/MA/ARMA/ARIMA; GARCH y volatilidad estocástica
- **URLs adicionales:** [Series temporales y predicción 17312](https://aplicaciones.uc3m.es/cpa/generaFicha?est=350&plan=392&asig=17312&idioma=1); [Aprendizaje en Series y Flujos de Datos 19199](https://aplicaciones.uc3m.es/cpa/generaFicha?est=378&asig=19199&idioma=1); [Apuntes A. Alonso — Introducción al Análisis de Series Temporales (PDF)](https://halweb.uc3m.es/esp/personal/personas/amalonso/esp/seriestemporales.pdf)
- **Notas:** los apuntes en PDF son **muy útiles**.

#### [Series Temporales — Grado en Estadística, US (Sevilla)](https://www.us.es/estudiar/que-estudiar/oferta-de-grados/grado-en-estadistica/1960029)

- **Profesores:** Antonio Beato Moreno y María Dolores Jiménez Gamero
- **Python:** no (R)

#### [Análisis de Series Temporales — UCM Madrid](https://matematicas.ucm.es/estudios/grado-economiamatematicas-plan-900722)

- **Python:** no (R y EViews)
- **Contenido:** ARMA/ARIMA, estacionalidad, Box-Jenkins, intervenciones/outliers, función de transferencia
- **URLs adicionales:** [Notas J.A. Martín en PDF (UCM)](https://www.ucm.es/data/cont/docs/518-2013-11-11-JAM-IAST-Libro.pdf)

#### [Series Temporales — Universidad de Zaragoza](http://titulaciones.unizar.es/asignaturas/30308/actividades14.html)

- **Python:** no
- **Contenido:** regresión, medias móviles, suavizado exponencial, ARMA/ARIMA, Box-Jenkins

#### [Centro de Estudios Hidrográficos (CEH) — CEDEX](https://ceh.cedex.es/)

- **Idioma:** **español**
- **Actividad:** Curso Internacional de Hidrología General y Aplicada (anual, Madrid); Base de datos HIDRO; modelo SIMPA; aplicación CHAC
- **URLs adicionales:** [CEH overview](https://www.cedex.es/centros-laboratorios/centro-de-estudios-hidrograficos-ceh); [Líneas — Hidrología](https://www.cedex.es/centros-laboratorios/centro-estudios-hidrograficos-ceh/lineas-actividad/hidrologia); [Documentación](https://ceh.cedex.es/web/Documentacion.htm); [Hidrología CEH](https://ceh.cedex.es/web/hidrologia.htm)
- **Notas:** referencia institucional obligada en España.

#### [Másteres con materias de hidrogeología — AIH-GE catálogo](https://www.aih-ge.org/masteres-con-materias-de-hidrogeologia/)

- **URL adicional:** [Máster Hidrología y Gestión de Recursos Hídricos UAH](https://master-universitario-hidrologia.web.uah.es/semipresencial.htm)

#### [Modelización de Sistemas Hídricos — Universidad de Salamanca](https://www.usal.es/modelizacion-de-sistemas-hidricos-online)

- **Idioma:** **español**
- **Contenido:** máster online en modelado hidrológico con herramientas computacionales.

---

## 3. Libros y referencias bibliográficas

### Time-series clásicos

#### [Forecasting: Principles and Practice, 3.ª ed. (fpp3)](https://otexts.com/fpp3/)

- **Autores / año / edición:** Rob J. Hyndman & George Athanasopoulos, 2021 (3.ª ed.; online actualizado en 2026)
- **Editorial:** OTexts (Monash University)
- **Coste:** **libre** online
- **Lenguaje:** R (tidyverse / fable / tsibble)
- **Tabla de contenidos (resumen):** getting started; gráficos; descomposición; features; toolbox; juicio; regresión; suavizado exponencial; ARIMA; regresión dinámica; jerárquicas/agrupadas; avanzados; cuestiones prácticas
- **Versión Python (no oficial):** [Anthology of Data Science — fpp the Pythonic Way](https://anthology-of-data.science/books/fpp.html); [GitHub pedroafleite/fpp3](https://github.com/pedroafleite/fpp3)
- **Versión Python (Hyndman + Nixtla + Amazon):** <https://otexts.com/fpppy/>
- **Edición previa:** [fpp2 (2018)](https://otexts.com/fpp2/)
- **Notas:** la referencia más usada del mundo. Estructura ideal para reutilizar como guion en 20 h.

#### [Time Series Analysis and Its Applications: With R Examples (5.ª ed.)](https://link.springer.com/book/10.1007/978-3-031-70584-7)

- **Autores / año:** Robert H. Shumway & David S. Stoffer, 2025 (5.ª ed.)
- **Editorial:** Springer (Springer Texts in Statistics)
- **Coste:** **de pago** (ediciones previas con PDF accesible)
- **Lenguaje:** R (`astsa`)
- **Contenido:** características; regresión/EDA; ARIMA; espectral; espacio-estado y Kalman; multivariantes; categóricas; memoria larga; no lineales; GARCH/volatilidad; resampling; MCMC; partículas; detección de cambios
- **PDFs antiguos:** [Edición previa](http://pzs.dstu.dp.ua/DataMining/times/bibl/TimeSeries.pdf); [UNAM](https://sistemas.fciencias.unam.mx/~ediaz/Cursos/Estadistica3/Libros/Time%20Series%20Analysis%20and%20Its%20Applications.pdf)
- **Notas:** estándar a nivel posgrado. Combinar con fpp3 para profundizar.

#### [Time Series Analysis](https://catdir.loc.gov/catdir/toc/prin031/93004958.html)

- **Autor / año:** James D. Hamilton, 1994 (1.ª ed.)
- **Editorial:** Princeton University Press
- **Lenguaje:** agnóstico (teórico-matemático)
- **Contenido (resumen):** lag operators; ARMA estacionarios; predicción; máxima verosimilitud; espectral; teoría asintótica; regresión; sistemas lineales simultáneos; vectoriales; VAR; bayesiano; Kalman; GMM; no estacionarias; raíces unitarias; cointegración; FIML cointegrado; ARCH/GARCH; cambio de régimen
- **URLs adicionales:** [JSTOR](https://www.jstor.org/stable/j.ctv14jx6sm); [Resumen Estima](https://www.estima.com/textbook_hamilton.shtml)
- **Notas:** la "biblia" de econometría temporal. Denso, referencia teórica.

#### [Practical Time Series Analysis: Prediction with Statistics and Machine Learning](https://www.oreilly.com/library/view/practical-time-series/9781492041641/)

- **Autora / año:** Aileen Nielsen, 2019
- **Editorial:** O'Reilly
- **Lenguaje:** Python (mayoría) y R
- **Contenido:** historia; limpieza; EDA; simulación; almacenamiento; modelos estadísticos; espacio-estado; features; ML; deep learning; medición de errores; performance; producción; salud; finanzas
- **GitHub:** [TimeSeriesAnalysisWithPython](https://github.com/AileenNielsen/TimeSeriesAnalysisWithPython)
- **Notas:** **el** libro Python-friendly aplicado.

#### [Deep Learning for Time Series Forecasting](https://machinelearningmastery.com/deep-learning-for-time-series-forecasting/)

- **Autor / año:** Jason Brownlee, 2018
- **Editorial:** Machine Learning Mastery (autoeditado)
- **Lenguaje:** Python (Keras + TensorFlow)
- **Contenido:** MLP, CNN, RNN/LSTM para series; 2 proyectos end-to-end; 25 tutoriales; 131 ficheros `.py`; 575 páginas
- **URLs adicionales:** [Google Books](https://books.google.com/books/about/Deep_Learning_for_Time_Series_Forecastin.html?id=o5qnDwAAQBAJ); [Mini-curso 7 días](https://machinelearningmastery.com/how-to-get-started-with-deep-learning-for-time-series-forecasting-7-day-mini-course/); [Time Series Forecasting With Python (libro hermano)](https://machinelearningmastery.com/introduction-to-time-series-forecasting-with-python/)

#### [Practical Time Series Forecasting with Python: A Hands-On Guide](https://www.forecastingbook.com/)

- **Autores / año:** Galit Shmueli & Eric Berger, 2024
- **Lenguaje:** Python
- **Contenido (síntesis):** introducción; visualización y descomposición; performance evaluation; promedios y suavizados; regresión; ARIMA; redes neuronales; deep learning; ensembles; casos de negocio
- **GitHub:** [gshmueli/ptsf-Python](https://github.com/gshmueli/ptsf-Python)

#### [Time Series Analysis: Forecasting and Control, 5.ª ed.](https://www.wiley.com/en-us/Time+Series+Analysis:+Forecasting+and+Control,+5th+Edition-p-9781118675021)

- **Autores / año:** Box, Jenkins, Reinsel, Ljung, 2015
- **Editorial:** Wiley
- **Notas:** el texto histórico que da nombre a la metodología Box-Jenkins. Referencia, no libro de texto.

#### [Time Series Analysis: Univariate and Multivariate Methods, 2.ª ed.](https://www.amazon.com/Time-Analysis-Univariate-Multivariate-Methods/dp/0321322169)

- **Autor / año:** William W. S. Wei, 2006
- **URLs adicionales:** [Datasets Temple](https://sites.temple.edu/wwei/files/2020/08/data_sets-1.pdf); [Pearson](https://www.pearson.com/en-us/subject-catalog/p/time-series-analysis-univariate-and-multivariate-methods-classic-version/P200000006412/9780137981465)

#### [Time Series Analysis: With Applications in R](https://link.springer.com/book/10.1007/978-0-387-75959-3)

- **Autores:** Jonathan D. Cryer & Kung-Sik Chan, 2008
- **URLs adicionales:** [Web Chan en U. Iowa](http://homepage.divms.uiowa.edu/~kchan/TSA.htm); [Soluciones](https://jolars.github.io/TSAsolutions/)
- **Notas:** muy didáctico para grado.

#### [Analysis of Financial Time Series, 3.ª ed.](https://faculty.chicagobooth.edu/ruey-s-tsay/research/analysis-of-financial-time-series-3rd-edition)

- **Autor:** Ruey S. Tsay, 2010
- **Port a Python:** [Jincheng-Gong/aofts3rd_python](https://github.com/Jincheng-Gong/aofts3rd_python)
- **Notas:** orientado a finanzas; lecciones de volatilidad útiles para eventos extremos hidrológicos.

#### [New Introduction to Multiple Time Series Analysis](https://link.springer.com/book/10.1007/978-3-540-27752-1)

- **Autor:** Helmut Lütkepohl, 2005
- **URL adicional:** [Stata Bookstore](https://www.stata.com/bookstore/multiple-time-series-analysis/)
- **Notas:** referencia obligada en VAR/VECM.

#### [Introduction to Time Series and Forecasting, 3.ª ed.](https://link.springer.com/book/10.1007/978-3-319-29854-2)

- **Autores:** Peter J. Brockwell & Richard A. Davis, 2016
- **Notas:** balance teórico/aplicado, pre-requisitos suaves.

### Hidrología + series temporales

#### [Time Series Modelling of Water Resources and Environmental Systems](https://www.sciencedirect.com/bookseries/developments-in-water-science/vol/45)

- **Autores / año:** Keith W. Hipel & A. Ian McLeod, 1994 (vol. 45 _Developments in Water Science_)
- **Editorial:** Elsevier (copyright revertido a autores; reprint electrónico gratuito)
- **Tabla de contenidos (1013 pp., resumen):**
  - I: rol del modelado en aguas y series ambientales
  - II: ARMA estacionarios e identificación
  - III: ARMA no estacionarios
  - IV: memoria larga, fenómeno de Hurst
  - V: estacionales (ARIMA estacional, PARMA, deseasonalizado)
  - VI: entrada-salida múltiple (transfer function)
  - VII: análisis de intervención
  - VIII: ARMA multivariantes
  - IX: simulación, observaciones faltantes, predicción, causalidad
  - X: decisiones con series temporales
- **URLs adicionales:** [Página del autor](http://www.systems.uwaterloo.ca/Faculty/Hipel/Time%20Series%20Book.htm); [SYDE 631](http://www.systems.uwaterloo.ca/Faculty/Hipel/SYDE631.html)
- **Notas:** **referencia capital.** El tratado más completo de series temporales aplicadas a aguas.

#### [Applied Modeling of Hydrologic Time Series](https://books.google.com/books/about/Applied_Modeling_of_Hydrologic_Time_Seri.html?id=GinL-8Cc6QgC)

- **Autores / año:** J. D. Salas, J. W. Delleur, V. Yevjevich, W. L. Lane, 1980
- **Editorial:** Water Resources Publications
- **Contenido (484 pp., resumen):** procesos estocásticos hidrológicos; descomposición; tests estacionariedad; AR/MA/ARMA/ARIMA; PARMA; desagregación temporal y espacial; multivariantes; generación sintética; momentos y memoria larga; gestión de embalses
- **Capítulo más citado:** Salas (1993). _Analysis and Modeling of Hydrologic Time Series_. Cap. 19 en [Maidment, _Handbook of Hydrology_, McGraw-Hill](https://www.scirp.org/reference/ReferencesPapers?ReferenceID=1186482) — accesible en [Scribd](https://www.scribd.com/document/53252964/Salas-Maidment-1993-Analysis-and-Modeling-of-Hydrologic-Time-Series)
- **Notas:** **texto fundacional** específico de hidrología. Pareja con Hipel & McLeod.

#### [Statistical Characteristics of Hydrologic Time Series — capítulo Springer](https://link.springer.com/chapter/10.1007/978-94-007-1861-6_2)

- **Autores:** Machiwal & Jha, 2012
- **Notas:** complemento moderno a Salas y Hipel/McLeod; tests específicos (Mann-Kendall, Pettitt).

#### [Analysis of Hydrologic Time Series — capítulo en _Engineering Hydrology_ (Wilson)](https://link.springer.com/chapter/10.1007/978-1-349-03467-3_2)

- Introducción accesible al análisis estadístico de registros hidrológicos.

---

## 4. Hidrología, hidrogeología y series temporales

### Cursos y workshops de organizaciones del agua

#### [USGS Python for Hydrology Self-Study Curriculum](https://www.usgs.gov/software/python-hydrology-self-study-curriculum)

- **Organización:** USGS — HyTEST
- **Coste:** Gratuito
- **Contenido:** Parte 0 (Python para análisis hidrológico: Pandas, xarray, visualización), Parte 1 (FloPy/MODFLOW)
- **URLs:** [Sitio](https://doi-usgs.github.io/python-for-hydrology/latest/index.html); [GitLab](https://code.usgs.gov/wma/hytest/training/python-for-hydrology); [GitHub](https://github.com/DOI-USGS/python-for-hydrology)

#### [HyTEST Hydro-Terrestrial Earth System Testbed](https://hytest-org.github.io/hytest/doc/About.html)

- **Organización:** USGS + NCAR
- **Contenido:** Notebooks Jupyter para modelado hidrológico en nube y HPC; Zarr; NWM
- **GitHub:** <https://github.com/hytest-org>

#### [USGS dataretrieval Python Package Usage Examples](https://www.hydroshare.org/resource/c97c32ecf59b4dff90ef013030c54264/)

- **Organización:** CUAHSI / USGS
- **Contenido:** notebooks `get_dv()`, `get_gwlevels()`, `get_discharge_measurements()`

#### [NOAA OWP Data Service Notebooks (WRDS)](https://github.com/NOAA-OWP/data-service-notebooks)

- **Contenido:** servicios de datos del National Water Model y pronósticos operacionales

#### [CIROH FIM Workshops](https://ciroh.ua.edu/devconference/fim-workshop-listings/)

- **Contenido:** workshops anuales sobre Flood Inundation Mapping con notebooks Python

#### [IAH — Time series modeling of Groundwater levels with Pastas](https://iah.org/education/professionals/training/time-series-modeling-of-groundwater-levels-with-pastas)

- **Organización:** International Association of Hydrogeologists
- **Contenido:** teoría + práctica con Pastas. Imparten Raoul Collenteur, Mark Bakker y Frans Schaars
- **Edición presencial IAH 2021 Bruselas:** <https://iah2021belgium.org/programme/sunday-courses/>

#### [IAH Python Masterclass: Advanced Skills for Hydrology](https://iah.org/events/python-masterclass-advanced-skills-for-hydrology)

- **Contenido:** Python avanzado específicamente para hidrólogos/hidrogeólogos

#### [IAH Hydrogeological Modelling Webinar Series](https://iah.org/education/professionals/training/hydrogeological-modelling-webinar-series)

- **Coste:** gratis para miembros

#### [WMO Hydrology Training Activities](https://community.wmo.int/site/knowledge-hub/programmes-and-initiatives/hydrology-and-water-resources/training-activities)

- **Contenido:** pronóstico hidrológico (incluye PyCPT y ML sub-seasonal AGRHYMET 2025)
- **URLs adicionales:** [Cursos](https://community.wmo.int/en/training-courses); [Publicaciones Hidrología](https://community.wmo.int/en/activity-areas/hydrology-and-water-resources/publications); [WMO Guide to Hydrological Practices](https://portal.camins.upc.edu/materials_guia/250144/2013/WMOENG.pdf)

#### [CEDEX — Centro de Estudios Hidrográficos](https://ceh.cedex.es/)

- **Idioma:** español
- **Contenido:** anuarios de aforos, modelo SIMPA, documentación tratamiento estadístico
- **Documento clave:** [Tendencias en modelación hidrológica y estadística (MITECO+CEDEX)](https://www.miteco.gob.es/content/dam/miteco/es/agua/formacion/gri-herramientas-hidrologicas-variabilidad-temporal-clima-inundaciones_tcm30-379109.pdf)

#### [MITECO — SAIH](https://www.miteco.gob.es/en/agua/temas/evaluacion-de-los-recursos-hidricos/saih.html)

- **Contenido:** Sistema Automático de Información Hidrológica
- **URLs:** [Descripción](https://www.miteco.gob.es/content/dam/miteco/es/agua/publicaciones/SAIH_WEB_MMA_V301109_tcm30-136204.pdf); [Anuario de aforos](https://www.miteco.gob.es/en/cartografia-y-sig/ide/descargas/agua/anuario-de-aforos.html); [Descarga SAIH](https://www.miteco.gob.es/en/cartografia-y-sig/ide/descargas/agua/saih.html)

#### [SAIH CH Guadalquivir](https://www.chj.es/es-es/medioambiente/SAIH/Paginas/Inicio.aspx)

- **Contenido:** datos en tiempo casi real del Genil
- **URL adicional:** [Catálogo gob.es Guadalquivir SAIH](https://datos.gob.es/en/catalogo/ea0043519-sistema-automatico-de-informacion-hidrologica-saih-de-la-demarcacion-hidrografica-del-guadalquivir)

#### [HEPEX — Hydrological Ensemble Prediction Experiment](https://hepex.org.au/)

- **Contenido:** pronóstico hidrológico por ensembles, post-procesamiento, verificación

#### [SARAI — Series de piezometría y precipitación de España (IGME)](https://sarai.igme.es/index.php/tool-to-obtain-time-series-of-piezometry-and-precipitation-from-1950-to-2020-respectively-and-directly-from-miteco-and-aemet-for-any-point-in-spain-in-the-iberian-peninsula-and-the-balearic-islands/)

- **Organización:** IGME-CSIC
- **Idioma:** español
- **Contenido:** notebook Jupyter que descarga series 1950-2020 desde MITECO/AEMET. **Extremadamente relevante** para caso Duero/Genil.

#### [AGU — Frontiers in Hydrology Meeting](https://www.agu.org/fihm)

- **Contenido:** short courses; muchos sobre ML/DL en hidrología
- **URL adicional:** [Tutorial ML/DL 2019](https://www.agu.org/Events/SCIWS20-Tutorial-on-Machine-Learning)

### Cursos universitarios con foco hídrico

#### [Hydroinformatics and Water Data Science (USU, HydroLearn)](https://edx.hydrolearn.org/courses/course-v1:USU+CEE6110+2022/about)

- **Organización:** USU / HydroLearn / CUAHSI
- **Coste:** Gratuito
- **Contenido:** acceso programático web services; ciclo de vida sensores; control de calidad; bases de datos; intro ML; Python

#### [HydroLearn Platform](https://hydrolearn.org/)

- **Contenido:** 50+ módulos sobre hidrología física, aguas subterráneas, calidad de agua, análisis de frecuencias
- **Catálogo:** <https://edx.hydrolearn.org/courses>

#### [Hydroinformatics Education at Iowa (UIHILab)](https://hydroinformatics.uiowa.edu/education.php)

- **Contenido:** CEE:5310 Environmental Informatics

#### [Hydro-Informatics.com — Sebastian Schwindt](https://hydro-informatics.com/)

- **Organización:** University of Stuttgart
- **Coste:** Gratuito (eBook abierto)
- **Contenido:** eBook completo con lecciones y ejercicios Python para water resources
- **URLs:** [Sitio del autor](https://sebastian-schwindt.org/); [GitHub team](https://github.com/hydro-informatics)

#### [Pastas Workshop — TU Delft / University of Graz](https://github.com/pastas/pastas_research)

- **Organización:** TU Delft (Mark Bakker) + Eawag (Raoul Collenteur) + Artesia (Frans Schaars)
- **URLs:** [Página personal Collenteur](https://raoulcollenteur.github.io/); [Página Mark Bakker TU Delft](https://www.tudelft.nl/en/staff/mark.bakker/)

#### [BYU Hydroinformatics](https://byu-hydroinformatics.edunext.io/)

- **Contenido:** BYU-Hydro 201 Intro to Python and Python Environments

#### [Australian Water School — Python for Hydrology and Hydrogeology](https://awschool.com.au/training/python-for-hydrology-and-hydrogeology/)

- **Contenido:** data wrangling, EDA multivariante, PCA, clustering, detrending temporal/frecuencial, regresión por deconvolución, harmonic least squares, deconvolución piezometría. Instructor Vincent Post
- **Cursos relacionados:**
  - [Python essentials for water](https://awschool.com.au/training/python-essentials-for-water/)
  - [Python Masterclass for Hydrology](https://awschool.com.au/training/python-masterclass-for-hydrology/)
  - [Modelling groundwater level time series with Pastas (Mark Bakker)](https://awschool.com.au/training/modelling-groundwater-pastas/)
  - [Groundwater modelling in Python](https://awschool.com.au/training/groundwater-modelling-in-python/)
  - [Python Applications for Hydrology and Hydrogeology (YouTube gratis)](https://www.classcentral.com/course/youtube-python-applications-for-hydrology-and-hydrogeology-112399)

#### [Hatari Labs / Gidahatari — cursos en español](https://gidahatari.com/cu-es/curso-virtual-de-python-en-hidrologia-bpthz)

- **Organización:** Hatari Labs (Perú)
- **Idioma:** **español** (también inglés)
- **Coste:** de pago
- **Contenido:** Curso Python en Hidrología; Diplomado Python para Recursos Hídricos y Geociencias; MODFLOW + FloPy
- **URLs adicionales:** [Listado links Python recursos hídricos](https://gidahatari.com/ih-es/los-mejores-links-para-aprender-python-en-recursos-hidricos); [Lista paquetes hidrogeología](https://hatarilabs.com/ih-en/a-comprehensive-list-of-specific-python-packages-for-hydrogeology-and-groundwater-modeling); [Tutorial pysheds](https://hatarilabs.com/ih-en/watershed-and-stream-network-delimitation-with-python-and-pysheds-tutorial)

#### [Modelización de Sistemas Hídricos — USAL](https://www.usal.es/modelizacion-de-sistemas-hidricos-online)

- **Idioma:** español

#### [Hydroinformatics at Virginia Tech — Flow Duration Curves](https://vt-hydroinformatics.github.io/fdcs.html)

- **Coste:** gratuito; libro abierto.

### Pastas (modelos de respuesta a impulsos para piezometría)

#### [Documentación oficial Pastas](https://pastas.readthedocs.io/)

- **Estable:** <https://pastas.readthedocs.io/stable/>
- **Latest (dev):** <https://pastas.readthedocs.io/latest/>
- **GitHub:** <https://github.com/pastas/pastas>

#### [Pastas — Paper original (Collenteur et al. 2019)](https://ngwa.onlinelibrary.wiley.com/doi/abs/10.1111/gwat.12925)

- **Cita:** Collenteur, R., Bakker, M., Caljé, R., Klop, S., Schaars, F. (2019). _Pastas: Open Source Software for the Analysis of Groundwater Time Series_. Groundwater 57(6).
- **Open access PMC:** <https://pmc.ncbi.nlm.nih.gov/articles/PMC6899905/>
- **Zenodo (notebooks suplementarios):** <https://zenodo.org/record/7928822>
- **TU Delft repo:** <https://repository.tudelft.nl/record/uuid:9974c10b-f25b-44c9-898d-fbc8f71b68a1>

#### Galería de ejemplos Pastas

- **Examples Gallery v1.13:** <https://pastas.readthedocs.io/stable/examples/index.html>
- **Standardized Groundwater Index (SGI):** <https://pastas.readthedocs.io/latest/examples/standardized_groundwater_index.html>
- **Groundwater Signatures:** <https://pastas.readthedocs.io/stable/examples/signatures.html>

#### [Paper Bakker & Schaars 2019: "Solving Groundwater Flow Problems with Time Series Analysis"](https://ngwa.onlinelibrary.wiley.com/doi/full/10.1111/gwat.12927)

- **Open access PMC:** <https://pmc.ncbi.nlm.nih.gov/articles/PMC6899660/>
- **Special Section Groundwater on TS:** <https://ngwa.onlinelibrary.wiley.com/toc/17456584/2019/57/6>

### Librerías Python específicas (hidrología)

| Librería                        | URL                                                                                        | Descripción                                                                                                                                        | Idioma docs      |
| ------------------------------- | ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| pastas                          | <https://pastas.readthedocs.io/>                                                           | Piezometría con funciones de respuesta impulsional (Gamma, exponencial, Hantush). Ideal para caso Duero.                                           | inglés           |
| dataretrieval                   | <https://doi-usgs.github.io/dataretrieval-python/>                                         | Cliente USGS NWIS + Water Quality Portal. Repo: <https://github.com/DOI-USGS/dataretrieval-python>                                                 | inglés           |
| hydrofunctions                  | <https://hydrofunctions.readthedocs.io/>                                                   | Conveniencia sobre NWIS, salida a Pandas. [Tutorial](https://hydrofunctions.readthedocs.io/en/master/notebooks/Hydrofunctions_Tutorial.html)       | inglés           |
| hydroeval                       | <https://thibhlln.github.io/hydroeval/>                                                    | NSE, KGE (Gupta 2009, modificada, non-parametric), RMSE, MARE, pbias. Repo: <https://github.com/ThibHlln/hydroeval>                                | inglés           |
| hydrostats                      | <https://hydrostats.readthedocs.io/>                                                       | 70+ métricas; ensemble forecast skill scores                                                                                                       | inglés           |
| pysheds                         | <https://github.com/mdbartos/pysheds>                                                      | Delineación de cuencas y drenaje desde DEM. [Docs](https://github.com/mdbartos/pysheds/blob/master/docs/index.md)                                  | inglés           |
| pyflwdir                        | <https://deltares.github.io/pyflwdir/latest/>                                              | DEM + flow direction (numba). Strahler, HAND, floodplains, pfafstetter                                                                             | inglés           |
| pysteps                         | <https://pysteps.github.io/>                                                               | Nowcasting de precipitación radar. [Docs](https://pysteps.readthedocs.io/) — [Paper GMD](https://gmd.copernicus.org/articles/12/4185/2019/)        | inglés           |
| neuralhydrology                 | <https://neuralhydrology.readthedocs.io/en/latest/>                                        | LSTM/GRU para streamflow con CAMELS. Tutorials multi-timescale, finetuning. [Sitio](https://neuralhydrology.github.io/)                            | inglés           |
| Caravan                         | <https://github.com/kratzert/Caravan>                                                      | Dataset global hidrología large-sample (6830 cuencas, ERA5-Land + caudales)                                                                        | inglés           |
| CAMELS-ES                       | <https://zenodo.org/records/8428374>                                                       | **Spanish CAMELS: 269 cuencas en España 1991-2020. Contribución a Caravan. Imprescindible para curso en español.**                                 | inglés           |
| pywqp                           | <https://github.com/wblondeau-usgs/pywqp>                                                  | Cliente Python USGS/EPA Water Quality Portal                                                                                                       | inglés           |
| FloPy                           | <https://github.com/modflowpy/flopy>                                                       | Interfaz Python para MODFLOW. [USGS](https://www.usgs.gov/software/flopy-python-package-creating-running-and-post-processing-modflow-based-models) | inglés           |
| TimML                           | <https://github.com/mbakker7/timml>                                                        | Modelado analítico flujo subterráneo multi-capa estacionario (Bakker). [PyPI](https://pypi.org/project/timml/)                                     | inglés           |
| TTim                            | <https://github.com/mbakker7/ttim>                                                         | Modelado transitorio multi-capa + Laplace (Bakker). [Sitio](http://mbakker7.github.io/ttim/)                                                       | inglés           |
| pywatershed                     | <https://www.usgs.gov/mission-areas/water-resources/pywatershed-a-hydrologic-model-python> | Modelo hidrológico USGS en Python puro                                                                                                             | inglés           |
| HyRiver / pygeohydro            | <https://docs.hyriver.io/>                                                                 | Stack 10 paquetes (NWIS, NLDAS-2, WQP). [PyGeoHydro](https://docs.hyriver.io/readme/pygeohydro.html)                                               | inglés           |
| hydrosignatures                 | <https://pypi.org/project/hydrosignatures/>                                                | FDC slope, baseflow Lyne&Hollick, exceedance. [Docs](https://hyriver.readthedocs.io/en/latest/readme/hydrosignatures.html)                         | inglés           |
| HydroBr                         | <https://github.com/wallissoncarvalho/hydrobr>                                             | Series hidrometeorológicas brasileñas (ANA, INMET, ONS)                                                                                            | inglés/portugués |
| hydropy                         | <https://github.com/stijnvanhoey/hydropy>                                                  | Hidrología sobre Pandas: recesión, peaks above percentile, storm extraction. [Docs](https://stijnvanhoey.github.io/hydropy/)                       | inglés           |
| pyAEMET                         | <https://github.com/Jaimedgp/pyAEMET>                                                      | **Cliente Python para AEMET OpenData (España): datos climatológicos diarios**                                                                      | español          |
| python-aemet                    | <https://github.com/pablo-moreno/python-aemet>                                             | Otra librería API AEMET. [PyPI](https://pypi.org/project/python-aemet/)                                                                            | español          |
| pySWATPlus                      | <https://github.com/swat-model/pySWATPlus>                                                 | Interfaz Python al modelo SWAT+                                                                                                                    | inglés           |
| Project Pythia AtmosCol radares | <https://projectpythia.org/AtmosCol-2023/radares/>                                         | Notebook (español) sobre radares meteorológicos                                                                                                    | **español**      |
| OWPHydroTools                   | <https://github.com/NOAA-OWP/data-service-notebooks>                                       | Herramientas NOAA-OWP para NWM streamflow + métricas                                                                                               | inglés           |

### Papers seminales en deep learning hidrológico

#### [Kratzert et al. 2018 — Rainfall–runoff modelling using LSTM networks (HESS)](https://hess.copernicus.org/articles/22/6005/2018/)

- **PDF:** <https://hess.copernicus.org/articles/22/6005/2018/hess-22-6005-2018.pdf>
- **Aporte:** primera aplicación sistemática de LSTM a 241 cuencas CAMELS. LSTM supera a SAC-SMA + Snow-17. Estándar de oro de DL en hidrología.
- **Notebook acompañante (pangeo):** <https://github.com/kratzert/pangeo_lstm_example>
- **Post:** <https://neuralhydrology.github.io/post/research/kratzert2018lstm/>

#### [Kratzert et al. 2019 — Towards learning universal, regional, and local hydrological behaviors via ML (HESS)](https://hess.copernicus.org/articles/23/5089/2019/)

- **arXiv:** <https://arxiv.org/abs/1907.08456>
- **Aporte:** introduce EA-LSTM (Entity-Aware LSTM). Un solo modelo entrenado en 531 cuencas CAMELS supera a modelos locales calibrados.
- **Código:** <https://github.com/kratzert/ealstm_regional_modeling>
- **Post:** <https://neuralhydrology.github.io/post/research/kratzert2019regional/>

#### [Klotz et al. 2022 — Uncertainty estimation with DL for rainfall–runoff modeling (HESS)](https://hess.copernicus.org/articles/26/1673/2022/)

- **arXiv:** <https://arxiv.org/abs/2012.14295>
- **Aporte:** 4 baselines DL para incertidumbre (Mixture Density Networks + MC Dropout)
- **Post:** <https://neuralhydrology.github.io/post/research/klotz2020uncertainty/>

#### [Frame et al. 2022 — Deep learning rainfall–runoff predictions of extreme events (HESS)](https://hess.copernicus.org/articles/26/3377/2022/hess-26-3377-2022.html)

- **PDF:** <https://hess.copernicus.org/articles/26/3377/2022/hess-26-3377-2022.pdf>
- **Aporte:** LSTM (incluida mass-conserving LSTM) mantiene precisión en eventos extremos no vistos, superando a Sacramento Model y US National Water Model. Conclusión sorprendente: añadir restricciones de balance de masa **empeora** las predicciones de extremos.

#### [Kratzert et al. 2019 — NeuralHydrology: Interpreting LSTMs in Hydrology](https://arxiv.org/abs/1903.07903)

- Interpretabilidad y visualización interna de LSTMs en hidrología.

#### [Kratzert et al. 2023 — Caravan dataset (Scientific Data)](https://www.nature.com/articles/s41597-023-01975-w)

- **Repo:** <https://github.com/kratzert/Caravan>
- **Zenodo:** <https://zenodo.org/records/10968468>
- **Post:** <https://neuralhydrology.github.io/post/research/kratzert2022caravan/>

#### [Nearing et al. 2021 — What Role Does Hydrological Science Play in the Age of Machine Learning? (WRR)](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2020wr028091)

- Reflexión sobre el rol de la ciencia hidrológica tradicional frente al ML.

#### [HESS 2024 — Large-sample hydrology, a few camels or a whole caravan?](https://hess.copernicus.org/articles/28/4219/2024/)

- Reflexión sobre límites y oportunidades de grandes datasets.

#### [EStreams (Scientific Data 2024)](https://www.nature.com/articles/s41597-024-03706-1)

- Dataset europeo integrado de streamflow + variables hidroclimáticas + landscape — incluye España.

### Recursos educativos abiertos (hidrología)

- [Pastas — Notebooks complementarios](https://github.com/pastas/pastas_research)
- [Bakker & Post — _Analytical Groundwater Modeling: Theory and Applications using Python_ (libro)](https://www.routledge.com/Analytical-Groundwater-Modeling-Theory-and-Applications-using-Python/Bakker-Post/p/book/9781138029392)
- [Python-Hydrology-Tools (curado por Raoul Collenteur)](https://github.com/raoulcollenteur/Python-Hydrology-Tools)
- [Open-Source-Hydrology-Tools (fork ampliado)](https://github.com/kbSSR/Open-Source-Hydrology-Tools)
- [AboutHydrology: Python resources for Hydrologists](http://abouthydrology.blogspot.com/2016/11/python-resources-for-hydrologists.html)
- [Python Resources for Earth Sciences (Javed Ali)](https://www.javedali.net/post/python-resources-for-earth-sciences/) — [Repo](https://github.com/javedali99/python-resources-for-earth-sciences)
- [Water Programming blog (Reed Group, Cornell)](https://waterprogramming.wordpress.com/)
  - [HyRiver para acceso a datos](https://waterprogramming.wordpress.com/2022/09/20/efficient-hydroclimatic-data-accessing-with-hyriver-for-python/)
  - [Packages for Hydrological Data Retrieval](https://waterprogramming.wpcomstaging.com/2019/07/08/packages-for-hydrological-data-retrieval-and-statistical-analysis/)
- [Hydro-Informatics eBook lectures](https://hydro-informatics.com/lectures/overview.html)
- [Project Pythia Foundations](https://projectpythia.org/) — [Cookbooks](https://projectpythia.readthedocs.io/)
- [Carleton — Time Series Analysis (SERC)](https://serc.carleton.edu/hydromodules/units/236434.html) — [Forecasting River Discharge](https://serc.carleton.edu/hydromodules/steps/287128.html)
- [pangeo_lstm_example (Kratzert)](https://github.com/kratzert/pangeo_lstm_example) — [Notebook directo](https://github.com/kratzert/pangeo_lstm_example/blob/master/LSTM_for_rainfall_runoff_modelling.ipynb)
- [NeuralHydrology multi-timescale tutorial](https://neuralhydrology.readthedocs.io/en/latest/tutorials/multi-timescale.html) — [Finetuning](https://neuralhydrology.readthedocs.io/en/latest/tutorials/finetuning.html)
- [Hatari Labs — Tutorial Completación de Datos Hidrológicos con IA / Keras (español)](https://gidahatari.com/ih-es/tutorial-completacion-datos-hidrologicos-inteligencia-artificial-python-keras)
- [Hydropy tutorial slides](https://github.com/stijnvanhoey/hydropy/blob/master/hydropy_tutorial.slides.html)
- [iAgua — Mejores links Python recursos hídricos (español)](https://www.iagua.es/blogs/gidahatari/mejores-links-aprender-python-recursos-hidricos)
- [Acolita — Lista recursos Python ciencias de la Tierra (español)](https://acolita.com/lista-de-recursos-python-para-las-ciencias-de-la-tierra/)

### Datos específicos para casos de estudio

#### Genil / Guadalquivir

- [SAIH CH Guadalquivir](https://www.chj.es/es-es/medioambiente/SAIH/Paginas/Inicio.aspx)
- [Anuario de Aforos MITECO](https://www.miteco.gob.es/en/cartografia-y-sig/ide/descargas/agua/anuario-de-aforos.html)
- [Estudio Quéntar y Canales (MDPI Water 2018)](https://www.mdpi.com/2073-4441/10/8/1038)
- [CAMELS-ES (incluye Guadalquivir)](https://zenodo.org/records/8428374)

#### Duero — piezometría

- [SARAI IGME — series 1950-2020](https://sarai.igme.es/index.php/tool-to-obtain-time-series-of-piezometry-and-precipitation-from-1950-to-2020-respectively-and-directly-from-miteco-and-aemet-for-any-point-in-spain-in-the-iberian-peninsula-and-the-balearic-islands/)
- [IGME portal oficial](https://www.igme.es/)
- [Communications Earth & Environment 2024 — niveles estables en SW Europa, incluye Duero](https://www.nature.com/articles/s43247-024-01554-w)
- [Caso de estudio Medina del Campo (Duero)](https://www.sciencedirect.com/science/article/pii/S2214581821000100)

---

## 5. ML/DL específico para series temporales

### Librerías Python

| Librería                      | URL                                              | Tipo                         | Cuándo usar                                                                                                                                                                                                        |
| ----------------------------- | ------------------------------------------------ | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Darts (Unit8)                 | <https://unit8co.github.io/darts/>               | Stats + ML + DL + Foundation | "Todo en uno": 60+ modelos (ARIMA, Prophet, N-BEATS, TFT, LSTM, XGBoost, Chronos-2, TimesFM). API tipo sklearn. Univariate y multivariate, probabilístico, covariables, anomalía. **Recomendado pedagógicamente.** |
| sktime                        | <https://www.sktime.net/>                        | ML clásico + pipelines       | Marco unificado para forecasting, clasificación, regresión, clustering. Sklearn-compatible. Útil para enseñar pipelines.                                                                                           |
| Aeon                          | <https://www.aeon-toolkit.org/>                  | ML clásico + DL              | Fork de sktime optimizado con numba. Clasificación, regresión, clustering, anomalía, segmentación, forecasting.                                                                                                    |
| NeuralForecast (Nixtla)       | <https://nixtlaverse.nixtla.io/neuralforecast/>  | DL (PyTorch)                 | NBEATS, NHITS, TFT, Informer, PatchTST, DilatedRNN, TCN, ESRNN, iTransformer, TimesNet. Exógenas y probabilístico.                                                                                                 |
| StatsForecast (Nixtla)        | <https://nixtlaverse.nixtla.io/statsforecast/>   | Estadística clásica          | AutoARIMA, AutoETS, AutoTheta, MSTL, TBATS, Croston. Muy rápido. Spark/Dask/Ray.                                                                                                                                   |
| MLForecast (Nixtla)           | <https://github.com/Nixtla/mlforecast>           | ML "global"                  | Feature engineering automático (lags, rolling, fechas) + cualquier sklearn-compatible (LightGBM, XGBoost).                                                                                                         |
| HierarchicalForecast (Nixtla) | <https://github.com/Nixtla/hierarchicalforecast> | Reconciliación jerárquica    | BottomUp, TopDown, MinTrace, ERM; reconciliación probabilística. **Útil para hidrología (cuencas/subcuencas).**                                                                                                    |
| NeuralProphet                 | <https://neuralprophet.com/>                     | DL interpretable             | Prophet + PyTorch; mantiene interpretabilidad con potencia DL.                                                                                                                                                     |
| Prophet (Meta)                | <https://facebook.github.io/prophet/>            | Aditivo bayesiano            | Series con estacionalidad fuerte, trends por tramos, holidays, faltantes. Baseline rápido.                                                                                                                         |
| GluonTS (AWS)                 | <https://ts.gluon.ai/>                           | DL probabilístico            | DeepAR, Transformer, WaveNet, PatchTST, iTransformer, TFT. Foco probabilístico.                                                                                                                                    |
| PyTorch Forecasting           | <https://pytorch-forecasting.readthedocs.io/>    | DL en PyTorch Lightning      | TFT, DeepAR, NBeats con dataset class robusto y Optuna.                                                                                                                                                            |
| tsai                          | <https://timeseriesai.github.io/tsai/>           | DL fastai/PyTorch            | InceptionTime, ROCKET, MiniRocket, TST, PatchTST, TSiT, XCM. Foco clasificación/regresión multivariada.                                                                                                            |
| TSLearn                       | <https://tslearn.readthedocs.io/>                | ML para TS                   | DTW, k-means con DTW/soft-DTW, SAX, kernel methods.                                                                                                                                                                |
| tsfresh                       | <https://tsfresh.readthedocs.io/>                | Feature extraction           | 794+ features automáticos; selección por hypothesis tests.                                                                                                                                                         |
| Kats (Meta)                   | <https://facebookresearch.github.io/Kats/>       | Toolkit completo             | Forecasting (10+ modelos), anomalía, changepoint, TSFeatures.                                                                                                                                                      |
| Functime                      | <https://docs.functime.ai/>                      | ML escalable (Polars)        | 100+ feature extractors, global forecasting con LightGBM/XGBoost. Paneles grandes.                                                                                                                                 |
| skforecast                    | <https://skforecast.org/>                        | Wrapper sklearn              | Convierte sklearn (RF, XGBoost, LightGBM, CatBoost) en forecasters. **Documentación con tutoriales en español (Joaquín Amat). Ideal para audiencia hispana.**                                                      |
| NeuralHydrology               | <https://neuralhydrology.github.io/>             | DL hidrológico               | LSTM/EA-LSTM/MTS-LSTM rainfall-runoff (PyTorch). **Imprescindible para nuestro enfoque.**                                                                                                                          |
| AutoTS                        | <https://github.com/winedarksea/AutoTS>          | AutoML                       | Búsqueda automática entre stats, ML y DL.                                                                                                                                                                          |
| Merlion (Salesforce)          | <https://github.com/salesforce/Merlion>          | Forecasting + anomalía       | Pipeline production-ready.                                                                                                                                                                                         |
| ADTK                          | <https://github.com/arundo/adtk>                 | Anomaly detection            | Reglas + métodos no supervisados.                                                                                                                                                                                  |

### Tutoriales destacados

- [Darts — Quickstart](https://unit8co.github.io/darts/quickstart/00-quickstart.html)
- [Darts — User Guide & Examples](https://unit8co.github.io/darts/examples.html)
- [sktime — Get Started](https://www.sktime.net/en/stable/get_started.html)
- [Aeon — Examples](https://www.aeon-toolkit.org/en/examples.html)
- [NeuralForecast — Getting Started](https://nixtlaverse.nixtla.io/neuralforecast/docs/getting-started/quickstart.html)
- [StatsForecast — Getting Started](https://nixtlaverse.nixtla.io/statsforecast/docs/getting-started/0_Installation.html)
- [MLForecast — Quickstart](https://nixtlaverse.nixtla.io/mlforecast/docs/quick_start_local.html)
- [HierarchicalForecast — Tutorials](https://nixtlaverse.nixtla.io/hierarchicalforecast/examples/introduction.html)
- [GluonTS — Quickstart](https://ts.gluon.ai/stable/tutorials/forecasting/quick_start_tutorial.html)
- [PyTorch Forecasting — TFT tutorial](https://pytorch-forecasting.readthedocs.io/en/stable/tutorials/stallion.html)
- [tsai — Intro to TS Classification (Colab)](https://timeseriesai.github.io/tsai/tutorials.html)
- [tsfresh — Quick Start](https://tsfresh.readthedocs.io/en/latest/text/quick_start.html) — [Rolling for forecasting](https://tsfresh.readthedocs.io/en/latest/text/forecasting.html)
- [Kats 101 basics notebook](https://github.com/facebookresearch/Kats/blob/main/tutorials/kats_101_basics.ipynb)
- [Prophet — Quick Start (Python)](https://facebook.github.io/prophet/docs/quick_start.html)
- [NeuralHydrology — Tutorials](https://neuralhydrology.readthedocs.io/en/latest/tutorials/index.html)
- [Kratzert — Pangeo LSTM rainfall-runoff notebook](https://github.com/kratzert/pangeo_lstm_example/blob/master/LSTM_for_rainfall_runoff_modelling.ipynb)
- [Forecasting: Principles & Practice — Pythonic Way](https://otexts.com/fpppy/)

### Papers seminales y benchmarks

#### [DeepAR (Salinas et al., Amazon, 2017)](https://arxiv.org/abs/1704.04110)

RNN/LSTM autoregresivo entrenado en muchas series relacionadas; verosimilitud paramétrica para forecasting probabilístico. Base del paradigma "global model". Implementación: GluonTS, PyTorch Forecasting, Darts.

#### [N-BEATS (Oreshkin et al., Element AI/Mila, ICLR 2020)](https://arxiv.org/abs/1905.10437)

Stack profundo fully-connected con backcast/forecast residual; ganó M4. Versión interpretable con bases trend/seasonality. Implementación: [NeuralForecast](https://nixtlaverse.nixtla.io/neuralforecast/models.nbeats.html), Darts.

#### [Temporal Fusion Transformer (Lim et al., Google, 2019)](https://arxiv.org/abs/1912.09363)

Atención + LSTM + variable selection + gating; multi-horizon probabilístico interpretable con covariables estáticas, pasadas y futuras. Implementación: [PyTorch Forecasting TFT](https://pytorch-forecasting.readthedocs.io/en/stable/api/pytorch_forecasting.models.temporal_fusion_transformer.TemporalFusionTransformer.html), Darts.

#### [Informer (Zhou et al., AAAI 2021 Best Paper)](https://arxiv.org/abs/2012.07436)

ProbSparse self-attention O(L log L), distilling, decoder generativo de una pasada para LSTF. <https://github.com/zhouhaoyi/Informer2020>

#### [Autoformer (Wu et al., Tsinghua, NeurIPS 2021)](https://arxiv.org/abs/2106.13008)

Descomposición series-trend dentro del transformer + Auto-Correlation Fourier. +38% sobre baselines. <https://github.com/thuml/Autoformer>

#### [FEDformer (Zhou et al., DAMO, ICML 2022)](https://arxiv.org/abs/2201.12740)

Atención en dominio frecuencial (Fourier/Wavelet) + descomposición; complejidad lineal. <https://github.com/MAZiqing/FEDformer>

#### [N-HiTS (Challu et al., AAAI 2023)](https://arxiv.org/abs/2201.12886)

Multi-rate pooling + hierarchical interpolation; ~20% mejor que transformers, 50× más rápido. [NeuralForecast NHITS](https://nixtlaverse.nixtla.io/neuralforecast/models.nhits.html).

#### [PatchTST (Nie et al., IBM, ICLR 2023)](https://arxiv.org/abs/2211.14730)

Patching + channel independence; pretraining auto-supervisado. Referencia actual en LTSF. <https://github.com/yuqinie98/PatchTST>

#### [Are Transformers Effective for TS Forecasting? — DLinear/NLinear (Zeng et al., AAAI 2023 Oral)](https://arxiv.org/abs/2205.13504)

Modelos lineales simples baten a transformers en muchos benchmarks. **Lectura crítica imprescindible.** <https://github.com/cure-lab/LTSF-Linear>

#### [TimesNet (Wu et al., ICLR 2023)](https://arxiv.org/abs/2210.02186)

Reformatea 1D-serie como 2D (intra/inter-período) + Inception 2D. SOTA en 5 tareas. <https://github.com/thuml/TimesNet> — [Time-Series-Library](https://github.com/thuml/Time-Series-Library)

#### [iTransformer (Liu et al., Tsinghua/Ant, ICLR 2024 Spotlight)](https://arxiv.org/abs/2310.06625)

Invierte los ejes — atención sobre variables (no tiempo), FFN sobre serie temporal. SOTA actual multivariate. <https://github.com/thuml/iTransformer>

#### Modelos fundacionales / foundation models

- **[TimeGPT-1 (Nixtla, 2023)](https://arxiv.org/abs/2310.03589)** — primer foundation model TS comercial; zero-shot. API: [docs.nixtla.io](https://docs.nixtla.io/).
- **[Chronos (Amazon Science, 2024)](https://arxiv.org/abs/2403.07815)** — tokeniza valores y entrena T5; open-source + Chronos-Bolt (250× más rápido). <https://github.com/amazon-science/chronos-forecasting>
- **[TimesFM (Google Research, ICML 2024)](https://arxiv.org/abs/2310.10688)** — 200M params, patched-decoder. <https://github.com/google-research/timesfm>
- **[Lag-Llama (Mila/U. Toronto, 2023)](https://arxiv.org/abs/2310.08278)** — decoder-only con lags. <https://github.com/time-series-foundation-models/lag-llama>

### Meta-recursos, awesome lists y competiciones

- [Time-Series-Library (THUML)](https://github.com/thuml/Time-Series-Library) — implementaciones SOTA bajo misma API (Autoformer, FEDformer, TimesNet, iTransformer, PatchTST, DLinear).
- [awesome-time-series (lmmentel)](https://github.com/lmmentel/awesome-time-series) — 138 paquetes, 24 datasets, 20 papers, 15 libros, 7 cursos.
- [Awesome-TimeSeries-SpatioTemporal-LM-LLM (qingsongedu)](https://github.com/qingsongedu/Awesome-TimeSeries-SpatioTemporal-LM-LLM) — LLMs/foundation models.
- [TSFpaper (ddz16)](https://github.com/ddz16/TSFpaper) — reading list de TSF/STF clasificada.
- [Awesome-time-series (cuge1995)](https://github.com/cuge1995/awesome-time-series).
- [Papers With Code — Time Series Forecasting](https://paperswithcode.com/task/time-series-forecasting).
- [Monash Time Series Forecasting Repository](https://forecastingdata.org/) — 30 datasets / 58 variantes (M1, M3, M4, NN5, tourism, KDD Cup 2018). [Paper](https://arxiv.org/abs/2105.06643). [Repo](https://github.com/rakshitha123/TSForecasting)
- [Makridakis Competitions — Wikipedia](https://en.wikipedia.org/wiki/Makridakis_Competitions) (M1 a M6).
- [M5 Forecasting (Kaggle, Walmart)](https://www.kaggle.com/competitions/m5-forecasting-accuracy).
- ["Learnings from Kaggle's Forecasting Competitions" (Bojer & Meldgaard)](https://arxiv.org/abs/2009.07701).
- [TFB: Time Series Forecasting Benchmark (PVLDB 2024)](https://github.com/decisionintelligence/TFB).
- [TSB-AD — Time-Series Anomaly Detection benchmark](https://thedatumorg.github.io/TSB-AD/) — 1070 series, 40 algoritmos. [TSB-UAD (VLDB 2022)](https://github.com/TheDatumOrg/TSB-UAD).
- [Kaggle Learn — Time Series](https://www.kaggle.com/learn/time-series).
- [Coursera — Sequences, Time Series and Prediction (deeplearning.ai)](https://www.coursera.org/learn/tensorflow-sequences-time-series-and-prediction).
- [Hyndman/Athanasopoulos/Nixtla — FPP the Pythonic Way](https://otexts.com/fpppy/) (gratis online). Versión R: [otexts.com/fpp3](https://otexts.com/fpp3/).
- [Kratzert et al. (HESS 2018) — Rainfall–runoff modelling using LSTM](https://hess.copernicus.org/articles/22/6005/2018/) — canónico de DL hidrológico.
- [NeuralHydrology JOSS paper (Kratzert et al. 2022)](https://joss.theoj.org/papers/10.21105/joss.04050).

---

## 6. Recursos en español

### Canales de YouTube

| Canal                               | URL                                                             | Contenido relevante                                                                                                                                                                                                                                                                                                 |
| ----------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dot CSV (Carlos Santana)            | <https://www.youtube.com/dotcsv>                                | Divulgación IA/DL en español. Sin playlist específica de series, pero explicaciones de RNN/LSTM, Transformers y foundation models excelentes para conceptos.                                                                                                                                                        |
| Codificando Bits (Miguel Sotaquirá) | <https://www.youtube.com/@codificandobits/playlists>            | Tutoriales prácticos en español: ["Pronósticos con Darts y redes neuronales"](https://www.youtube.com/watch?v=YCFuRuP_1ik); ["Pronósticos con redes LSTM"](https://codificandobits.com/blog/pronosticos-series-de-tiempo-redes-lstm/); playlist "Redes Neuronales Recurrentes". Blog: <https://codificandobits.com> |
| Ringa Tech                          | <https://www.youtube.com/@RingaTech>                            | ML/DL en español con Python. [Curso ML desde cero](https://www.youtube.com/watch?v=xyU2pzKTQE0).                                                                                                                                                                                                                    |
| AprendeIA con Ligdi González        | <https://www.youtube.com/c/AprendeIAconLigdiGonzalez/playlists> | [Playlist Machine Learning español](https://www.youtube.com/playlist?list=PLA050nq-BHwMr0uk7pPJUqRgKRRGhdvKb)                                                                                                                                                                                                       |
| Hektor Profe                        | <https://www.youtube.com/channel/UCtjAOyZmqDXO-Oz87cZnWgw>      | Cursos Python (fundamentos). Útil como prerrequisito. [Sitio](https://hektorprofe.net).                                                                                                                                                                                                                             |
| Píldoras Informáticas               | <https://www.pildorasinformaticas.es/course/curso-python/>      | [Curso Python extenso](https://www.youtube.com/c/pildorasinformaticas). Sin curso dedicado de series.                                                                                                                                                                                                               |
| Nixtla                              | <https://www.youtube.com/@Nixtla>                               | Equipo hispanohablante, charlas sobre StatsForecast/NeuralForecast/TimeGPT.                                                                                                                                                                                                                                         |
| PyData TV                           | <https://www.youtube.com/@PyDataTV>                             | Búsquedas "series temporales" devuelven charlas en español de PyData Madrid / Mallorca.                                                                                                                                                                                                                             |

### Cursos en español

#### [Modelos predictivos con aprendizaje automático — Universidad de los Andes (Coursera)](https://www.coursera.org/learn/modelos-predictivos-con-aprendizaje-automatico)

Incluye módulo de series de tiempo y predicción con ML.

#### [Modelos predictivos con Machine Learning — Universidad Anáhuac (Coursera)](https://www.coursera.org/learn/modelos-predictivos-con-machine-learning)

Implementación con Python.

#### [Predicción de Ventas Pronosticando Tendencias (Coursera project)](https://www.coursera.org/projects/prediccion-de-ventas-pronosticando-tendencias-en-google-sheets)

Project-based corto.

#### [Gestión de Ingresos — Universidad de Palermo (Coursera)](https://www.coursera.org/learn/gestion-de-ingresos)

Demand forecasting + pricing.

#### [Pronósticos de Series de Tiempo con Python — Udemy](https://www.udemy.com/course/pronosticos-de-series-de-tiempo-con-python/)

ARIMA, Prophet, ML/DL en español.

#### [Curso avanzado de Series Temporales con R y Python — Udemy (Gomila)](https://www.udemy.com/course/series-temporales/)

Multivariante, R y Python.

#### [Curso de series temporales multivariantes con R y Python — Udemy](https://www.udemy.com/course/curso-de-series-temporales-multivariantes-con-r-y-python/)

> 15 h, 10+ casos prácticos.

#### [Forecasting con Python: ARIMA y Prophet para Negocios — Udemy](https://www.udemy.com/course/forecasting-con-python-arima-y-prophet-para-negocios/)

#### [Curso Python: Series Temporales con Pandas — Udemy](https://www.udemy.com/course/curso-python-series-temporales-con-pandas/)

Resampling, rolling windows, descomposición, anomalías.

#### [Series temporales con Deep Learning (RNN, LSTM) y Prophet — MOOC.es](https://cursos.mooc.es/curso/series-temporales-con-deep-learning-rnn-lstm-y-prophet-1482)

Curso online gratuito.

#### [Curso Universitario en Series Temporales y Forecast — TECH](https://www.techtitute.com/es/escuela-de-negocios/curso-universitario/series-temporales-y-forecast-para-analisis-de-datos)

#### [Curso de análisis práctico de series temporales con R — Máxima Formación](https://www.maximaformacion.es/curso/curso-de-analisis-practico-de-series-temporales-con-r/)

#### [Introducción al Análisis de Series Temporales con R y Python — Universidad de Burgos](https://www.ubu.es/te-interesa/curso-introduccion-al-analisis-de-series-temporales-con-r-y-python)

#### [Predicción con series temporales — BertIA](https://bertia.es/formacion/prediccion-con-series-temporales/)

#### [Métodos de pronóstico de series de tiempo — UNAM (catálogo)](https://repositorio.unam.mx/contenidos/ficha/metodos-de-pronostico-de-series-de-tiempo-500070)

### Blogs y tutoriales en español

- [**Ciencia de Datos (Joaquín Amat)**](https://www.cienciadedatos.net/) — referencia esencial en español. Tutoriales destacados:
  - [Skforecast: forecasting de series temporales con Python, ML y scikit-learn](https://www.cienciadedatos.net/documentos/py27-forecasting-series-temporales-python-scikitlearn.html)
  - [Modelos ARIMA y SARIMAX con Python](https://www.cienciadedatos.net/documentos/py51-modelos-arima-sarimax-python)
  - [Forecasting con gradient boosting (XGBoost, LightGBM, CatBoost)](https://www.cienciadedatos.net/documentos/py39-forecasting-time-series-with-skforecast-xgboost-lightgbm-catboost)
  - [Forecasting global: múltiples series con ML](https://cienciadedatos.net/documentos/py44-multi-series-forecasting-skforecast-espa%C3%B1ol.html)
  - [Forecasting de demanda intermitente](https://www.cienciadedatos.net/documentos/py48-forecasting-demanda-intermitente)
  - [Forecasting de la demanda eléctrica](https://www.cienciadedatos.net/documentos/py29-forecasting-demanda-energia-electrica-python)
  - [Interpretabilidad en forecasting](https://www.cienciadedatos.net/documentos/py57-modelos-forecasting-interpretables)
  - [Prediction intervals con ML](https://cienciadedatos.net/documentos/py42-forecasting-prediction-intervals-machine-learning)
  - [Análisis comparativo de modelos globales](https://cienciadedatos.net/documentos/py53-modelos-forecasting-globales)
- [**skforecast** (Joaquín Amat — librería)](https://skforecast.org/) — [Repo](https://github.com/JoaquinAmatRodrigo/skforecast)
- [**ML Pills** (David)](https://mlpills.dev/category/series-temporales/) — píldoras semanales:
  - [Métodos de pronóstico](https://mlpills.dev/series-temporales/pronostico-de-series-temporales/)
  - [Limpieza de datos I](https://mlpills.dev/series-temporales/limpieza-de-datos-de-series-temporales/) y [II](https://mlpills.dev/series-temporales/limpieza-de-datos-de-series-temporales-ii/)
  - [ARIMA estacional](https://mlpills.dev/series-temporales/arima-estacional/)
  - [ARIMA-GARCH](https://mlpills.dev/series-temporales/modelos-arima-garch/)
- [**Aprende Machine Learning** (Juan Ignacio Bagnato)](https://www.aprendemachinelearning.com/):
  - [Pronóstico de Series Temporales con Redes Neuronales en Python](https://www.aprendemachinelearning.com/pronostico-de-series-temporales-con-redes-neuronales-en-python/)
  - [Pronóstico de Ventas con Redes Neuronales — Parte 2](https://www.aprendemachinelearning.com/pronostico-de-ventas-redes-neuronales-python-embeddings/)
- [**The Machine Learners** — intro series temporales](https://www.themachinelearners.com/series-temporales-intro/)
- [**Cyberclick — Numerical blog**: Predicciones de series temporales con ML](https://www.cyberclick.es/numerical-blog/data-science-predicciones-de-series-temporales-con-machine-learning)
- [**Tacos de Datos** — SARIMAX en Python](https://medium.com/tacosdedatos/herramientas-para-pron%C3%B3sticos-de-series-de-tiempo-en-python-parte-1-sarimax-89ff0a97b030)
- [**Ciencia y Datos** (Medium) — Modelos de Series de Tiempo en Python](https://medium.com/datos-y-ciencia/modelos-de-series-de-tiempo-en-python-f861a25b9677)
- [**Rodrigo López Briega** — Series de tiempo con Python](https://relopezbriega.github.io/blog/2016/09/26/series-de-tiempo-con-python/)
- [**Microsoft Learn (ES)** — Previsión de series temporales en Fabric](https://learn.microsoft.com/es-es/fabric/data-science/time-series-forecasting)
- [**Educa Open** — Series temporales: usos en ML](https://www.educaopen.com/digital-lab/blog/inteligencia-artificial/serie-temporal)

### Repositorios y materiales abiertos en español

- [**SeriesTemporalesEnCastellano** (FrancisArgnR)](https://github.com/FrancisArgnR/SeriesTemporalesEnCastellano) — compendio en castellano (componentes, ARIMA/SARIMA, suavizado, NN, autoencoders, LSTM).
- [**Diplomado Pronósticos y Series de tiempo con Python y R** (SciData)](https://github.com/scidatmath2020/Pron-sticos-y-series-de-tiempo).
- [**curso-series-temporales** (ECABestadistica)](https://github.com/ecabestadistica/curso-series-temporales).
- [**Platzi — Estadística y análisis de datos con Python**](https://github.com/platzi/fundamentos-estadistica-analisis-de-datos-python).

### Libros en español

- **Pronósticos, series de tiempo y regresión** — Bowerman, O'Connell & Koehler. Cengage/Thomson, 4.ª ed. 2007 (traducción). [Catálogo TESJO](http://biblioteca.tesjo.edu.mx/cgi-bin/koha/opac-detail.pl?biblionumber=4440)
- **Aprende Machine Learning en Español: Teoría + Práctica Python** — Juan Ignacio Bagnato. [Amazon](https://www.amazon.es/Aprende-Machine-Learning-Espa%C3%B1ol-Pr%C3%A1ctica/dp/8409258161) · [Leanpub](https://leanpub.com/aprendeml). Contiene capítulos sobre forecasting con NN.
- **Análisis de Series de Tiempo** — Oliva Vázquez, UNAM (apuntes): <http://herzog.economia.unam.mx/ea20201/MATEMATICAS/OLIVA_VAZQUEZ_B_SERIESDETIEMPO.pdf>
- **Apuntes UC3M (Andrés Alonso) — Introducción al Análisis de Series Temporales:** <https://halweb.uc3m.es/esp/personal/personas/amalonso/esp/seriestemporales.pdf>
- **Notas UCM (J.A. Martín) — Análisis de Series Temporales:** <https://www.ucm.es/data/cont/docs/518-2013-11-11-JAM-IAST-Libro.pdf>

### Charlas en eventos en español

- [Python España — canal YouTube](https://www.youtube.com/@PythonEspanaVideos) y [PyConES 2023 charlas](https://charlas.2023.es.pycon.org/pycones-2023/speaker/) — anualmente forecasting/series.
- [PyData Madrid](https://github.com/PyDataMadrid) y [PyData TV](https://www.youtube.com/@PyDataTV) — búsquedas "PyData Mallorca/Madrid series temporales".

---

## 7. Patrones observados y conclusiones para el currículo

### Resumen cuantitativo de la búsqueda

| Tipo de recurso                                      | Aprox. catalogados                  |
| ---------------------------------------------------- | ----------------------------------- |
| Cursos MOOC                                          | ~30                                 |
| Cursos universitarios                                | ~25 (15 anglosajones + 10 hispanos) |
| Libros (clásicos + hidrología)                       | ~16                                 |
| Librerías Python (forecasting + hidrología)          | ~40                                 |
| Papers seminales DL                                  | ~25 (foundation + DL hidrológico)   |
| Recursos en español (cursos, blogs, libros, canales) | ~40                                 |
| **Total con URL registrada**                         | **>175 fuentes únicas**             |

### Patrón 1 — La estructura "~20 h, modular, statistical → ML → DL" es estándar

Tres referencias muy cercanas a duración objetivo:

1. **DataCamp — Time Series with Python Track** (~20 h en 5 cursos modulares).
2. **Coursera — A Practical Approach to Timeseries Forecasting Using Python (Packt)** (~20 h, statistical + DL).
3. **Coursera — Sequences, Time Series and Prediction (DeepLearning.AI)** (~20 h, solo DL).

**Conclusión:** la división en 4 sesiones × 5 h con progresión estadísticos → ML → DL es coherente con lo que el mercado considera "completo".

### Patrón 2 — `skforecast` es la mejor puerta de entrada para audiencia hispana

- **Único framework con tutoriales nativos en español de alta calidad** (Joaquín Amat, cienciadedatos.net).
- API sklearn-compatible, soporta XGBoost/LightGBM/CatBoost, predicción multi-paso, intervalos.
- Comunidad activa, casos hidrométricos (demanda eléctrica → fácilmente adaptable a caudales).

**Conclusión:** considerar `skforecast` en la sesión 3 como puente ML clásico, junto a `statsforecast`/`mlforecast` de Nixtla. El alumno encuentra material de referencia inmediato en su idioma.

### Patrón 3 — DL hidrológico tiene una literatura específica madura

- **Kratzert et al. 2018 (HESS)** es el paper canónico (LSTM bate a SAC-SMA en CAMELS).
- **NeuralHydrology** es el framework de referencia (PyTorch, mantenido).
- **Mass-conserving LSTM** y trabajos de extremos (**Frame et al. 2022**) demuestran que DL puede superar a modelos físicos en eventos extremos — argumento didáctico potente para sesión 4.
- **CAMELS-ES** (Spanish CAMELS) es un dataset large-sample listo para usar con cuencas españolas.

**Conclusión:** la sesión 4 puede tener un bloque "DL en hidrología hoy" muy bien sustentado bibliográficamente. Imitable el pipeline de [`pangeo_lstm_example`](https://github.com/kratzert/pangeo_lstm_example) como demo.

### Patrón 4 — `Pastas` es virtualmente la única herramienta open-source madura para piezometría con respuesta a impulsos

- Creada y mantenida por TU Delft / Eawag / Artesia (Mark Bakker, Raoul Collenteur, Frans Schaars).
- Workshops impartidos por los propios autores (IAH, Australian Water School).
- Galería de ejemplos abundante (>15 casos reales).
- Papers de respaldo (Collenteur 2019, Bakker & Schaars 2019).

**Conclusión:** mantener Pastas como pieza central del bloque piezométrico (sesión 2). No hay alternativa equivalente.

### Patrón 5 — Foundation models para TS están entrando rápido al currículo

- Cursos de 2025–2026 (Marco Peixeiro, bootcamp Nixtla) ya incluyen **Chronos, TimesFM, TimeGPT**.
- Aún hay debate académico (`DLinear`/`NLinear` muestra que transformers no siempre baten a lineales).

**Conclusión:** dedicar un mini-bloque al final de la sesión 4 a probar `TimeGPT`/`Chronos` en zero-shot sobre el caudal del Genil. Útil para conectar con el "estado del arte" y abrir reflexión sobre cuándo (no) vale la pena.

### Patrón 6 — R sigue siendo dominante en la academia clásica

- Casi todos los cursos universitarios anglosajones citados (MIT, ETH, Oxford, Bristol, ETH, UNED, UC3M, UCM, UGR) usan R.
- fpp3 (Hyndman) es R; la versión Python (fpp the Pythonic Way, Nixtla) es reciente (2025).
- Mucho material clásico de series está documentado en R con menos paralelo en Python.

**Conclusión:** apoyarse en `statsmodels`, `pmdarima` y la suite Nixtla (`statsforecast`, `mlforecast`, `neuralforecast`) para reproducir conceptualmente el material R clásico. Citar fpp3 (R) como referencia conceptual y fpppy como referencia de código Python.

### Patrón 7 — Datasets españoles oficiales son accesibles vía API

- **SAIH Guadalquivir** (caudal): datos descargables, no requiere registro.
- **SARAI IGME** (piezometría): notebook listo para descargar series 1950–2020 cualquier punto peninsular.
- **AEMET OpenData** (meteorología): `pyAEMET`, `python-aemet`.
- **CAMELS-ES** (Caravan): 269 cuencas españolas con forcings y caudal preprocesados.

**Conclusión:** los datasets del curso (Genil + PZ0267014) son representativos y bien soportados por la infraestructura abierta. Mencionar CAMELS-ES como "siguiente paso" en la sesión 4 para alumnos motivados.

### Patrón 8 — Bibliografía sugerida

fpp3 (Hyndman, online gratis) + Nielsen (Practical Time Series, Python) + Hipel & McLeod (referencia hidrológica) + apuntes UC3M / UCM (en español).
