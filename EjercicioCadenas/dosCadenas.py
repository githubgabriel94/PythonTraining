# Implementar funciones que reciben dos cadenas de caracteres y:

cadena = input("Introduce una cadena de caracteres: ")
cadena2 = input("Introduce una segunda cadena de caracteres: ")

# Devuelve si la segunda cadena es una subcadena de la primera.

def esSubcadena(c, c2):
    if c2 in c:
        return "La segunda cadena es subcadena de la primera."
    else: return "La segunda cadena NO es subcadena de la primera."

print(esSubcadena(cadena, cadena2))

# Devuelve la cadena que sea anterior en orden alfabético.

def cadenaAnterior(c, c2):
    c = sorted(c)
    c2 = sorted(c2)

    if c < c2:
        return "La cadena anterior es: ", c
    else: return "La cadena anterior es: ", c2

print(cadenaAnterior(cadena, cadena2))