# Implementar una función que reciba una cadena y devuelva un diccionario 
# con la cantidad de repeticiones de cada palabra en la cadena

cadena= input("Introduzca la cadena de palabras que desee: ")

palabras = cadena.split()

def diccionarioCadena(cadena):
    diccionario = {}
    for palabra in cadena:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else: diccionario[palabra] = 1

    print(diccionario)

diccionarioCadena(palabras)