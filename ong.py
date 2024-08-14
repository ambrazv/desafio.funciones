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
