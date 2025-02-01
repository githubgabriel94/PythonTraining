# Implementar una función que recibe un archivo y un número N y devuelva
# las primeras N líneas del archivo.

from itertools import islice

archivo_texto=open("archivoNLineas.txt", "w")

x = 10
textoEjemplo = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."


def nextLineEveryXWords(text, x):
    words = text.split()
    for i in range(x, len(words), x):
        words[i] += "\n"
    return " ".join(words)

archivo_texto.write(nextLineEveryXWords(textoEjemplo, x))

archivo = archivo_texto=open("archivoNLineas.txt", "r")
def numeroLineas(archivo):
    count = 0
    lineas = list(archivo)
    for _ in lineas:
        count +=1
    
    return count

lineasTexto = numeroLineas(archivo)


def solicitaNLineas(lineasTexto):
        lineas = int(input("Introduce el numero de lineas que quieres ver del texto: "))
        if lineas > lineasTexto:
            print("El numero de lineas solicitadas excede las contenidas por el texto ", str(lineasTexto), ".")
            solicitaNLineas(lineasTexto)
        else: 
            print(lineas)
            return lineas
   
count = solicitaNLineas(lineasTexto)

def primerasNLineas(archivo, n):
    lines = list(islice(archivo, n))
    for line in lines:
        print(line.strip())

archivo = archivo_texto=open("archivoNLineas.txt", "r")
print("------------------------------------------------------------------")
primerasNLineas(archivo, count)
print("\n")