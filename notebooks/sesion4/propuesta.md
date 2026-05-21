# Propuesta ejercicio

## Ejercicio 1

Sobre el notebook `notebook/sesion3/sklearn.ipynb`, calcular la permutation importance del modelo y/o valores SHAP

## Ejercicio 2

1. Replicar el entrenamiento de la LSTM pero usando datso de 2018-2026 de caudal y lluvias (fuente SAIH) o datos propios (usar como base `notebook/sesion4/01_lstm_caudal_keras.ipynb`)
2. Probar modificando los hiper-parámetros de la LSTM:
    - Tamaño de ventana 30, 60, 365
    - Número unidades LSTM
    - Añadir más variables exógenas (temperatura, ...)
    - Calcular variables exógenas derivadas de la lluvia por ej. lluvia acumulada último mes
3. Modificar la LSTM para poder predecir a 1, 7 y 30 días


