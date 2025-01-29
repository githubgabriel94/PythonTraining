# Implementar una función que reciba un diccionario y una clave
# y devuelva el valor contenido en el diccionario de esa clave.
# Si la clave no está, se generará un error de tipo ValueError
# y se mostrará un mensaje descriptivo.

diccionario = {1 : "Salamanca", 2 : "Madrid", 3 : "Badajoz"}
print(diccionario)

searchKey = int(input("Introduce una clave (1, 2, 3) para obtener una ciudad: "))

def claveEnDiccionario(dicc, key):
    if key in dicc:
        print(dicc[key])
    else: raise ValueError("Esta clave no se encuentra en el diccionario.")

claveEnDiccionario(diccionario, searchKey)