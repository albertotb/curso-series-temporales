Usando los datos de caudal + lluvia del repositorio o datos propios (si disponibles):
1. Dividir serie temporal + exógena (si disponible) en train test respetando años naturales
2. Crear matriz de diseño de una serie temporal mensual con 2 lags anteriores + variable exógena agregada de últimos 2 meses (si disponible) + mes del año codificado con sin/cos (cíclico)
3. Entrenar modelo RandomForest fijando unos hiper-parámetros razonables (500 arboles, max_depth=5)
4. Calcular MAE y MSE sobre conjunto de test