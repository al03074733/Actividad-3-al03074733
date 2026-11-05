print("Ejercicio 3: Desbloquea tu celular")
print("Sofia Eileen Lozano Serrano")
print("T03074733")
print()

# Guardamos el PIN correcto
pin_correcto = "5867"

# Empezamos con 0 intentos
intentos = 0

# Mientras lleve menos de 3 intentos
while intentos < 3:
    pin = input("🔐 Escribe tu PIN de 4 números: ")

    if pin == pin_correcto:
        print("🔓 Celular desbloqueado")
        break
    else:
        intentos = intentos + 1
        restantes = 3 - intentos
        print("❌ PIN incorrecto. Te quedan", restantes, "intentos")

# Ya fuera del while
if intentos == 3:
    print("🔒 Celular bloqueado por 30 segundos")
    print("💡 Pista: son los números de la columna del centro")
else:
    print("📱 Tienes 3 notificaciones nuevas")

    cambiar = input("¿Quieres cambiar tu PIN? (s/n): ")

    if cambiar == "s":
        coinciden = False

        while coinciden == False:
            nuevo = input("Escribe tu nuevo PIN: ")
            confirmacion = input("Vuelve a escribirlo para confirmar: ")

            if nuevo == confirmacion:
                print("✅ Tu PIN se cambió correctamente")
                coinciden = True
            else:
                print("❌ No coinciden, intenta otra vez")
    else:
        print("👍 Tu PIN se queda igual")