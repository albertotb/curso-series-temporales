# Ejercicios — Sesión 4

Soluciones / pistas a los ejercicios de los notebooks 01–03 de Sesión 4.

---

## 4.1 · LSTM Keras

### 1. GRU vs LSTM

```python
from keras.layers import GRU
m_gru = Sequential([Input(shape=(VENTANA, len(FEATS))), GRU(32), Dropout(0.2), Dense(1)])
m_gru.compile(optimizer='adam', loss='mse')
m_gru.fit(...)
```

> *Discusión:* GRU suele entrenar 20-30% más rápido y obtener RMSE similar. En datasets pequeños puede ganar por menos parámetros.

### 2. Ventanas largas

```python
for v in (60, 120, 365):
    X, y, idx = crear_ventanas(df_d, FEATS, 'caudal', ventana=v)
    # entrena, evalúa, anota tiempo + RMSE
```

> Con `v=365` capturas estacionalidad pero el dataset (N) cae y el modelo se ralentiza ~5×.

### 3. Calendario como feature

```python
df_d['sin_an'] = np.sin(2 * np.pi * df_d.index.dayofyear / 365.25)
df_d['cos_an'] = np.cos(2 * np.pi * df_d.index.dayofyear / 365.25)
FEATS_PLUS = ['caudal', 'lluvia', 'sin_an', 'cos_an']
```

> En ventanas cortas (< 90 días) las features de calendario ayudan; en ventanas largas (365d) la red ya "ve" el ciclo y aportan menos.

### 4. LSTM apilado

```python
Sequential([
    Input(shape=(VENTANA, len(FEATS))),
    LSTM(32, return_sequences=True),
    Dropout(0.2),
    LSTM(16),
    Dense(1),
])
```

> Cuidado con overfit: sube `Dropout(0.3)` y baja `EarlyStopping(patience=10)`.

### 5. Reto multi-paso (h=7)

**Opción MIMO** (la más simple):

```python
def crear_ventanas_mimo(df, features, target, ventana, h):
    X, y, idx = [], [], []
    vf = df[features].values; vt = df[target].values; f = df.index
    for i in range(len(vf) - ventana - h + 1):
        X.append(vf[i:i+ventana])
        y.append(vt[i+ventana:i+ventana+h])
        idx.append(f[i+ventana])
    return np.asarray(X), np.asarray(y), pd.DatetimeIndex(idx)

X, y, idx = crear_ventanas_mimo(df, FEATS, 'caudal', VENTANA, h=7)
model = Sequential([Input(shape=(VENTANA, len(FEATS))), LSTM(32), Dense(7)])
model.compile(optimizer='adam', loss='mse')
```

> Reporta RMSE por horizonte (h=1, 3, 7). El error crece con el horizonte.

---

## 4.2 · Comparación y NeuralHydrology

### 1. Ensemble simple

```python
# Mensual
ensemble = (pred_sx_m.values + lgb_mes.values + lstm_mes.values) / 3
print('Ensemble NSE:', nse(obs_mes.values, ensemble))
```

> Ensemble simple suele ganar al mejor individual por 2-5% en métricas hidrológicas.

### 2. Comparación diaria

```python
# RMSE diario sin agregar
rmse_lgb = float(np.sqrt(((y_te_d - pred_lgb_d) ** 2).mean()))
rmse_lstm = float(np.sqrt(((pd.Series(obs_lstm_d, index=idx_lstm) - pd.Series(pred_lstm_d, index=idx_lstm)) ** 2).mean()))
print(f'Diario  LightGBM: {rmse_lgb:.3f}   LSTM: {rmse_lstm:.3f}')
```

> LightGBM suele tener ventaja en el día a día por su gestión nativa de features no temporales (calendario, lluvia acumulada).

### 3. Reto — seq_length=365

```python
model = Sequential([Input(shape=(365, len(FEATS))), LSTM(64), Dropout(0.3), Dense(1)])
# Entrenamiento mucho más lento. Compensa si NSE >> sin él.
```

### 4. NeuralHydrology + CAMELS-ES

```bash
pip install neuralhydrology
# Descarga CAMELS-ES desde Zenodo
nh-run train --config-file config_5basins.yml
```

> Fuera del scope de la sesión presencial. Es ideal como proyecto extendido o TFM.

---

## 4.3 · Interpretabilidad y errores

### 1. SHAP sobre LSTM

```python
import shap
import tensorflow as tf

# Submuestra (SHAP es lento sobre LSTM)
sample_idx = np.random.choice(len(Xtr), 100, replace=False)
explainer = shap.GradientExplainer(model, Xtr[sample_idx])
sv = explainer.shap_values(Xte[:50])

# sv tiene shape (n_outputs, n_samples, ventana, n_features)
# Reducir agregando sobre la ventana:
sv_agg = np.abs(sv[0]).sum(axis=1)   # (50, n_features)
shap.summary_plot(sv_agg, feature_names=FEATS)
```

### 2. Error vs lluvia acumulada

```python
import seaborn as sns
df_plot = df_err.join(X_te['p_acum7d'])
sns.scatterplot(data=df_plot, x='p_acum7d', y='err', alpha=0.4)
```

### 3. Quintil más alto

```python
q80 = np.quantile(df_err['obs'], 0.8)
top = df_err[df_err['obs'] >= q80]
print('NSE top-20%:', nse(top['obs'], top['pred']))
```

> Típicamente NSE cae 0.2-0.4 puntos en el quintil alto. Es el quintil que más le importa al gestor de avenida.

### 4. Reto — ACF de los errores

```python
from statsmodels.graphics.tsaplots import plot_acf
plot_acf(df_err['err'].dropna(), lags=30)
```

> Si la ACF del error tiene picos, queda señal sin modelar. Es indicador para subir capacidad del modelo o añadir features.
