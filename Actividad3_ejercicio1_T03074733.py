print("Ejercicio 1: Inicia sesión en Roblox")
print("Sofia Eileen Lozano Serrano")
print("T03074733")
print()

# Guardamos el usuario y la contraseña correctos
usuario_correcto = "Sopona129"
contrasena_correcta = "R3dh4t34"

# Al inicio NO ha iniciado sesión
sesion_iniciada = False

# Repetir hasta que inicie sesión correctamente
while sesion_iniciada == False:
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")

    if usuario == usuario_correcto:
        if contrasena == contrasena_correcta:
            print("✅ ¡Bienvenido!", usuario, "!")
            sesion_iniciada = True
        else:
            print("❌ La contraseña es incorrecta")
    else:
        print("❌ Ese usuario no existe")

print("🎮 Cargando tus juegos...")