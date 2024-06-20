import random

def obtener_eleccion_computadora():
    opciones = ['piedra', 'papel', 'tijeras']
    return random.choice(opciones)

def determinar_ganador(eleccion_usuario, eleccion_computadora):
    if eleccion_usuario == eleccion_computadora:
        return "Empate"
    elif (eleccion_usuario == 'piedra' and eleccion_computadora == 'tijeras') or \
         (eleccion_usuario == 'papel' and eleccion_computadora == 'piedra') or \
         (eleccion_usuario == 'tijeras' and eleccion_computadora == 'papel'):
        return "Ganaste"
    else:
        return "Perdiste"

def jugar_piedra_papel_tijeras():
    while True:
        eleccion_usuario = input("Elige piedra, papel o tijeras (o escribe 'salir' para terminar): ").lower()
        if eleccion_usuario == 'salir':
            break
        elif eleccion_usuario not in ['piedra', 'papel', 'tijeras']:
            print("Elección inválida. Por favor, elige piedra, papel o tijeras.")
            continue
        
        eleccion_computadora = obtener_eleccion_computadora()
        print(f"Tú elegiste: {eleccion_usuario}")
        print(f"La computadora eligió: {eleccion_computadora}")
        
        resultado = determinar_ganador(eleccion_usuario, eleccion_computadora)
        print(resultado)

jugar_piedra_papel_tijeras()
