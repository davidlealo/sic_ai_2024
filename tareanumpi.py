import numpy as np

# Tarea: Parte 1.
# ¿Cómo cambiar la forma de una matriz con numpy?
# Paso 1: Definimos nuestra matriz, o "array".

arr1 = np.arange(20)
print("Array original:", arr1)

# Paso 2: Usamos la "reshape" para cambiar la forma de nuestra matriz pero SIN CAMBIAR
# SUS DATOS!
# En este caso yo elegí que fuera de 4 filas y 5 columnas, pero puede ser de 
# la forma que quieras. 

reshaped_arr1 = arr1.reshape(4, 5)
print("Array cambiada con 'reshape':")
print(reshaped_arr1)

# Paso 3: Podemos volver a cambiar la forma de la matriz, pero alterandola desde la 
# base con "shape"

arr1.shape = (2, 10)
print("Array con alterada con 'shape'):")
print(arr1)

# Tarea: Parte 2.
# Para hacer una matriz con números aleatorios entre 0 y 1, podemos usar 
# "np.random.randn". Ejemplo:
numerosAleatorios = np.random.randn(10)
print("Números aleatorios entre 0 y 1:", numerosAleatorios)
# Este código hará una matriz unidimensional

# Ahora podemos juntar los dos métodos 'np.random.randn' y 'shape' pero, 
# ¿Qué hará la función...? 
# R: Creará una matriz 2D (bidimensional) de 100 filas y 100 columnas 
# con números aleatorios entre 0 y 1.
arrayGrande = np.random.randn(100, 100)
print("Array grande:", arrayGrande.shape)
