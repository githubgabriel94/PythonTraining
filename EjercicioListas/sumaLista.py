# Implementar una función que reciba una lista 
# y devuelva la suma de los valores de la lista 

miLista=[1, 2, 3, 4, 5, 6, 7, 8, 9]

def sumaLista(list):

    total = 0

    for x in list:
        total += x

    return total

print(sumaLista(miLista))