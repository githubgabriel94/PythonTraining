# Implementar un script en Python que permita gestionar un conjunto
# de contadores. El usuario proporcionará el nombre del contador como 
# argumento en la línea de comandos incrementándose este contador y 
# mostrándose su valor actual. Para almacenar los valores actuales de 
# los contadores se utilizará un solo archivo Json.

import os
import json

file = "contadores.json"

def cargar():
    if os.path.exists(file):
        readFile = open(file, "r")
        return json.load(readFile)
    return {}

def guardar(contadores):
    writeFile = open(file, "w")
    json.dump(contadores, writeFile)

def incrementar(contador):
    contadores = cargar()
    if contador in contadores:
        contadores[contador] += 1
    else:
        contadores[contador] = 1
    guardar(contadores)
    return contadores[contador]

contador = input("Introduzca el nombre de un contador (nuevo/existente): ")
valor = incrementar(contador)
print("El valor de ", contador, "es actualmente: ", valor)