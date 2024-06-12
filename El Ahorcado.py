def main():
    nombre_jugador = solicitar_nombre_jugador()
    print(f"Hola, {nombre_jugador}!")
    opcion = mostrar_menu_principal()

    if opcion == "1":
        nivel = seleccionar_nivel_dificultad()
        if nivel:
            print(f"{nombre_jugador}, has seleccionado el nivel: {nivel}")
        else:
            print("Opción no válida")
    elif opcion == "2":
        print("Modo Versus seleccionado")
        # Espacio para desarrollar modo versus 
    else:
        print("Opción no válida")


def mostrar_menu_principal():
    print("Bienvenido al Juego del Ahorcado")
    print("Selecciona el modo de juego:")
    print("1. Adivinar Palabras")
    print("2. Modo Versus")
    opcion = input("Ingresa el número de tu elección: ")
    if opcion in ["1", "2"]:
        return opcion
    else:
        return None

def seleccionar_nivel_dificultad():
    print("Selecciona el nivel de dificultad:")
    print("1. Fácil")
    print("2. Medio")
    print("3. Difícil")
    nivel = input("Ingresa el número de tu elección: ")
    if nivel in ["1", "2", "3"]:
        return nivel
    else:
        return None

def solicitar_nombre_jugador():
    nombre = input("Ingresa tu nombre: ")
    return nombre

if __name__ == "__main__":
    main()
