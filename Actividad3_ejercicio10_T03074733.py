print("Ejercicio 10: Tu playlist en el camión")
print("Sofia Eileen Lozano Serrano")
print("T03074733")
print()

# Nuestra playlist
playlist = [
    "Flowers",
    "Calm Down",
    "Ella Baila Sola",
    "Anti-Hero",
    "Tití Me Preguntó",
    "Daylight"
]

# Mostramos la playlist numerada
print("===== 🎧 MI PLAYLIST =====")

numero = 1
for cancion in playlist:
    print(numero, ".", cancion)
    numero = numero + 1

# Preguntamos qué canción saltar y dónde bajarse
saltar = input("¿Qué canción quieres saltar? ")
parada = input("¿En qué canción llegas a tu parada? ")

# Contador de canciones escuchadas
escuchadas = 0

# Recorremos la playlist
for cancion in playlist:

    # Si es la canción que queremos saltar
    if cancion == saltar:
        print("⏭️ Saltando", cancion)
        continue

    # Escuchamos la canción
    print("🎵 Escuchando", cancion)
    escuchadas = escuchadas + 1

    # Si llegamos a la parada
    if cancion == parada:
        print("🚌 ¡Llegaste a tu parada!")
        break

else:
    print("🎧 Escuchaste toda la playlist")

print("Canciones escuchadas:", escuchadas)