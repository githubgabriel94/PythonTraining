# Implementar una función que reciba un archivo de texto de origen 
# y uno de destino, de modo que para cada línea del archivo origen, 
# se guarde una línea cifrada en el archivo destino. El algoritmo de 
# cifrado a utilizar consiste en lo siguiente: cada carácter comprendido 
# entre la a y la z, se le suma 13 y luego se aplica el módulo 26, 
# para obtener un nuevo carácter.

archivoOrigen = open("origenADestino.txt", "w")

textoEjemplo = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

archivoOrigen.write(textoEjemplo)

archivoOrigen = open("origenADestino.txt", "r")

origen = archivoOrigen.read()

def transformArchivo(archivo):
    cifrado = []
    for caracter in archivo:
        if "a" <= caracter <= "z":
            nuevoCaracter = chr((ord(caracter) - ord("a") + 13) % 26 + ord("a"))
            cifrado.append(nuevoCaracter)
        elif "A" <= caracter <= "Z":
            nuevoCaracter = chr((ord(caracter) - ord("A") + 13) % 26 + ord("A"))
            cifrado.append(nuevoCaracter)
        else:
            cifrado.append(caracter)

    return "".join(cifrado)
            

archivoDestino = open("destino.text", "w")
print(transformArchivo(origen))
archivoDestino.write(transformArchivo(origen))