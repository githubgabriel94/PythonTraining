# Implementar una función que reciba tres números 
# y devuelva el máximo de tres valores

def mayorDeTres(num1, num2, num3):
    
    if num1 > num2 and num1 > num3:
        print("Numero 1 es el mayor")
    elif num2 > num1 and num2 > num3:
        print("Numero 2 es el mayor")
    elif num3 > num1 and num3 > num2:
        print("Numero 3 es el mayor")
    else:
        print("Dos o más números empatan en mayor tamaño")

mayorDeTres(22, 1, 2)