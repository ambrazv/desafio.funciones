# Definimos la lista de velocidades
velocidades = [
    25, 12, 19, 16, 11, 11, 24, 1, 14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
    14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2, 14, 23, 19, 23, 9, 18, 20, 22,
    14, 1, 10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5, 11, 10, 18, 10, 14, 5,
    23, 20, 23, 21
]

# Función para calcular el promedio de la lista de velocidades
def calcular_promedio(lista):
    return sum(lista) / len(lista)

# Función para encontrar las posiciones con velocidades por encima del promedio
def alertas_telematicas(lista):
    promedio = calcular_promedio(lista)
    alertas = [i for i, v in enumerate(lista) if v > promedio]
    return alertas

# Llamada a la función y mostrar las posiciones con alertas
if __name__ == "__main__":
    resultado = alertas_telematicas(velocidades)
    print(resultado)
