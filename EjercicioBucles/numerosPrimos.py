# Implementar una función que reciba un numero 
# y devuelva su descomposición en números primos

numero = input("Introduzca un número a descomponer: ")

def numerosPrimos(n):
    primos = []
    div = 2
    while n > 1:
        while n % div == 0:
            primos.append(div)
            n //= div
        div += 1
    return primos


print(numerosPrimos(int(numero)))