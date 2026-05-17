# Ejercicios — Sesión 2

Soluciones / pistas a los ejercicios propuestos en los notebooks 01–04 de Sesión 2.

---

## 2.1 · SARIMAX y ETS sobre caudal

### 1. Forecast con lluvia perfecta

```python
exog_test_real = test['lluvia'].values.reshape(-1, 1)
fc_real = modelo.get_forecast(steps=len(test), exog=exog_test_real).predicted_mean
print('RMSE clima:', rmse(test['caudal'], media))
print('RMSE real :', rmse(test['caudal'], fc_real))
```

> *Discusión:* la mejora con lluvia perfecta cuantifica el techo del modelo. En cuencas naturales puede ser del 20-40%; en reguladas (Genil) menos, porque la regulación amortigua.

### 2. RMSE por horizonte

```python
for h in (1, 3, 6, 12):
    p = modelo.forecast(steps=h, exog=exog_test[:h]).iloc[-1]
    print(f'h={h:2d}  RMSE-paso-h={abs(p - test["caudal"].iloc[h-1]):.2f}')
```

> *Mejor:* hacer walk-forward de varios pasos y calcular RMSE por horizonte (lo verás en 04).

### 3. SARIMA sin exógena

```python
m_solo = SARIMAX(train['caudal'], order=order, seasonal_order=seas,
                 enforce_stationarity=False, enforce_invertibility=False).fit(disp=False)
print(f'AIC con lluvia : {modelo.aic:.1f}')
print(f'AIC sin lluvia : {m_solo.aic:.1f}')
```

> Si la lluvia es informativa el AIC baja al añadirla.

### 4. Modelo log

```python
y_log = np.log(train['caudal'] + 0.1)
m_log = SARIMAX(y_log, exog=exog_train, order=order, seasonal_order=seas).fit(disp=False)
# Cuidado: residuos normales en log != normales en escala original
```

### 5. Dos covariables (reto)

```python
exog2 = np.column_stack([
    train['lluvia'].shift(1).fillna(method='bfill'),
    train['lluvia'].shift(2).fillna(method='bfill'),
])
m_2x = SARIMAX(train['caudal'], exog=exog2, order=order, seasonal_order=seas).fit(disp=False)
```

> *Discusión:* en cuencas con respuesta lenta (regulada), el lag-2 puede aportar más que el lag-1.

---

## 2.2 · Prophet baseline

### 1. Multiplicativa

```python
m_mult = Prophet(yearly_seasonality=True, weekly_seasonality=False,
                  daily_seasonality=False, seasonality_mode='multiplicative')
m_mult.add_regressor('lluvia'); m_mult.fit(train)
```

> *Discusión:* en caudal con amplitud proporcional al nivel medio, multiplicativa suele ajustar mejor las crecidas. Pero los intervalos también crecen multiplicativamente — comprueba calibración.

### 2. Changepoints manuales

```python
cps = pd.to_datetime(['2005-07-01', '2017-09-01'])
m_cp = Prophet(changepoints=cps, ...)
```

### 3. Lluvia lag-2

```python
df['lluvia_lag2'] = df['lluvia'].shift(2)
m.add_regressor('lluvia_lag2')
```

### 4. Calibración de intervalos (reto)

```python
def cobertura(yhat_lower, yhat_upper, y_real, nivel=0.8):
    return np.mean((y_real >= yhat_lower) & (y_real <= yhat_upper))

# Compara con SARIMAX
```

> Esperado: cobertura ~ nivel teórico (80%). Si está muy por debajo, los intervalos son demasiado optimistas.

---

## 2.3 · Pastas piezometría

### 1. Otra rfunc

```python
for rfunc_cls in [ps.Gamma, ps.Exponential, ps.Hantush]:
    ml_x = ps.Model(piezo)
    ml_x.add_stressmodel(ps.StressModel(lluvia, rfunc=rfunc_cls(), name='r', settings='prec'))
    ml_x.solve(report=False)
    print(rfunc_cls.__name__, '→ NSE =', round(ml_x.stats.nse(), 3))
```

> *Discusión:* `Gamma` suele ganar por su flexibilidad (3 parámetros). `Exponential` (2 par.) puede ser mejor si el sistema es muy simple.

### 2. RechargeModel con ET₀ (Open-Meteo)

Añade `&daily=et0_fao_evapotranspiration` a la URL en `descargar_lluvia_openmeteo` (modifica el helper) o usa una llamada manual.

```python
import requests
url = 'https://archive-api.open-meteo.com/v1/archive'
r = requests.get(url, params={
    'latitude': 41.66, 'longitude': -4.63,
    'start_date': '1985-01-01', 'end_date': '2024-12-31',
    'daily': 'et0_fao_evapotranspiration',
    'timezone': 'Europe/Madrid',
}).json()
et0 = pd.Series(r['daily']['et0_fao_evapotranspiration'],
                index=pd.to_datetime(r['daily']['time']), name='et0')

rm = ps.RechargeModel(lluvia, et0, rfunc=ps.Exponential(),
                      recharge=ps.rch.Linear(), name='recarga')
ml_rch = ps.Model(piezo)
ml_rch.add_stressmodel(rm)
ml_rch.solve(report=False)
```

### 3. Otro pozo

```python
piezo2 = ud.cargar_piezometria('PZ0228005')  # otro código que aparezca en el catálogo
# Igual luego para cargar lluvia ERA5 en sus coords (lat/lon desde el Excel LISTADO_PUNTOS)
```

### 4. Calibración por trozos

```python
ml_train = ps.Model(piezo, name='train')
ml_train.add_stressmodel(ps.StressModel(lluvia, rfunc=ps.Gamma(), name='r', settings='prec'))
ml_train.solve(report=False, tmin='1985-01-01', tmax='2010-12-31')

# Predicción extendida hasta 2024
sim_ext = ml_train.simulate(tmin='1985-01-01', tmax='2024-12-31')
```

