# Ejercicios — Sesión 1

Soluciones / pistas para los ejercicios propuestos en los notebooks 01, 02 y 03. Los snippets asumen que las celdas iniciales de cada notebook (`from cst import datos as ud`, carga de `caudal`, `lluvia_m`, `piezo`) ya se han ejecutado.

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

### 1.5 Zoom evento feb-2026 (SAIH)

```python
# Si HistSAIH.xlsx está descargado, ud.cargar_caudal_genil() devuelve la
# serie diaria del SAIH (2018-2026); el caudal antiguo del ROEA se carga
# aparte para comparar.
caudal_saih = ud.cargar_caudal_genil()
caudal_roea = ud.cargar_anuario_caudal(5020)   # 1913-2020

# Eventos
v85 = caudal_roea.loc["1985-01-15":"1985-03-15"]
v26 = caudal_saih.loc["2026-02-01":"2026-03-15"]

fig, axes = plt.subplots(1, 2, figsize=(11, 3.4), sharey=False)
axes[0].plot(v85.index, v85.values, color="#c2410c", lw=1.5, marker="o", ms=3)
axes[0].axhline(caudal_roea.quantile(0.95), color="grey", ls="--", lw=0.8)
axes[0].set_title(f"Feb-1985  · pico {v85.max():.0f} m³/s")

axes[1].plot(v26.index, v26.values, color="#0d9488", lw=1.5, marker="o", ms=3)
axes[1].axhline(caudal_saih.quantile(0.95), color="grey", ls="--", lw=0.8)
axes[1].set_title(f"Feb-2026  · pico {v26.max():.0f} m³/s")
for ax in axes:
    ax.set_ylabel("Caudal (m³/s)"); ax.grid(alpha=0.3)
plt.tight_layout()

print(f"1985: pico / P95(1913-2020) = {v85.max()/caudal_roea.quantile(0.95):.1f}×")
print(f"2026: pico / P95(2018-2026) = {v26.max()/caudal_saih.quantile(0.95):.1f}×")
```

> *Discusión:* el SAIH `A20_GENIL_TOCON` mide río abajo de Pinos-Genil (donde corta el ROEA 5020), por lo que las magnitudes no son directamente comparables. La comparación relativa al P95 de cada serie es la honesta. El evento de feb-2026 supera con creces el P95 reciente, pero el de 1985 sigue siendo el máximo histórico no-regulado.

### 1.6 Tres fuentes de lluvia diaria

```python
lluvia_saih = ud.cargar_lluvia_genil()   # SAIH A20_202, diaria 2018-2026
lluvia_era5 = ud.cargar_lluvia_genil_diaria(
    fecha_inicio="2018-01-01", fecha_fin="2024-12-31"
)                                         # Open-Meteo ERA5 sobre Pinos-Genil

df = pd.concat({"saih": lluvia_saih, "era5": lluvia_era5}, axis=1).dropna()
print(f"Periodo solapado: {df.index.min().date()} → {df.index.max().date()}  "
      f"({len(df)} días)")

for col in df:
    s = df[col]
    print(f"  {col:5s}  total={s.sum():7.0f} mm   "
          f"días >1 mm = {(s>1).sum():4d}   "
          f"max diario = {s.max():.1f} mm")

print(f"  correlación día-a-día: {df['saih'].corr(df['era5']):.2f}")
```

> *Discusión esperada:* la suma de ERA5 suele ser **mayor** porque el pixel de 25 km integra una zona con relieve (Sierra Nevada) más lluviosa que el punto del pluviómetro del valle. El número de "días lluviosos" también es mayor en ERA5: tiende a *manchar* eventos cortos. La correlación día-a-día ronda 0.5-0.7 — buena para tendencias, mediocre para eventos puntuales. Moraleja: usa ERA5 como **proxy regional**, no como sustituto del pluviómetro local.

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

### 2.5 Outliers en lluvia diaria

```python
lluvia = ud.cargar_lluvia_genil().dropna()
print(f"n={len(lluvia)}, fracción de ceros = {(lluvia==0).mean():.2%}")
print(f"q25={lluvia.quantile(0.25):.1f}  q50={lluvia.quantile(0.5):.1f}  "
      f"q75={lluvia.quantile(0.75):.1f}  q99={lluvia.quantile(0.99):.1f}  "
      f"max={lluvia.max():.1f}")

# 1) IQR clásico
q1, q3 = lluvia.quantile([0.25, 0.75])
iqr_out = lluvia > q3 + 1.5 * (q3 - q1)

# 2) MAD (mediana ± 3.5·MAD)
med = lluvia.median()
mad = (lluvia - med).abs().median() * 1.4826
mad_out = (lluvia - med).abs() > 3.5 * mad if mad > 0 else lluvia > 0

# 3) Hampel ventana 30 días
def hampel(s, w=30):
    m = s.rolling(w, center=True, min_periods=5).median()
    md = (s - m).abs().rolling(w, center=True, min_periods=5).median() * 1.4826
    return ((s - m).abs() > 3.5 * md.replace(0, np.nan)).fillna(False)
ham_out = hampel(lluvia, 30)

for nombre, mask in [("IQR", iqr_out), ("MAD", mad_out), ("Hampel", ham_out)]:
    print(f"{nombre:7s} marca {mask.mean()*100:5.2f}%  "
          f"(valores mínimo marcado = {lluvia[mask].min():.1f} mm)")
```

