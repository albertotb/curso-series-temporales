# Ejercicios — Sesión 1

Soluciones / pistas para los ejercicios propuestos en los notebooks 01, 02 y 03. Los snippets asumen que las celdas iniciales de cada notebook (`import utils_datos as ud`, carga de `caudal`, `lluvia_m`, `piezo`) ya se han ejecutado.

---

## 01 · Carga y exploración

### 1.1 Año más seco vs más húmedo

```python
q_anual = caudal.resample("YE-SEP").mean()
print("Más seco :", q_anual.idxmin().year, q_anual.min())
print("Más húmedo:", q_anual.idxmax().year, q_anual.max())
print("Ratio húmedo/seco:", q_anual.max() / q_anual.min())
```

> *Discusión:* las mayores diferencias suelen aparecer entre años de sequía severa (2004-05, 2017-18) y años torrenciales (1996-97, 2009-10). El ratio típico en el Genil regulado puede superar 10×.

### 1.2 Cobertura por década en `PZ0267014`

```python
piezo.groupby(piezo.index.year // 10 * 10).size()
piezo.index.to_series().diff().dt.days.describe()
```

> *Pista:* la cadencia es muy heterogénea. Antes de los 2000 las mediciones eran trimestrales o semestrales; con la red oficial se densifican a mensuales en los 2010.

### 1.3 P95 por mes

```python
q = caudal.dropna()
p95_mes = q.groupby(q.index.month).quantile(0.95)
p95_mes.plot.bar()
```

> *Discusión:* el P95 más alto suele caer en febrero-marzo (combinación de lluvia atlántica + deshielo temprano).

### 1.4 Mapa estaciones SAIH ↔ ROEA (reto)

```python
import matplotlib.pyplot as plt

est = ud.cargar_anuario_estaciones()
mask = est["cod_saih"].notna() & est["xetrs89"].notna()
sub = est[mask]
fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(sub["xetrs89"], sub["yetrs89"], c="#1f6f8b", s=30)
for _, r in sub.iterrows():
    ax.annotate(r["cod_saih"], (r["xetrs89"], r["yetrs89"]), fontsize=6, alpha=0.7)
ax.set_aspect("equal"); ax.set_title("Estaciones ROEA con equivalente SAIH (UTM ETRS89)")
```

---

## 02 · Limpieza y agregación

### 2.1 Hampel sensible a la ventana

```python
def hampel(serie, ventana):
    med = serie.rolling(ventana, center=True, min_periods=max(5, ventana // 4)).median()
    mad = (serie - med).abs().rolling(ventana, center=True,
                                       min_periods=max(5, ventana // 4)).median() * 1.4826
    z = (serie - med) / mad.replace(0, np.nan)
    return z.abs() > 3.5

for v in (7, 30, 90):
    out = hampel(caudal_limpio, v)
    print(f"ventana={v:3d}d → outliers={out.mean()*100:5.2f}%   "
          f"pico 1985 marcado: {out.loc['1985-02-10':'1985-02-13'].any()}")
```

> *Discusión:* con ventana = 7 días el filtro es agresivo y marca el pico real como outlier; con 90 días lo "ve" como excursión normal del entorno → la **ventana** importa mucho.

### 2.2 Imputación con tope

```python
def imputar_caudal(serie, gap_max=3):
    """Interpola linealmente sólo si el gap es < gap_max días."""
    return serie.interpolate("linear", limit=gap_max - 1, limit_area="inside")
```

> `limit_area="inside"` evita rellenar al inicio o al final de la serie.

### 2.3 Caudal máximo anual hidrológico

```python
q_max = caudal.resample("YE-SEP").max()
ax = q_max.plot(marker="o")
# Ajuste lineal grosero (sin tests):
import numpy as np
y = q_max.dropna().values; x = np.arange(len(y))
m, b = np.polyfit(x, y, 1)
print(f"Pendiente: {m:+.2f} m³/s por año")
```

