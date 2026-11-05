print("Ejercicio 13: Mis juegos favoritos")
print("Sofia Lozano")
print("T03074733")
print()

# Creamos la lista con 5 juegos
juegos = ["Minecraft", "Roblox", "Fortnite", "FIFA", "Among Us"]

# Mostrar primero, último y tercero
print("🎮 Mi juego número 1:", juegos[0])
print("📂 El último de mi lista:", juegos[-1])
print("3️⃣ El tercero:", juegos[2])

# Mostrar cuántos juegos hay
print("📦 Tengo", len(juegos), "juegos favoritos")

# Mostrar lista numerada del 1 al 5
print()
print("===== MIS FAVORITOS =====")

for i in range(len(juegos)):
    print(i + 1, ".", juegos[i])

# Pedir un número del 1 al 5
numero = int(input("Escribe un número del 1 al 5: "))

# Mostrar el juego correspondiente
print("🎮 Elegiste:", juegos[numero - 1])