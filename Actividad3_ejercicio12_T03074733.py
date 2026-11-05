print("Ejercicio 12: Alta de productos con folio")
print("Sofia Eileen Lozano Serrano")
print("T03074733")
print()

# ¿Cuántos productos vamos a dar de alta?
cuantos = int(input("¿Cuántos productos vas a dar de alta? "))

# Aquí sumaremos el valor total del inventario
valor_total = 0

# Para cada producto
for numero in range(1, cuantos + 1):

    # Creamos el folio
    folio = "SNK" + str(numero)

    print()
    print("📝 Producto con folio", folio)

    nombre = input("Nombre: ")

    # Pedimos y validamos el precio
    precio = int(input("Precio: $"))

    while precio <= 0:
        print("❌ El precio debe ser mayor que 0")
        precio = int(input("Precio: $"))

    piezas = int(input("Piezas en bodega: "))

    # Calculamos el valor del producto
    valor = precio * piezas
    valor_total = valor_total + valor

    # Mostramos la ficha
    print("✅ Alta exitosa")
    print("Folio:", folio, "- Nombre:", nombre)
    print("Precio: $", precio, "- Piezas:", piezas, "- Valor: $", valor)

# Resumen final
print()
print("===== RESUMEN DEL INVENTARIO =====")
print("Productos dados de alta:", cuantos)
print("💰 Valor total del inventario: $", valor_total)