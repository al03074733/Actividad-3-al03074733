print("Ejercicio 15: Bajas en el inventario")
print("Sofia Eileen Lozano Serrano")
print("T03074733")
print()

# El inventario inicial
inventario = ["Air Max", "Jordan 1", "Converse", "Samba", "New Balance 550"]

while True:

    # Mostramos el inventario numerado
    print()
    print("===== INVENTARIO =====")
    for i in range(len(inventario)):
        print(i + 1, ".", inventario[i])

    numero = int(input("Número del producto a eliminar (0 para terminar): "))

    # ¿Escribió 0?
    if numero == 0:
        break

    # ¿El número es inválido?
    elif numero < 1 or numero > len(inventario):
        print("❌ Ese número no existe")

    else:
        # El número sí existe
        elegido = inventario[numero - 1]
        confirmar = input("¿Seguro que quieres eliminar " + elegido + "? (s/n): ")

        if confirmar == "s":
            del inventario[numero - 1]
            print("🗑️", elegido, "fue eliminado")
        else:
            print("👍 Baja cancelada")

    # ¿El inventario quedó vacío?
    if len(inventario) == 0:
        print("📭 El inventario quedó vacío")
        break

# Ya salimos del while
print()
print("Quedaron", len(inventario), "productos en el inventario")