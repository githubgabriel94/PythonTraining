# Implementar una representación con tuplas de la baraja francesa

import random

palos = "Picas", "Diamantes", "Treboles", "Picas"
cartas = 1, 2, 3, 4, 5, 6, 7, 8, 9, "Jota", "Reina", "Rey"

baraja = [(carta, palo) for palo in palos for carta in cartas]

def barajar(baraja):
    random.shuffle(baraja)
    return baraja

# Implementar una función que reciba cinco cartas de la baraja francesa
# y devuelva si tiene un poker o no (4 cartas con el mismo número)

def crearMano(barajada):
    mano = random.sample(barajada, 5)
    print(mano)
    return mano


def isPoker(mano):
    valores = [carta[0] for carta in mano]
    for valor in valores:
        if valores.count(valor) == 4:
            print("True")
            return True

    return False

baraja_barajada = barajar(baraja)
mano = crearMano(baraja_barajada)

while isPoker(mano) == False:
    baraja_barajada = barajar(baraja)
    mano = crearMano(baraja_barajada)