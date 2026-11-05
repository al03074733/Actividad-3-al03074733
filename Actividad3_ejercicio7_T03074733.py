print("Ejercicio 7: Boletos para el concierto")
print("Sofia Eileen Lozano Serrano")
print("T03074733")
print()

# Pedimos el artista y cuántos boletos quiere
artista = input("¿De quién es el concierto? ")
cantidad = int(input("¿Cuántos boletos quieres? "))

# Generamos los boletos
for boleto in range(1, cantidad + 1):
    # Pedimos el nombre del asistente
    asistente = input("Nombre del asistente " + str(boleto) + ": ")

    # Mostramos el boleto
    print("🎟️ Boleto", boleto, "de", cantidad)
    print("🎤", artista, "- Asistente:", asistente)

# Mensaje final
print("✅ Se generaron", cantidad, "boletos. ¡Disfruten el concierto!")