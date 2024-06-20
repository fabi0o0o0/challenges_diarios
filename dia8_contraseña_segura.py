import string

def es_contrasena_valida(contrasena):
    if not (8 <= len(contrasena) <= 16):
        return False
    if not any(char.isdigit() for char in contrasena):
        return False
    if not any(char in string.punctuation for char in contrasena):
        return False
    return True

contrasena = input("Introduce una contraseña entre 8 y 16 caracteres, con al menos un número y un carácter especial: ")

if es_contrasena_valida(contrasena):
    print("La contraseña es válida y segura.")
else:
    print("La contraseña no cumple con los requisitos. Asegúrate de que tenga entre 8 y 16 caracteres, al menos un número y al menos un carácter especial.")