> *Discusión:* todos los métodos fallan **estrepitosamente** porque con tantos ceros la mediana, q25 y q75 son 0 (o casi). Eso hace que cualquier lluvia no-nula entre en la "cola" estadística y aparezca como outlier — incluyendo lluvias perfectamente normales de 5 mm. La distribución 0-inflada con cola pesada **no es la hipótesis** de estos métodos. Alternativas:
>
> ```python
> # (a) Trabajar en log(1+P) — comprime la cola, pero los ceros siguen pesando.
> # (b) Cuantil alto sobre días lluviosos:
> lluviosos = lluvia[lluvia > 1]
> umbral = lluviosos.quantile(0.999)
> print(f"P99.9 (días con P>1mm) = {umbral:.1f} mm — días por encima: {(lluvia>umbral).sum()}")
>
> # (c) Regla física: máximo histórico AEMET en Andalucía ≈ 800 mm/día.
> # Cualquier valor > 200 mm/día merece inspección manual, no descarte automático.
> ```

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

### 3.6 CCF diario SAIH lluvia→caudal

```python
caudal_d = ud.cargar_caudal_genil()    # SAIH diario A20_GENIL_TOCON
lluvia_d = ud.cargar_lluvia_genil()    # SAIH diario A20_202 (mismo cluster)
df = pd.concat({"P": lluvia_d, "Q": caudal_d}, axis=1).dropna()
print(f"Periodo: {df.index.min().date()} → {df.index.max().date()}  n={len(df)}")

lags = list(range(-5, 31))
ccf = [df["P"].corr(df["Q"].shift(-k)) for k in lags]

fig, ax = plt.subplots(figsize=(9, 3.4))
ax.bar(lags, ccf, width=0.85, color="#1f6f8b", alpha=0.8)
ax.axhline(0, color="grey", lw=0.5)
ax.axvline(0, color="grey", lw=0.5, ls="--")
ax.set_xlabel("Lag (días, positivo = lluvia precede caudal)")
ax.set_ylabel("Correlación")
ax.set_title("CCF diario lluvia→caudal · SAIH A20")
plt.tight_layout()

k_opt = lags[int(np.argmax(ccf))]
print(f"Lag óptimo: {k_opt} días  (corr = {max(ccf):.2f})")
```

> *Discusión esperada:* el pico aparece típicamente en **lag +1 a +5 días** — mucho más rápido y nítido que el lag mensual de 1-2 meses del ejercicio del notebook. La razón: aquí lluvia y caudal están en el **mismo punto físico** (cluster A20), mientras que el CCF mensual mezcla pluvio Iznájar (río abajo, mensual) con aforo Pinos-Genil (río arriba). La regulación de Iznájar todavía suaviza la cola: la correlación no cae a cero hasta 20+ días.

### 3.7 CCF lluvia-piezometría con ERA5 (Duero)

```python
# ERA5 diario en la coordenada del piezómetro PZ0267014 (Valladolid)
lluvia_duero = ud.cargar_lluvia_duero_diaria(
    fecha_inicio="2010-01-01", fecha_fin="2024-12-31"
)
lluvia_m = lluvia_duero.resample("MS").sum()
piezo_m  = ud.cargar_piezometria().resample("MS").mean()

df = pd.concat({"P": lluvia_m, "piezo": piezo_m}, axis=1).dropna()
print(f"Meses con dato: {len(df)}  ({df.index.min().date()} → {df.index.max().date()})")

lags = list(range(-3, 25))
ccf = [df["P"].corr(df["piezo"].shift(-k)) for k in lags]

fig, ax = plt.subplots(figsize=(9, 3.4))
ax.bar(lags, ccf, width=0.85, color="#0d9488", alpha=0.8)
ax.axhline(0, color="grey", lw=0.5); ax.axvline(0, color="grey", lw=0.5, ls="--")
ax.set_xlabel("Lag (meses, positivo = lluvia precede cota)")
ax.set_ylabel("Correlación")
ax.set_title("CCF lluvia ERA5 → cota piezométrica · PZ0267014")
plt.tight_layout()

k_opt = lags[int(np.argmax(ccf))]
print(f"Lag óptimo: {k_opt} meses  (corr = {max(ccf):.2f})")
```

> *Discusión esperada:* el lag óptimo depende de la **profundidad y conexión del acuífero**. En PZ0267014 (Duero medio, Renedo de Esgueva) aparece un máximo modesto en 1-6 meses con correlación baja (≈ 0.2). Razones del bajo valor:
>
> - La cota piezométrica responde a **bombeos agrícolas** y recarga lateral del río, no sólo a lluvia local.
> - El píxel ERA5 (~25 km) puede no capturar bien la lluvia efectiva sobre la zona de recarga.
> - Las mediciones del pozo son **irregulares** (mensual con huecos): tras alinear queda poco solapamiento útil.
>
> Comparando con el CCF lluvia→caudal del 3.6 (lag de días, corr 0.4), aquí el sistema es claramente más lento y peor explicado por la lluvia puntual. Esto motiva los modelos paramétricos de **Pastas** (sesión 2), donde la respuesta se modela con una función de transferencia (Gamma/exponencial) en lugar de un único lag puntual.