> *Comentario:* el signo de la pendiente y su significancia depende del periodo elegido. Sin un test formal (Mann-Kendall) sólo es exploratorio.

### 2.4 Piezometría a mensual sin imputar

```python
mensual = piezo.resample("MS").mean()
print("Meses con dato:", mensual.notna().sum(), "/", len(mensual))
print("Cobertura:", mensual.notna().mean() * 100, "%")
```

> *Discusión:* dejamos los NaN tal cual. Para modelar más adelante (Pastas, sesión 2) el modelo trabaja con la estructura irregular sin necesidad de imputar.

---

## 03 · Descomposición y correlación

### 3.1 STL anual sobre serie diaria

```python
from statsmodels.tsa.seasonal import STL
diaria = caudal.loc["2010":"2020"].interpolate("linear", limit=3).dropna()
stl_d = STL(diaria, period=365, robust=True).fit()
```

> *Pista:* es bastante más lento (~10×). El residuo presenta más estructura porque el ciclo anual está mejor capturado pero los eventos sub-anuales no.

### 3.2 STL de log(caudal)

```python
import numpy as np
log_q = np.log(caudal_mensual.clip(lower=0.01))
stl_log = STL(log_q, period=12, robust=True).fit()
print("std resid lineal:", stl.resid.std())
print("std resid log   :", stl_log.resid.std())
```

> *Discusión:* en variables con amplitud proporcional al nivel (caudal típico), el log estabiliza la varianza del residuo y suele dejar un STL "más limpio".

### 3.3 ACF por décadas

```python
from statsmodels.graphics.tsaplots import plot_acf

fig, axes = plt.subplots(2, 2, figsize=(10, 6))
for ax, decada in zip(axes.flat, ["1980", "1990", "2000", "2010"]):
    s = caudal.loc[decada:str(int(decada)+9)].dropna()
    plot_acf(s, lags=60, ax=ax)
    ax.set_title(decada + "s")
plt.tight_layout()
```

> *Discusión:* si la estructura cambia, indica regímenes hidrológicos distintos (por ejemplo cambios en la regulación tras la entrada en servicio de un embalse).

### 3.4 CCF con otro pluviómetro

```python
otra_lluvia = ud.cargar_anuario_precip_mensual(5002)   # Bembézar
df = pd.concat({"lluvia": otra_lluvia, "caudal": caudal_mensual}, axis=1).dropna()
ccf = [df["lluvia"].corr(df["caudal"].shift(-k)) for k in range(-6, 13)]
```

> *Discusión:* Bembézar está en otra subcuenca; la correlación cae bruscamente. Útil para discutir que la elección del pluvio importa mucho.

### 3.5 Modelo naive de respuesta a impulso

```python
import numpy as np
df = pd.concat({"P": lluvia_m, "Q": caudal_mensual}, axis=1).dropna()
X = np.column_stack([df["P"].shift(1), df["P"].shift(2)])
y = df["Q"].values
mask = ~np.isnan(X).any(axis=1)
X, y = X[mask], y[mask]
coef, *_ = np.linalg.lstsq(X, y, rcond=None)
print("α (lag-1) =", coef[0], "  β (lag-2) =", coef[1])

# Baseline persistencia
naive = df["Q"].shift(1)
mae_naive = (df["Q"] - naive).abs().mean()
pred = X @ coef
mae_modelo = np.abs(y - pred).mean()
print(f"MAE persistencia: {mae_naive:.2f}   MAE impulso: {mae_modelo:.2f}")
```

> *Conclusión esperada:* la persistencia mensual ya es **un baseline muy fuerte** para caudales regulados; el modelo impulso-respuesta lineal a 2 lags suele empatar o mejorar ligeramente. Spoiler: en sesión 2 veremos que **Pastas** generaliza esto con funciones de respuesta paramétricas para piezometría.
