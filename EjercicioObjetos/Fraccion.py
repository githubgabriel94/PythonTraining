from math import gcd

class Fraccion():

    def __init__(self, dividendo, divisor):
        self.dividendo = dividendo
        self.divisor = divisor
        self.simplificar()

    def __str__(self):
        return f"{self.dividendo}/{self.divisor}"

    def sumar(self, otra):
        dividendoSuma = self.dividendo * otra.divisor + otra.dividendo * self.divisor
        divisorSuma = self.divisor * otra.divisor
        return Fraccion(dividendoSuma, divisorSuma)

    def multiplicar(self, otra):
        dividendoMulti = self.dividendo * otra.dividendo
        divisorMulti = self.divisor * otra.divisor
        return Fraccion(dividendoMulti, divisorMulti)

    def simplificar(self):
        comunDivisor = gcd(self.dividendo, self.divisor)
        self.dividendo //= comunDivisor
        self.divisor //= comunDivisor


dividendo = int(input("Introduzca el dividendo de la primera fracción: "))
divisor = int(input("Introduzca el divisor de la primera fracción: "))

fraccion = Fraccion(dividendo, divisor)

dividendo2 = int(input("Introduzca el dividendo de la segunda fracción: "))
divisor2 = int(input("Introduzca el divisor de la segunda fracción: "))

fraccionOtra = Fraccion(dividendo2, divisor2)

print("\nPrimera fracción: ", fraccion)
print("Segunda fracción: ", fraccionOtra)
print("-------------------------------")
print("Suma: ", fraccion.sumar(fraccionOtra))
print("Multiplicar: ", fraccion.multiplicar(fraccionOtra))