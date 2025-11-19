# EJERCICIO 1: Suma de matrices 2x2
# Paso 1: Crear las dos matrices
matriz_a = [
    [1, 2],
    [3, 4]
]

matriz_b = [
    [5, 6],
    [7, 8]
]

# Paso 2: Crear matriz vacía para el resultado
resultado = []

# Paso 3: Recorrer las matrices y sumar
for i in range(2):  # 2 filas
    fila = []  # Crear fila vacía
    for j in range(2):  # 2 columnas
        suma = matriz_a[i][j] + matriz_b[i][j]  # Sumar elementos
        fila.append(suma)  # Agregar a la fila
    resultado.append(fila)  # Agregar fila al resultado

# Paso 4: Mostrar resultado
print("Matriz A:")
for fila in matriz_a:
    for elemento in fila:
        print(elemento, end=" ")
    print()
print("\nMatriz B:")
for fila in matriz_b:
    for elemento in fila:
        print(elemento, end=" ")
    print()

print("\nResultado A + B:")
for fila in resultado:
    for elemento in fila:
        print(elemento, end=" ")
    print()



# EJERCICIO 2: Suma de matrices 3x3
# Suma de matrices de 3x3
matriz_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Crear matriz resultado
resultado = []
# Sumar elemento por elemento
for i in range(3):  # 3 filas
    fila = []
    for j in range(3):  # 3 columnas
        suma = matriz_a[i][j] + matriz_b[i][j]
        fila.append(suma)
    resultado.append(fila)

# Mostrar resultado
print("\nResultado de la suma:")
for fila in resultado:
    for elemento in fila:
        print(elemento, end=" ")
    print()



# EJERCICIO 3: Resta de matrices 3x3
# Creamos las matrices que vamos a restar
matriz_a = [
    [10, 15, 20],
    [25, 30, 35],
    [40, 45, 50]
]

matriz_b = [
    [2, 5, 8],
    [3, 10, 15],
    [5, 20, 25]
]

# Crear una matriz vacía para guardar el resultado
resultado = []

# Recorre las matrices y resta elemento por elemento
for i in range(3):  # 3 filas
    fila = []  # Crear fila vacía para el resultado
    for j in range(3):  # 3 columnas
        resta = matriz_a[i][j] - matriz_b[i][j]  # Restar elementos
        fila.append(resta)  # Agregar resultado a la fila
    resultado.append(fila)  # Agregar fila completa al resultado

# Mostramos las matrices y el resultado
print("\nMatriz A:")
for fila in matriz_a:
    for elemento in fila:
        print(f"{elemento:3}", end=" ")
    print()

print("\nMatriz B:")
for fila in matriz_b:
    for elemento in fila:
        print(f"{elemento:3}", end=" ")
    print()

print("\nResultado (A - B):")
for fila in resultado:
    for elemento in fila:
        print(f"{elemento:3}", end=" ")
    print()


#  EJERCICIO 4: Encuentra el número mayor en una matriz
matriz = [
    [15, 8],
    [23, 12]
]

# Empezamos asumiendo que el primero es el mayor
mayor = matriz[0][0]  # Empieza con 15

# Recorremos toda la matriz
for fila in matriz:
    for elemento in fila:
        if elemento > mayor:  # Si encuentro uno más grande
            mayor = elemento  # Lo guardo como el nuevo mayor

# Mostramos resultado
print("\nLa matriz es:")
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()

print(f"\nEl número mayor es: {mayor}")
