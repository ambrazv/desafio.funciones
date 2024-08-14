def calcular_factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def calcular_productoria(lista):
    resultado = 1
    for numero in lista:
        resultado *= numero
    return resultado