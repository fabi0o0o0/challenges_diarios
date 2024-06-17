# Crear un Diccionario a partir de dos listas

# Inicializar listas vacías
lista1 = []
lista2 = []

# Pedir la cantidad de elementos
cantidad = int(input("¿Cuántos elementos tendrán ambas listas?: "))

# Llenar las listas con los datos proporcionados por el usuario
for i in range(cantidad):
    datos1 = input(f"De la Lista 1, ingrese el elemento nro {i + 1}: ")
    lista1.append(datos1)
    datos2 = input(f"De la Lista 2, ingrese el elemento nro {i + 1}: ")
    lista2.append(datos2)

print(lista1)
print(lista2)

# Crear el diccionario usando zip y dict
diccionario = dict(zip(lista1, lista2))

# Imprimir el diccionario resultante
print(diccionario)
