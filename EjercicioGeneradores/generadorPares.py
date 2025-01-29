# Implementar un generador que devuelva los números pares.

limite = input("Introduzca número de pares deseados: ")

def generaPares(lim):
    num = 1

    while num < lim:
        yield num * 2
        num += 1

pares = generaPares(int(limite) + 1)

for numero in pares:
    
    print(numero)