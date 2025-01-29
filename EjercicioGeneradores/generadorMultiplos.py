# Implementar un generador que reciba un número 
# y devuelva los múltiplos de 3 de ese número.

num = input("Introduzca un número: ")
lim = input("Introduzca cuantos múltiplos de 3 del número anterior desea: ")

def generaMultiplos(limite, num):
    i = 0

    while i < limite:
        num *= 3
        yield num
        i += 1

multiplos = generaMultiplos(int(lim), int(num))

for multiplo in multiplos:
    print(multiplo)