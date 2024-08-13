def filtrar_productos(precios, umbral, condicion="mayor"):
  """Filtra los productos de un diccionario según un umbral y una condición.

  Args:
    precios: Un diccionario con los productos y sus precios.
    umbral: El valor umbral para la comparación.
    condicion: La condición de comparación ("mayor" o "menor").

  Returns:
    Una lista con los nombres de los productos que cumplen la condición. """

  productos_filtrados = []
  for producto, precio in precios.items():
    if (condicion == "mayor" and precio > umbral) or (condicion == "menor" and precio < umbral):
      productos_filtrados.append(producto)
  return productos_filtrados

if __name__ == "__main__":
  import sys

  precios = {'Notebook': 700000, 'Teclado': 25000, 'Mouse': 12000, 'Monitor': 250000, 'Escritorio': 135000, 'Tarjeta de Video': 1500000}

  # Obtener argumentos de la línea de comandos
  umbral = int(sys.argv[1])
  condicion = "mayor" if len(sys.argv) == 2 else sys.argv[2]

  if condicion not in ["mayor", "menor"]:
    print("Lo sentimos, no es una operación válida")
  else:
    resultado = filtrar_productos(precios, umbral, condicion)
    print(f"Los productos {condicion} al umbral son: {', '.join(resultado)}")
