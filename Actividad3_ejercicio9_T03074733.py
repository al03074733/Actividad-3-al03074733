print("Ejercicio 9: Torneo de videojuegos")
print("Sofia Eileen Lozano Serrano")
print("T03074733")
print()

# Datos del torneo
juego = input("¿De qué juego es el torneo? ")
cantidad = int(input("¿Cuántos jugadores hay? "))

# Contadores y acumuladores
total_puntos = 0
finalistas = 0

# Variables para guardar al mejor jugador
mejor_nombre = ""
mejor_puntos = -1

# Recorremos a todos los jugadores
for jugador in range(1, cantidad + 1):
    print()
    print("🎮 Jugador", jugador)

    nombre = input("Gamertag: ")
    puntos = int(input("Puntos: "))

    # Sumamos puntos al total
    total_puntos = total_puntos + puntos

    # Revisamos si pasa a la final
    if puntos >= 100:
        print("🏅", nombre, "pasa a la final")
        finalistas = finalistas + 1
    else:
        print("💪", nombre, "sigue practicando")

    # Guardamos al que tenga más puntos
    if puntos > mejor_puntos:
        mejor_puntos = puntos
        mejor_nombre = nombre

# Resultados finales
print()
print("===== 🏆 RESULTADOS DEL TORNEO DE", juego, "=====")
print("Puntos de todos los jugadores:", total_puntos)
print("Finalistas:", finalistas)
print("👑 Ganador:", mejor_nombre, "con", mejor_puntos, "puntos")