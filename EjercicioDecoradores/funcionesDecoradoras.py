# Implementar un decorador que convierte cualquier función unaria en
# un generador que recibe un valor incial.

def decoradorGenerador(fun):
    
    def funcionInterior(valorIni):
        valor = valorIni
        while True:
            yield fun(valor)
            valor += 1

    return funcionInterior

@decoradorGenerador
def generaPares(num):
    return num * 2

generador = generaPares(1)

for _ in range(10):
    print(next(generador))


# Implementar un decorador que calcula la n-ésima potencia de un valor
# sobre la operación op.

print("-------------------------")
def decoradorPotencia(n):
    
    def decorador(fun):
        
        def funInterior(valor):
            return fun(valor) ** n 
        
        return funInterior
    
    return decorador

@decoradorPotencia(2)
def op(valor):
    return valor + 1

print("Resultado: ", op(4))