### 5. Reto: convolución manual

```python
from scipy.stats import gamma as gamma_dist

def respuesta_gamma(t, n, a):
    return gamma_dist.pdf(t, a=n, scale=a)

t = np.arange(0, 365 * 5)
theta = respuesta_gamma(t, n=1.0, a=180.0)
theta /= theta.sum()

P = lluvia.values
sim_manual = np.convolve(P, theta, mode='full')[:len(P)]
```

> Ajustar (n, a) por mínimos cuadrados respecto a las observaciones — útil para entender qué hace Pastas por dentro.

---

## 2.4 · Validación y comparación

### 1. Horizonte 3

```python
H = 3
for fecha in fechas_eval[:-H]:
    historico = df.loc[:fecha].iloc[:-1]
    # ... ajustar, predecir steps=H y guardar la predicción del paso H-ésimo
```

> Esperado: NSE cae con horizonte; SARIMAX/ETS suelen mantener mejor la estructura estacional que Prophet en horizontes largos sin recalibrar.

### 2. Bootstrap del NSE

```python
rng = np.random.default_rng(0)
def bootstrap_nse(o, s, B=1000):
    boot = []
    n = len(o)
    for _ in range(B):
        idx = rng.integers(0, n, size=n)
        boot.append(nse(o[idx], s[idx]))
    return np.percentile(boot, [2.5, 97.5])
```

### 3. Sólo crecidas

```python
mask_alta = obs > np.quantile(obs, 0.75)
for k, p in preds.items():
    print(k, 'NSE-crecidas:', nse(obs[mask_alta], p[mask_alta]))
```

> El error de pico suele empeorar drásticamente — los modelos clásicos infraestiman picos. Es exactamente la motivación de las sesiones 3 y 4.

### 4. Diebold-Mariano

```python
def diebold_mariano(e1, e2, h=1):
    d = e1 ** 2 - e2 ** 2
    n = len(d)
    dm = d.mean() / (d.std(ddof=1) / np.sqrt(n))
    from scipy.stats import t
    p = 2 * (1 - t.cdf(abs(dm), df=n - 1))
    return dm, p

e_sx = obs - preds['SARIMAX']
e_et = obs - preds['ETS']
dm, p = diebold_mariano(e_sx, e_et)
print(f'DM = {dm:.2f}  p = {p:.3f}')
```

### 5. Persistencia

```python
persistencia = df['y'].shift(12).loc[fechas_eval].values
print('Persistencia anual NSE:', nse(obs, persistencia))
```

> En cuencas con estacionalidad fuerte, `y_{t-12}` es difícil de batir. Si tu modelo no lo gana, repensar.

---

## 2.5 · Prophet — tuning sobre datos diarios SAIH

### 1. Lluvia diaria sin lag

```python
df['lluvia_0d'] = df['lluvia']   # sin acumulado, sin shift
# repetir grid usando 'lluvia_0d' en add_regressor
```

> *Discusión:* el RMSE empeora ~10-20 %. La respuesta del Genil al impulso de lluvia no es instantánea (hay tránsito + acuíferos) — `lluvia_7d.shift(1)` empaqueta esa memoria. Para Prophet importa más la elección del regresor que el `regressor_prior_scale`.

### 2. Sin regresor

```python
m = Prophet(yearly_seasonality=10, weekly_seasonality=False,
            daily_seasonality=False, changepoint_prior_scale=0.01)
m.fit(train[['ds', 'y']])
```

> El RMSE sube de ~2.2 a ~3.5: en daily la lluvia hace la mitad del trabajo. Útil para distinguir qué parte de la mejora viene de Prophet vs del input físico.

### 3. Fourier order

```python
grid['yearly_seasonality'] = [5, 10, 20]
```

> 20 sobreajusta el patrón anual de los años húmedos y empeora CV-RMSE; 5 infraajusta el doble pico marzo-abril/octubre. 10 (default) suele ser óptimo aquí — confirma la elección por defecto.

### 4. Reto · crecida feb 2026

```python
train_full = df[df['ds'] < pd.Timestamp('2026-02-01')]
test_flood = df[(df['ds'] >= '2026-02-01') & (df['ds'] < '2026-03-01')]
m, _, _ = fit_and_score({k: best[k] for k in grid})  # mejor del grid
fc = m.predict(test_flood[['ds', 'lluvia_7d']])
print('Pico real :', test_flood['y'].max(), 'm³/s')
print('Pico Prophet:', fc['yhat'].max(), 'm³/s')
```

> Prophet pronostica un pico de ~10-15 m³/s para un evento real de 312. La regresión lineal sobre lluvia + curva determinista **no extrapola** fuera del rango de entrenamiento. Justifica las sesiones 3-4: modelos no lineales (boosting, redes) pueden captar la relación lluvia → caudal en régimen de crecida si reciben features adecuados.

### 5. Discusión · ¿por qué el tuning manda aquí y no en mensual?

| | Mensual (slides) | Diario (este ejercicio) |
|---|---|---|
| n (train) | ~270 | ~2550 |
| Señal estacional vs ruido | dominada por ciclo anual claro | ciclo anual + estiaje + eventos |
| Sensibilidad a `cps` | baja (poca varianza intra-año) | alta (drought 2022-23 induce changepoints espurios si `cps>0.05`) |
| Mejora absoluta del tuning | 0.6 % | ~18 % |

> **Lección:** la falta de mejora con tuning en mensual no es una propiedad de Prophet, es una propiedad del *problema*. En agregaciones bajas la estructura es tan simple que cualquier configuración razonable funciona. En daily, los priors importan.
