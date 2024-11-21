# Array Transposition and Axis Swap  

Trabajo Catalina Ramirez Olave 

## Índice
- [Introducción](#introducción)
- [Transposición de Arrays](#transposición-de-arrays)
  - [Método `.transpose()`](#método-transpose)
  - [Ejemplo de `.transpose()`](#ejemplo-de-transpose)
  - [Transposición en Arrays Multidimensionales](#transposición-en-arrays-multidimensionales)
- [Intercambio de Ejes](#intercambio-de-ejes)
  - [Método `.swapaxes()`](#método-swapaxes)
  - [Ejemplo de `.swapaxes()`](#ejemplo-de-swapaxes)
  - [Intercambio de Ejes en Arrays Multidimensionales](#intercambio-de-ejes-en-arrays-multidimensionales)
- [Comparación entre `.transpose()` y `.swapaxes()`](#comparación-entre-transpose-y-swapaxes)

## Introducción
En la manipulación de arrays, especialmente con bibliotecas como NumPy en Python, las operaciones de transposición y el intercambio de ejes son fundamentales. Estas operaciones permiten reorganizar los datos en un array sin cambiar su contenido. Esto es útil en el procesamiento de datos, aprendizaje automático y otras áreas científicas y de ingeniería.

## Transposición de Arrays

### Método `.transpose()`
La transposición de un array implica cambiar su orientación. En términos simples, convierte las filas en columnas y las columnas en filas. En NumPy, esto se logra utilizando el método `.transpose()`.

#### Sintaxis
```python
numpy_array.transpose(*axes)
```
- `axes`: Tupla de enteros. Por defecto, invierte el orden de los ejes.

### Ejemplo de `.transpose()`
```python
import numpy as np

# Crear un array 2D
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Transponer el array
array_transposed = array_2d.transpose()

print("Array Original:\n", array_2d)
print("Array Transpuesto:\n", array_transposed)
```
**Salida:**
```
Array Original:
 [[1 2 3]
 [4 5 6]]
Array Transpuesto:
 [[1 4]
 [2 5]
 [3 6]]
```

### Transposición en Arrays Multidimensionales
La transposición también se puede aplicar a arrays multidimensionales. Aquí, el orden de los ejes se puede especificar explícitamente.

#### Ejemplo de transposición en arrays 3D
```python
import numpy as np

# Crear un array 3D
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Transponer el array
array_transposed = array_3d.transpose(1, 0, 2)

print("Array Original:\n", array_3d)
print("Array Transpuesto:\n", array_transposed)
```
**Salida:**
```
Array Original:
 [[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
Array Transpuesto:
 [[[1 2]
  [5 6]]

 [[3 4]
  [7 8]]]
```

## Intercambio de Ejes

### Método `.swapaxes()`
El método `.swapaxes()` permite intercambiar dos ejes específicos de un array. Esto es más flexible que `.transpose()` cuando se necesitan cambios específicos entre dos ejes.

#### Sintaxis
```python
numpy_array.swapaxes(axis1, axis2)
```
- `axis1`: Primer eje a intercambiar.
- `axis2`: Segundo eje a intercambiar.

### Ejemplo de `.swapaxes()`
```python
import numpy as np

# Crear un array 2D
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Intercambiar ejes
array_swapped = array_2d.swapaxes(0, 1)

print("Array Original:\n", array_2d)
print("Array con Ejes Intercambiados:\n", array_swapped)
```
**Salida:**
```
Array Original:
 [[1 2 3]
 [4 5 6]]
Array con Ejes Intercambiados:
 [[1 4]
 [2 5]
 [3 6]]
```

### Intercambio de Ejes en Arrays Multidimensionales
El intercambio de ejes también se puede aplicar a arrays multidimensionales, proporcionando más control sobre la manipulación de datos.

#### Ejemplo de intercambio de ejes en arrays 3D
```python
import numpy as np

# Crear un array 3D
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Intercambiar ejes
array_swapped = array_3d.swapaxes(0, 2)

print("Array Original:\n", array_3d)
print("Array con Ejes Intercambiados:\n", array_swapped)
```
**Salida:**
```
Array Original:
 [[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
Array con Ejes Intercambiados:
 [[[1 5]
  [3 7]]

 [[2 6]
  [4 8]]]
```

## Comparación entre `.transpose()` y `.swapaxes()`
- `.transpose()` es útil para transponer matrices completas o invertir el orden de los ejes.
- `.swapaxes()` es más flexible para intercambiar dos ejes específicos en arrays multidimensionales.

