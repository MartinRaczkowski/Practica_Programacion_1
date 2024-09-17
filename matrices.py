matriz_datos = [
    ["pepe", "moni", "dardo", "paola"]
    [56, 42, 49, 18]
    [175, 168, 180, 160]
]

# matriz fila --> columna

fila = 0
columna = 2

matriz_datos[fila][columna] = 'coqui'

for fila in range(len(matriz_datos)):
    for columna in range(len(matriz_datos[fila])):
        dato = matriz_datos[fila][columna]
        