# Ejercicios — Sesión 3

Soluciones / pistas a los ejercicios propuestos en los notebooks 01–03 de Sesión 3.

---

## 3.1 · Feature engineering y baseline

### 1. Lasso vs Ridge

```python
from sklearn.linear_model import Lasso
f_lasso = ForecasterRecursive(regressor=Lasso(alpha=0.05), lags=LAGS)
f_lasso.fit(y=y_train, exog=X_train[exog_cols])
# Inspecciona coeficientes:
coef_lasso = pd.Series(f_lasso.regressor.coef_,
                       index=list(f_lasso.lags_names) + exog_cols)
print('Lasso descarta:', (coef_lasso == 0).sum(), 'features de', len(coef_lasso))
```

> *Discusión:* Lasso suele dejar 5–10 features no nulos. Si Ridge usaba 30+, Lasso simplifica radicalmente; el RMSE puede subir un 5-10% pero gana interpretabilidad.

### 2. Ablation

```python
configs = {
    'sólo lags':       (LAGS, None),
    'lags + lluvia':   (LAGS, ['p_acum7d', 'p_acum14d', 'p_acum30d']),
    'todo':            (LAGS, exog_cols),
}
for nombre, (lags, cols) in configs.items():
    f = ForecasterRecursive(regressor=Ridge(alpha=1), lags=lags)
    exog = X_train[cols] if cols else None
    f.fit(y=y_train, exog=exog)
    p = f.predict(steps=len(y_test), exog=X_test[cols] if cols else None)
    print(f'{nombre:20s}  RMSE={rmse(y_test, p):.2f}')
```

### 3. Fourier orden 2

```python
out['sin_an2'] = np.sin(4 * np.pi * idx.dayofyear / 365.25)
out['cos_an2'] = np.cos(4 * np.pi * idx.dayofyear / 365.25)
```

> En el Genil con régimen pluvio-nival, orden 2 capta la doble onda (lluvias invernales + deshielo primaveral).

### 4. Polinómicas e interacciones

```python
df_feat['q_lag1_sq'] = df_feat['q_lag1'] ** 2
df_feat['p_x_doy'] = df_feat['p_acum7d'] * df_feat['sin_an']
```

> Las interacciones manuales suelen ser inferiores a lo que XGBoost/LightGBM aprenden solos. Pero ayudan a Ridge.

### 5. Reto — Recursive vs Direct

```python
from skforecast.direct import ForecasterDirect
f_dir = ForecasterDirect(regressor=Ridge(alpha=1), lags=LAGS, steps=7)
f_dir.fit(y=y_train, exog=X_train[exog_cols])
p_dir = f_dir.predict(steps=7, exog=X_test[exog_cols].iloc[:7])
# Compara con recursivo h=7
```

> Direct suele ganar en h=3-30 pero requiere h modelos entrenados.

---

## 3.2 · RF, XGBoost, SHAP

### 1. Tuning con TimeSeriesSplit

```python
from skforecast.model_selection import grid_search_forecaster, TimeSeriesFold

cv = TimeSeriesFold(initial_train_size=2000, steps=30, refit=False)
grid = {'n_estimators': [200, 500], 'learning_rate': [0.03, 0.05, 0.1],
        'num_leaves': [15, 31, 63]}
res = grid_search_forecaster(
    forecaster=f_lgb, y=y_train, exog=X_train,
    param_grid=grid, cv=cv, metric='mean_absolute_error',
    return_best=True, show_progress=False,
)
```

### 2. Quantile regression

```python
f_q90 = ForecasterRecursive(
    regressor=lgb.LGBMRegressor(objective='quantile', alpha=0.9,
                                 n_estimators=300, verbose=-1, random_state=0),
    lags=LAGS,
)
f_q90.fit(y=y_train, exog=X_train)
p_q90 = f_q90.predict(steps=len(y_test), exog=X_test)
print('Cobertura por arriba (% obs <= q90):',
      (y_test.values <= p_q90.values).mean())
```

> Cobertura cercana a 0.9 → bien calibrado.

### 3. Sin lluvia

```python
X_no_p = X_train[['sin_an', 'cos_an']]
f_no_p = ForecasterRecursive(regressor=lgb.LGBMRegressor(...), lags=LAGS)
f_no_p.fit(y=y_train, exog=X_no_p)
```

> En cuencas reguladas el modelo sin lluvia puede perder solo 5-15% RMSE — la regulación amortigua.

### 4. NSE de todos

```python
def nse(o, s):
    o, s = np.asarray(o), np.asarray(s)
    return 1 - np.sum((o - s) ** 2) / np.sum((o - o.mean()) ** 2)

for n, p in preds.items():
    print(f'{n:10s}  NSE={nse(y_test, p):.3f}')
```

### 5. Reto — ensembling

```python
ensemble = (preds['LightGBM'].values + preds['XGBoost'].values) / 2
# o con pesos optimizados sobre validation
print('Ensemble RMSE:', rmse(y_test, ensemble))
```

> A menudo el ensemble simple gana al mejor individual por un 2-5%.

---

## 3.3 · Backtesting

### 1. Refit=True

```python
cv_refit = TimeSeriesFold(initial_train_size=n_train, steps=30, refit=True)
metrica, predicciones = backtesting_forecaster(
    forecaster=forecaster, y=y, exog=X_exog, cv=cv_refit,
    metric='mean_absolute_error', show_progress=False,
)
```

> Mucho más lento (reajusta en cada paso) pero realista. La diferencia con `refit=False` es la señal de cuánto deriva el modelo en producción.

### 2. Distintos horizontes

```python
for h in (1, 7, 30):
    cv = TimeSeriesFold(initial_train_size=n_train, steps=h, refit=False)
    m, _ = backtesting_forecaster(forecaster, y=y, exog=X_exog, cv=cv,
                                  metric='mean_absolute_error', show_progress=False)
    print(f'h={h:3d}  MAE={m.iloc[0,0]:.3f}')
```

### 3. Quantile en backtest

> Ver receta en 3.2 ejercicio 2. Comparar `sim.max() - obs.max()` (error de pico) con el modelo de la media.

### 4. Comparar con Sesión 2

```python
# Agregar predicciones diarias de LightGBM a mensual y comparar con SARIMAX 2.4
sim_mensual = pd.Series(sim, index=predicciones.index).resample('MS').mean()
obs_mensual = pd.Series(obs, index=predicciones.index).resample('MS').mean()
```

### 5. Reto — Conformal

```python
# Conformal calibration sobre la validation (últimos 365 días antes del test)
val_idx = (y.index >= '2017-01-01') & (y.index < '2018-01-01')
preds_val = forecaster.predict(steps=val_idx.sum(),
                               exog=X_exog.loc[val_idx])
err_val = (y[val_idx] - preds_val).abs()
q90 = np.quantile(err_val, 0.9)
print(f'IC 90% = ± {q90:.2f} m³/s alrededor de la predicción')
```

> Garantiza cobertura ≥ 90% en el test si la distribución del error es estable. La asunción se llama *exchangeability* y se rompe levemente en series con tendencia.
