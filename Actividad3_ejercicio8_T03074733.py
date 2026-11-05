print("Ejercicio 8: Revisa tu gamertag")
print("Sofia Eileen Lozano Serrano")
print("T03074733")
print()

# Pedimos el gamertag
gamertag = input("Escribe tu gamertag: ")

# Contadores
vocales = 0
numeros = 0
caracteres = 0

# Recorremos el gamertag letra por letra
for letra in gamertag:
    print("🔤", letra)

    # Contamos caracteres
    caracteres = caracteres + 1

    # Contamos vocales
    if letra in "aeiouAEIOU":
        vocales = vocales + 1

    # Contamos números
    if letra in "0123456789":
        numeros = numeros + 1

# Mostramos resultados
print("===== RESUMEN =====")
print("Caracteres:", caracteres)
print("Vocales:", vocales)
print("Números:", numeros)

# Damos consejo
if numeros == 0:
    print("💡 Consejo: agrégale un número para que sea único")
else:
    print("✅ ¡Buen gamertag!")