def contar_letras_texto(texto: str) -> int:
    contador_caracteres = 0 
    
    for _ in texto:
        contador_caracteres += 1
    print(contador_caracteres)

palabra = "bienvenido a la UTN"
contar_letras_texto(palabra)

