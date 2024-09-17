
def inicializar_matriz_de(filas: int, columnas: int) -> list[list]:
    matriz = []

    for _ in range(filas):
        fila = [0] * columnas
        matriz.append(fila)
    return matriz

matriz = (inicializar_matriz_de(4,8))

for fila in range(len(matriz)):
    for columna in range(len(matriz)):
        print(matriz[fila][columna], end='')
    print(' ')

def quick_sort(lista_numerica: list[int]):

    if len(lista_numerica) < 2:
        return lista_numerica
    
    pivot = lista_numerica.pop()
    mas_chicos = []
    mas_grandes = []

    for numero in lista_numerica:
        if numero <= pivot:
            mas_chicos.append(numero)
        else:
            mas_grandes.append(numero)

    return quick_sort(mas_chicos) + pivot + quick_sort(mas_grandes)

lista_numerica_original = list(range(1000))

shuffle(lista_numerica_original)

print(lista_numerica_original[0:10])

inicio = time.time()
lista_ordenada = quick_sort(lista_numerica_original)
fin = time.time()

total = fin - inicio
print(lista_ordenada[:30])

print(f'Se tardo {total} tiempo')

