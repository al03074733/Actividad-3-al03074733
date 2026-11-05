print("Ejercicio 11: Buscador de la tienda de sneakers")
print("Sofia Eileen Lozano Serrano")
print("T03074733")
print()

# Inventario de la tienda
inventario = ["Air Max", "Jordan 1", "Converse", "Samba", "New Balance 550"]

# Contadores
busquedas = 0
encontrados = 0

# El buscador funciona hasta que escriban "salir"
while True:
    print()
    buscado = input("🔍 ¿Qué modelo buscas? (escribe salir para terminar): ")

    # Salir del programa
    if buscado == "salir":
        break

    # Contamos la búsqueda
    busquedas = busquedas + 1

    # Buscar en el inventario
    for modelo in inventario:

        if modelo == buscado:
            print("✅ ¡Sí tenemos", modelo, "!")
            encontrados = encontrados + 1
            break

    else:
        print("❌ No tenemos", buscado)
        print("👟 Te recomendamos estos modelos:")

        for modelo in inventario:
            print(" -", modelo)

# Resumen final
print()
print("===== RESUMEN =====")
print("Búsquedas:", busquedas)
print("Encontrados:", encontrados)
print("👋 ¡Gracias por visitar la tienda!")