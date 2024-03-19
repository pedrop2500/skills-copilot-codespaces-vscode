import random

def jugar():
    opciones = ["piedra", "papel", "tijera"]
    puntuacion_jugador = 0
    puntuacion_ordenador = 0
    
    while True:
        try:
            opcion_jugador = input("Elige 1 para piedra, 2 para papel, 3 para tijera, o 4 para salir: ")
            
            if opcion_jugador == "4":
                break
            
            if opcion_jugador not in ["1", "2", "3"]:
                print("Error: opción inválida.")
                continue
            
            opcion_jugador = opciones[int(opcion_jugador) - 1]
            
            opcion_ordenador = random.choice(opciones)
            
            print("El ordenador eligió:", opcion_ordenador)
            
            if opcion_jugador == opcion_ordenador:
                print("Empate.")
            elif (opcion_jugador == "piedra" and opcion_ordenador == "tijera") or \
                 (opcion_jugador == "papel" and opcion_ordenador == "piedra") or \
                 (opcion_jugador == "tijera" and opcion_ordenador == "papel"):
                print("¡Ganaste!")
                puntuacion_jugador += 1
            else:
                print("Perdiste.")
                puntuacion_ordenador += 1
        
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario.")
            break
    
    print("Puntuación final:")
    print("Jugador:", puntuacion_jugador)
    print("Ordenador:", puntuacion_ordenador)

jugar()
