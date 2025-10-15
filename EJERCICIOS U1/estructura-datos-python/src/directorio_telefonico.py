# filepath: estructura-datos-python/src/directorio_telefonico.py
# -*- coding: utf-8 -*-
"""
Archivo: directorio_telefonico.py
Descripción:
  Este programa implementa un directorio telefónico utilizando un diccionario.
  Permite almacenar contactos y buscar el número de un contacto por su nombre.
"""

# Paso 1: Crear un diccionario para almacenar los contactos
# Las claves del diccionario serán los nombres de los contactos y los valores serán sus números de teléfono.
directorio_telefonico = {
    "Ana": "123-456-7890",
    "Luis": "234-567-8901",
    "María": "345-678-9012",
    "Carlos": "456-789-0123",
    "Sofía": "567-890-1234"
}

# Paso 2: Función para buscar un número de teléfono por nombre
def buscar_numero(nombre):
    """Busca el número de teléfono de un contacto por su nombre."""
    return directorio_telefonico.get(nombre, "Contacto no encontrado.")

# Paso 3: Mostrar el directorio completo
print("Directorio telefónico completo:")
for nombre, numero in directorio_telefonico.items():
    print(f"{nombre}: {numero}")

# Paso 4: Ejemplo de búsqueda de un contacto
nombre_a_buscar = "María"
numero_encontrado = buscar_numero(nombre_a_buscar)
print(f"\nNúmero de teléfono de {nombre_a_buscar}: {numero_encontrado}")

# Fin del programa
print("\n✅ Programa finalizado correctamente.")