# Implementar una función que reciba una lista de tuplas y devuelva un diccionario donde las claves son los primeros elementos de las tuplas 
# y los valores una lista con los segundos elementos

claves = "Uno", "Dos", "Tres", "Cuatro", "Cinco"
valores = 1, 2, 3, 4, 5, 6, 7, 8, 9

listaDeTuplas = [(clave, valor) for clave in claves for valor in valores]


def miDiccionario(lista):
    diccionario = {}
    for clave, valor in lista:
        if clave in diccionario:
            diccionario[clave].append(valor)
        else:
            diccionario[clave] = [valor]

    return diccionario

diccionario = miDiccionario(listaDeTuplas)

print(diccionario)