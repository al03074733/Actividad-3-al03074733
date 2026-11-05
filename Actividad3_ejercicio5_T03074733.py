print("Ejercicio 5: El menú de tu proyecto CRUD")
print("Sofia Eileen Lozano Serrano")
print("T03074733")
print()

# Pedimos el nombre del sistema
nombre_sistema = input("¿Cómo se llama tu sistema? ")

# Contador de operaciones
operaciones = 0

# Menú principal
while True:
    print()
    print("=====", nombre_sistema, "=====")
    print("1. Altas")
    print("2. Bajas")
    print("3. Cambios")
    print("4. Consultas")
    print("5. Imprimir")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("➕ Aquí irán las ALTAS de tu proyecto")
        operaciones = operaciones + 1

    elif opcion == "2":
        print("🗑️ Aquí irán las BAJAS de tu proyecto")
        operaciones = operaciones + 1

    elif opcion == "3":
        print("✏️ Aquí irán los CAMBIOS de tu proyecto")
        operaciones = operaciones + 1

    elif opcion == "4":
        print("🔍 Aquí irán las CONSULTAS de tu proyecto")
        operaciones = operaciones + 1

    elif opcion == "5":
        print("🖨️ Aquí irá IMPRIMIR de tu proyecto")
        operaciones = operaciones + 1

    elif opcion == "6":
        seguro = input("¿Seguro que quieres salir? (s/n): ")

        if seguro == "s":
            print("👋 Hiciste", operaciones, "operaciones. ¡Hasta luego!")
            break
        else:
            print("👍 Regresando al menú...")

    else:
        print("❌ Opción no válida, elige del 1 al 6")