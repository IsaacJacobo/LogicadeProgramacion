def mostrar_menu_principal():
    print("Bienvenido al Juego del Ahorcado")
    print("Selecciona el modo de juego:")
    print("1. Adivinar Palabras")
    print("2. Modo Versus")
    opcion = input("Ingresa el número de tu elección: ")
    return opcion

def seleccionar_nivel_dificultad():
    print("Selecciona el nivel de dificultad:")
    print("1. Fácil")
    print("2. Medio")
    print("3. Difícil")
    nivel = input("Ingresa el número de tu elección: ")
    return nivel

def solicitar_nombre_jugador():
    nombre = input("Ingresa tu nombre: ")
    return nombre

def main():
    nombre_jugador = solicitar_nombre_jugador()
    print(f"Hola, {nombre_jugador}!")
    opcion = mostrar_menu_principal()
    
    if opcion == "1":
        nivel = seleccionar_nivel_dificultad()
        print(f"{nombre_jugador}, has seleccionado el nivel: {nivel}")
        # lógica para iniciar el juego
    elif opcion == "2":
        print("Modo Versus seleccionado")
        # lógica para el modo versus
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
