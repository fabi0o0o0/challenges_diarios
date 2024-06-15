# Pedir la cantidad de números al usuario
cantidad = int(input("¿Cuántos números va a ingresar?: "))

# Inicializar la lista
lista = []

# Verificar si la cantidad es válida
if cantidad <= 1:
    print("No se puede crear una lista ascendente con 1(un) número")
else:
    print("**********Empiece a cargar los números**********")
    for i in range(cantidad):
        numero = int(input("Ingrese el número: "))
        lista.append(numero)
    
    # Ordenar la lista en orden ascendente
    lista.sort()
    
    # Imprimir la lista ordenada
    print("Lista ordenada:", lista)
