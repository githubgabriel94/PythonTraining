# Implementar una función que reciba dos números 
# y devuelva el máximo común divisor

n1 = input("Introduzca un numero superior a cero: ")
n2 = input("Introduzca un segundo número superior a cero: ")

def maximoComunDivisor(num1, num2):
    resto = 0
    while num1 % num2 != 0:
        resto = num1 % num2
        num1 = num2
        num2 = resto
    
    return num2

print(maximoComunDivisor(int(n1), int(n2)))