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

ingreso = input(
    "¿Qué quieres calcular? Para factorial escribe 'fact', o 'prod', para productoria: "
)
if ingreso == "fact":
    numero = int(input("Ingresa un número para calcular factorial: "))
    resultado = calcular_factorial(numero)
    print(f"El factorial del {numero} es {resultado}")

elif ingreso == "prod":
    lista = input(
        "Ingrese una lista de números ej. 1,2,3,4, para calcular productoria: "
    )
    numeros = list(map(int, lista.split(",")))
    resultado = calcular_productoria(numeros)
    print(f"La productoria de {numeros} es {resultado}")
