# File: /estructura-datos-python/estructura-datos-python/src/lista_estudiantes.py

# -*- coding: utf-8 -*-
"""
Archivo: lista_estudiantes.py
Descripción:
  Este programa demuestra el uso de una estructura de datos tipo lista (array)
  para almacenar y recorrer una lista de nombres de estudiantes.
"""

# Paso 1: Crear una lista con nombres de estudiantes
# Las listas se declaran entre corchetes [] y los elementos se separan por comas.
estudiantes = ["Ana", "Luis", "María", "Carlos", "Sofía"]

# Paso 2: Mostrar la lista completa
print("Lista completa de estudiantes:")
print(estudiantes)
print("--------------------------------")

# Paso 3: Recorrer la lista con un bucle for
print("Nombres de los estudiantes (uno por línea):")
for nombre in estudiantes:
    print("→", nombre)

# Paso 4: Agregar un nuevo estudiante a la lista
nuevo_estudiante = "Javier"
estudiantes.append(nuevo_estudiante)  # .append() añade un elemento al final
print("\nDespués de agregar un nuevo estudiante:")
print(estudiantes)

# Paso 5: Mostrar la cantidad total de estudiantes
print("\nCantidad total de estudiantes:", len(estudiantes))

# Paso 6: Ejemplo adicional: acceder al primer y último estudiante
print("\nPrimer estudiante de la lista:", estudiantes[0])
print("Último estudiante de la lista:", estudiantes[-1])

# Fin del programa
print("\n✅ Programa finalizado correctamente.")