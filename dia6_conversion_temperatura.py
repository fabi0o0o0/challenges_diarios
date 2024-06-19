#Conversión de Temperatura: Escribe un programa que convierta una temperatura dada en grados Celsius a grados Fahrenheit.

def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

celsius = float(input("Introduce la temperatura en grados Celsius: "))

fahrenheit = celsius_a_fahrenheit(celsius)

print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")
