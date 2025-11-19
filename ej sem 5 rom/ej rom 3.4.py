# EJEMPLO 1: Mostrar el menú
print("\nEjemplo 1 mostrar el menu\n")

def mostrar_menu():
    print("=== MENÚ ===")
    print("1. Hamburguesa")
    print("2. Pizza")
    print("3. Tacos")

mostrar_menu()



# EJEMPLO 2: Reproducir tu canción favorita (sin parámetros)
print("\nEjemplo 2 la fav canción\n")

def reproducir_favorita():
    print("Reproduciendo: 'Blinding Lights' de The Weeknd")

reproducir_favorita()



# EJEMPLO 3: Mostrar reglas del juego
print("\nEjemplo 3 reglas del juego\n")

def mostrar_reglas():
    print("REGLAS DEL JUEGO:")
    print("- No hacer trampa")
    print("- Respetar turnos")
    print("- Divertirse")

mostrar_reglas()



# EJEMPLO 4: Reproducir cualquier canción (con parámetros)
print("\nEjemplo 4\n")

def reproducir_cancion(nombre_cancion):
    print(f"🎵 Reproduciendo: {nombre_cancion}")

reproducir_cancion("Bad Bunny - Titi Me Preguntó")
reproducir_cancion("Karol G - TQG")
reproducir_cancion("Taylor Swift - Anti-Hero")



# EJEMPLO 5: Calcular impuesto
print("\nEjemplo 5\n")

def calcular_impuesto(precio):
    total = precio * 1.16  # impuesto 16%
    return total

print(calcular_impuesto(110))
print(calcular_impuesto(500))
print(calcular_impuesto(1200))
