# Contar Vocales: Escribe un programa que cuente el número de vocales en una cadena dada.

def EsVocal(cadena):
    vocales = "aeiou"
    cont = 0

    for letra in cadena:
        if letra in vocales:
            cont += 1

    return cont

palabra = input("Ingrese una palabra: ").lower()
numero_vocales = EsVocal(palabra)
print(f"El número de vocales en la palabra es: {numero_vocales}")

