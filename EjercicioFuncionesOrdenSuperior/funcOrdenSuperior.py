# Implementar una función lambda que devuelva el área de un triángulo.

def baseEsDigito():
    base = input("Introduce la base del triángulo: ")
    if not base.isdigit():
      print("El valor introducido ha de ser numérico.")
      baseEsDigito()
    else: return base

def alturaEsDigito():
    altura = input("Introduce la altura del triángulo: ")
    if not altura.isdigit():
      print("El valor introducido ha de ser numérico.")
      baseEsDigito()
    else: return altura

base = int(baseEsDigito())
altura = int(alturaEsDigito())

areaTriangulo = lambda base, altura: (base*altura)/2
print(areaTriangulo(base, altura))


# Implementar una función, utilizando filter, que reciba una lista de números
# y devuelva una lista de los elementos que son múltiplos de 3.

print("-----------------------------------------------------------------------")
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

multiplos = list(filter(lambda multiplo_tres: multiplo_tres%3==0, lista))
print("Múltiplos de 3: " ,multiplos)


# Implementar una función, utilizando map, que reciba una lista de números
# y devuelva la lista con todos sus elementos multiplicados por 5.

print("-----------------------------------------------------------------------")
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

#calculo = lambda numero: numero *5

listaMultiplicada = list(map(lambda numero: numero *5, lista))

print("La lista multiplicada por 5: ", listaMultiplicada)