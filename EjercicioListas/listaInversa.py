# Implementar una función que reciba una lista 
# y devuelva la lista inversa de la lista

miLista=[1, 2, 3, 4, 5, 6, 7, 8, 9]

def listaInversa(list):
    listInv = []

    for x in reversed(list):
        listInv.append(x)

    return listInv

print(listaInversa(miLista[:]))