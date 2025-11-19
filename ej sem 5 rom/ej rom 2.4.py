print("Ejercicio 1: Ordenar una lista pequeña\n") 

numeros_lista = [5, 2, 8, 1, 9, 12, 4]
print("Lista original:", numeros_lista)

# Ordenar con Bubble Sort
n = len (numeros_lista) #n = 7 elementos en numeros_lista
for i in range(n):
    for j in range(0, n - i - 1):
        # Comparar vecinos
        if numeros_lista[j] > numeros_lista[j + 1]:
            # Intercambiar
            numeros_lista[j], numeros_lista[j + 1] = numeros_lista[j + 1], numeros_lista[j]
print("Lista ordenada:", numeros_lista)

print("\nEjercicio 3: Calificaciones de la clase\n")
calificaciones = [85, 92, 78, 100, 88, 70]
print("Calificaciones desordenadas: \n", calificaciones)
n = len (calificaciones)
for i in range(n) :
        for j in range(0, n - i - 1):
            if calificaciones [j] > calificaciones [j + 1]:
                calificaciones[j], calificaciones[j + 1] = calificaciones [j + 1], calificaciones [j]
print ("Calificaciones ordenadas: \n", calificaciones)
print("Calificacion mas baja: In", calificaciones[0])
print("Calificacion mis alta: In", calificaciones[-1])

print("InEjercicio 4: Ver cada paso del ordenamiento \n")
numeros_ej4 = [25, 18, 34, 79, 83]
print("Inicio:", numeros_ej4)
print("-" * 30)
n = len (numeros_ej4)

for i in range(n):
    print(f" (nPasada {i + 1}:")
    for j in range(0, n - i - 1):
        print(f" Comparando {numeros_ej4[j]} y {numeros_ej4[j + 1]}")
        if numeros_ej4[j] > numeros_ej4[j + 1]:
            # Intercambiar
            numeros_ej4[j], numeros_ej4[j + 1] = numeros_ej4[j + 1], numeros_ej4[j]
            print(f" Intercambio → {numeros_ej4}")
        else:
            print(f" No cambiar → {numeros_ej4}")

print("\n" + "-" * 30)
print("Final:\n", numeros_ej4)

print("InEjercicio 5: Orden descendente (mayor a menor) \n")
numeros_ej5 = [51, 23, 85, 17, 19]
print("Original:\n", numeros_ej5)
n = len(numeros_ej5)

for i in range(n):
    for j in range(0, n - i - 1):
        # CAMBIO: < en lugar de >
        if numeros_ej5[j] < numeros_ej5[j + 1]:
            numeros_ej5[j], numeros_ej5[j + 1] = numeros_ej5[j + 1], numeros_ej5[j]

print("Ordenado (mayor a menor): \n", numeros_ej5)
      
print( "InEjercicio 6: Desafio\n")

numeros_ej6 = [12, 5, 9, 2, 15]
print("Original: \n", numeros_ej6)
n = len (numeros_ej6)
for i in range(n):
    for j in range(0, n - i - 1):
        if numeros_ej6[j] > numeros_ej6[j + 1]: # ¿Qué va aqui?
            numeros_ej6[j], numeros_ej6[j + 1] = numeros_ej6[j + 1] , numeros_ej6[j] # Completa

print("Ordenado: \n",numeros_ej6)
