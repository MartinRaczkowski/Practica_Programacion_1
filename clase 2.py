# 7 - crear una funcion con parametros que dado un numero, retorne si el numeor es primo o no
numero_a = input("numero")
def es_primo(numero_a: float) -> bool:
    contador_divisores = 2
    posible_divisor = 2
    while posible_divisor < numero_a:
        check_multiplo = numero_a % posible_divisor == 0
        if check_multiplo == True:
            contador_divisores += 1
            break
        posible_divisor += 1
    validar_es_primo = contador_divisores == 2
    return validar_es_primo

print(es_primo)