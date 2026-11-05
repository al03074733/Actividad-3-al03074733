print("Ejercicio 4: La caja registradora de la cafetería")
print("Sofia Eileen Lozano Serrano")
print("T03074733")
print()

acumulado = 0
articulos = 0

seguir = True

while seguir:
    print("----- Agregar producto -----")
    producto = input("Nombre del producto (escribe terminar para cobrar): ")

    if producto == "terminar":
        seguir = False
    else:
        costo = int(input("Costo de " + producto + ": $"))
        piezas = int(input("Cantidad: "))

        importe = costo * piezas

        acumulado = acumulado + importe
        articulos = articulos + piezas

        print("🛒", piezas, "x", producto, "= $", importe)
        print("💲 Acumulado: $", acumulado)

print()
print("====== RESUMEN DE COMPRA ======")
print("Artículos:", articulos)
print("Total: $", acumulado)

if acumulado >= 200:
    acumulado = acumulado - 20
    print("⭐ Se aplicó un descuento de $20")
    print("Nuevo total: $", acumulado)

efectivo = int(input("Dinero recibido: $"))

while efectivo < acumulado:
    print("⚠️ Aún faltan $", acumulado - efectivo)
    efectivo = int(input("Ingresa nuevamente el dinero recibido: $"))

vuelto = efectivo - acumulado

print("✅ Compra pagada correctamente")
print("💸 Cambio: $", vuelto)
print("😊 Gracias por su visita")