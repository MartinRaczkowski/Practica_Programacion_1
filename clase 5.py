lista_nombres_heroes = ["deadpool", "batman", "spiderman", "goku"]

for indice in range(len(lista_nombres_heroes)):
    nombre = lista_nombres_heroes[indice]
    print(indice, nombre)

for nombre in lista_nombres_heroes:
    print(nombre)

lista_nombres_heroes.append("saitama")

for nombre in lista_nombres_heroes:
    print(nombre)

    