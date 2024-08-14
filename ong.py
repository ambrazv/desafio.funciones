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


def calcular(fact_1, prod_1, fact_2):
    factorial_1 = calcular_factorial(fact_1)
    print(f"El factorial de {fact_1} es {factorial_1}")

    productoria = calcular_productoria(prod_1)
    print(f"La productoria de {prod_1} es {productoria}")

    factorial_2 = calcular_factorial(fact_2)
    print(f"El factorial de {fact_2} es {factorial_2}")


# Genero los input para el usuario (niño/a)
fact_1 = int(input("Ingresa un número para calcular la primera factorial: "))
prod_1 = input(
    "Ingresa la lista de números para calcular la productoria (separados por coma): "
)
fact_2 = int(input("Ingresa el número para calcular la segunda factorial: "))

prod_1 = list(map(int, prod_1.split(",")))

calcular(fact_1, prod_1, fact_2)
