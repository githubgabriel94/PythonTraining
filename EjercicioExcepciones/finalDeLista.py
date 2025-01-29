# Implementar una función que reciba una lista y un elemento y
# devuelva una lista con el elemento añadiendo al final de la lista.
# Si el elemento ya existe en la lista se generará un error de tipo
# ValueError y se mostrará un mensaje descriptivo.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numero = int(input("Introduce un número para añadir a la lista: "))

def finalDeLista(li, n):
    if n in li:
        raise ValueError("El número introducido ya existe en la lista.")
    else: li.append(n)

    print(li)

finalDeLista(lista, numero)
