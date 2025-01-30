# Implementar funciones que reciben una cadena de caracteres y:

cadena = input("Introduce una cadena de caracteres: ")

# Devuelva los dos primero caracteres.

def dosPrimerosCaracteres(c):
    return c[:2]

print("Los dos primeros caracteres: ", dosPrimerosCaracteres(cadena))

# Devuelva los tres últimos caracteres.

def tresUltimosCaracteres(c):
    return c[-3:]

print("Los tres ultimos caracteres: ", tresUltimosCaracteres(cadena))

# Devuelva la cadena cada dos caracteres.

def cadaDosCaracteres(c):
    return c[::2]

print("La cadena cada dos caracteres: ", cadaDosCaracteres(cadena))

# Devuelva la cadena en sentido inverso.

def sentidoInverso(c):
    
    inv = ""
    for letra in c:
        inv = letra + inv
    
    return inv

print("La cadena invertida: ", sentidoInverso(cadena))