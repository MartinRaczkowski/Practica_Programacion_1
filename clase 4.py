def calcular_factorial(numero):
    if numero == 0:
        resultado = 1
    else:
        resultado = numero * calcular_factorial(numero - 1)
    
    return resultado

print(calcular_factorial(6))

#otra manera de escribirlo 
def factorial(numero: int):
    if numero == 0 or numero == 1:
        return 1
    else:
        anterior = numero - 1
        return numero * factorial(anterior)


print(factorial(6))

#se ingresa la posicion del numero y te devuelve que numero es en la secuencia fibonacci
def fibonacci(numero: int) ->int:
    if numero <= 1:
        return numero
    else:
        ultimo = numero -1
        penultimo = numero -2
        return fibonacci(ultimo) + fibonacci(penultimo)
    
print(fibonacci(4))

#minimo comun divisor?
def mcd(numero_a: int, numero_b: int) -> int:
    if numero_b == 0:
        return numero_a
    else:
        modulo_a_b = numero_a % numero_b
        return mcd(numero_b, modulo_a_b)

minimo_comun_divisor = mcd(5, 10)

print(minimo_comun_divisor)

