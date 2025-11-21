# Ejercicio 1
print("Ejercicios try except - Jueves 20 de nov\n")

print("Ejercicio 1: Convertir texto a número\n")

try:
    edad = int(input("¿Cuántos años tienes? "))
    print(f"El próximo año tendrás {edad + 1}")
except ValueError:
    print("ERROR: Debes escribir un número, no texto")


# Ejercicio 2
print("Ejercicios try except - Jueves 20 de nov\n")

print("Ejercicio 2: División entre números\n")

try:
    numero1 = int(input("Escribe el primer número: "))
    numero2 = int(input("Escribe el segundo número: "))
    resultado = numero1 / numero2
    print(f"El resultado de {numero1} + {numero2} = {resultado}")
except ZeroDivisionError:
    print("ERROR: No puedes dividir entre cero")
except ValueError:
    print("ERROR: Debes escribir números, no texto")


# Ejercicio 3
print("Ejercicio 3: Acceder a elementos de una lista")

try:
    amigos = ["Juan", "María", "Carlos", "Sofía"]
    posicion = int(input("¿Cuál es el número de amigo que quieres ver? (1-4): "))
    # Restamos 1 porque las listas empiezan en 0
    amigo = amigos[posicion - 1]
    print(f"Tu amigo es: {amigo}")
except IndexError:
    print("ERROR: Ese número no existe en la lista")
except ValueError:
    print("ERROR: Debes escribir un número")


# Ejercicio 4
print("Ejercicio 4: Búsqueda en un diccionario")

try:
    telefonos = {
        "Yami": "555-1234",
        "Allison": "555-5678",
        "Saul": "555-9012"
    }

    nombre = input("¿De quién quieres el teléfono? ")
    telefono = telefonos[nombre]
    print(f"El teléfono de {nombre} es: {telefono}")
except KeyError:
    print("ERROR: Ese nombre no está en la agenda")


# Ejercicio 5
print("Ejercicio 5: Multiplicar número por texto")

try:
    numero = int(input("¿Cuántas veces quieres ver el mensaje? "))
    mensaje = input("¿Cuál es el mensaje? ")
    print(mensaje * numero)
except ValueError:
    print("ERROR: Debes escribir un número entero")
except TypeError:
    print("ERROR: No se puede hacer esa operación")


# Ejercicio 6
print("Ejercicio 6: Validar edad para entrar a una peli")

try:
    edad = int(input("¿Cuántos años tienes? "))

    if edad < 0:
        print("ERROR: La edad no puede ser negativa")
    elif edad < 13:
        print("Puedes ver películas infantiles (G)")
    elif edad < 16:
        print("Puedes ver películas para adolescentes (PG-13)")
    elif edad < 18:
        print("Puedes ver películas de 15+ (PG-15)")
    else:
        print("Puedes ver cualquier película, incluyendo mayores de 18")
except ValueError:
    print("ERROR: Debes escribir tu edad como número")