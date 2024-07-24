# Numpy Array Operations 
* [1. Suma](#1-suma)
* [2. Resta](#2-resta)
* [3. Multiplicación](#3-multiplicacion)
* [4. Repeat y Tile](#4-repeat-y-tile)
* [5. Método Mosaico](#5-metodo-mosaico)
* [6. Funciones Universales y Métodos Estadísticos](#6-funciones-universales)

## 1. Suma
Primero definimos 2 variables, en este caso son 2 listas. Al sumarlas el resultado sería una nueva lista concatenada.
```python

arr1 = [4,5,6]
arr2 = [7,8,9]
resultado = arr1 + arr2
print(resultado)
```

```python

import numpy as np

arr1 = np.array([4, 5, 6])
arr2 = np.array([7, 8, 9])
resultado = arr1 + arr2
print(resultado)  # array([11, 13, 15])
```

## 2. Resta

```python
import numpy as np
```

## 3. Multiplicación 
```python
import numpy as np
```
## 4. Repeat y Tile
En el contexto de operaciones con arrays en Python, usando la biblioteca NumPy, las funciones "repeat" y "tile" son utilizadas para manipular y duplicar elementos en un array de diferentes maneras.

- #### Repeat:
La función "repeat" de NumPy se utiliza para repetir elementos de un array a lo largo de un eje especificado y un específico de de veces.

- #### numpy.repeat:
Considerando:

a= El array de entrada

repeats= El número de repeticiones para cada elemento.

axis= El eje a lo largo del cual repetir los valores (opcional)

Ejemplo:
```python
import numpy as np
#Array de ejemplo:
a=np.array([1,2,3])

#Repetir cada elemento 2 veces
rep_a=np.repeat(a,2)
print(rep_a)
#[1 1 2 2 3 3]
```
En el ejemplo anterior, el array "a" se repite 2 veces consecutivamente.

 - #### Tile:
Por otro lado, la funciópn "tile", se utiliza para construir un nuevo array repitiendo el array de entrada un número especificado de veces.

- #### numpy.tile(b, rep)
Considerando:

b= El array de entrada rep=El número de repeticiones del array.

Ejemplo:
```python
import numpy as np
#Array de ejemplo
b=np.array([4,5,6])

#Repetir todo el array 3 veces
tile_b=np.tile(b,3)

print(tile_b)
#[4 5 6 4 5 6 4 5 6]
```
En el ejemplo anterior, el array "b" se repite como toda una entrada 3 veces.
### Diferencias entre Repeat & Tile:
- #### Repeat: 
repite cada elemento individual del array el número de veces que uno desea.
- #### Tile: 
repite el array completo el número de veces que se especifica.
Ejemplo de como usar Repeat & Tile para ver las diferencias entre estas 2 opciones:
```python
import numpy as np
#Array de ejemplo
c=np.array([7,8,9])

#Usando Repeat
rep_c=np.repeat(c,5)
print('Usando Repeat:',rep_c)

#Usando Tile
tile_c=np.tile(c,5)
print('Usando Tile:',tile_c)
#Usando Repeat: [7 7 7 7 7 8 8 8 8 8 9 9 9 9 9]
#Usando Tile: [7 8 9 7 8 9 7 8 9 7 8 9 7 8 9]
```

## 5. Método Mosaico
```python
import numpy as np
```
## 6. Funciones Universales y Métodos Estadísticos 
### Características principales:
- Operaciones elementales: Las funciones universales realizan operaciones matemáticas básicas como suma, resta, multiplicación, división, potencia, logaritmos, funciones trigonométricas, etc.
- Trabajo con arrays: Operan directamente sobre arrays NumPy, lo que las hace ideales para trabajar con grandes conjuntos de datos.
- Eficiencia: Altamente optimizadas para un rendimiento rápido, especialmente en operaciones vectoriales y matriciales.
- Versatilidad: Se pueden aplicar a arrays de diferentes dimensiones y tipos de datos.
- Transmisión: Permiten realizar operaciones entre arrays de diferentes formas y tamaños, ajustando automáticamente las dimensiones.

### Tipos de funciones universales:
- Matemáticas: Funciones aritméticas básicas, funciones trigonométricas, funciones hiperbólicas, potencias, logaritmos, etc.
- Comparación: Operadores lógicos y de comparación como igual, mayor que, menor que, etc.
- Lógicas: Operaciones lógicas como and, or, not, etc.
- Reducción: Funciones como sum, prod, min, max, mean, etc., que calculan un valor único a partir de un array.
- Otras: Funciones para redondeo, conversión de tipos, manipulación de bits, etc.
 
```python
import numpy as np
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
array3 = np.array([7, 8, 9])

```
![img](https://github.com/Carolinava21/sic_ai_2024/blob/Array-Operations/002_preprocesamiento/3.1.3_NumPy_Array_Operations/img/Funciones-Universales.png)

### Funciones Trigonométricas
```python
import numpy as np
#sin, cos, tan
senoArray1 = np.sin(array1)
cosenoArray2 = np.cos(array2)
tangenteArray3 = np.tan(array3)

print("Seno de array1:", senoArray1)
print("Coseno de array2:", cosenoArray2)
print("Tangente de array3:", tangenteArray3)
#Seno de array1: [0.84147098 0.90929743 0.14112001]
#Coseno de array2: [-0.65364362  0.28366219  0.96017029]
#Tangente de array3: [ 0.87144798 -6.79971146 -0.45231566]
```
### Funciones Trigonométricas Inversas
```python
import numpy as np
##arcsin, arccos, arctan
senoArray1 = np.arcsin(array1)
cosenoArray2 = np.arccos(array2)
tangenteArray3 = np.arctan(array3)

print("Arcseno de array1:", senoArray1)
print("Arccoseno de array2:", cosenoArray2)
print("Arctangente de array3:", tangenteArray3)
#Arcseno de array1: [1.57079633        nan        nan]
#Arccoseno de array2: [nan nan nan]
#Arctangente de array3: [1.42889927 1.44644133 1.46013911]
#<ipython-input-24-0e9887a546c8>:2: RuntimeWarning: invalid value encountered in arcsin
  #senoArray1 = np.arcsin(array1)
#<ipython-input-24-0e9887a546c8>:3: RuntimeWarning: invalid value encountered in arccos
 # cosenoArray2 = np.arccos(array2)
```
Lo que sucede en las funciones anteriores es que la funcion arcsin y arccos solo aceptan valores entre -1 y 1 por lo que no logra calcular el valor de manera correcta.
```python
import numpy as np
#por lo tanto debemos utilizar esos valores para que la función pueda realizarse
array4 = np.array([-1, 0, 1])

senoArray4 = np.arcsin(array4)
cosenoArray4 = np.arccos(array4)

print("Arcseno de array4:", senoArray4)
print("Arccoseno de array4:", cosenoArray4)
#Arcseno de array4: [-1.57079633  0.          1.57079633]
#Arccoseno de array4: [3.14159265 1.57079633 0.  
```
### Round: Redondear a un número determinado de decimales.

```python
import numpy as np
array5 = np.array([1, 2.3, 4.56, 7.89])

print("Redondeo a 1 decimal:", np.round(array5, 1))
print("Redondeo a 2 decimales:", np.round(array5, 2))
#Redondeo a 1 decimal: [1.  2.3 4.6 7.9]
#Redondeo a 2 decimales: [1.   2.3  4.56 7.89]
```
### Floor: Devuelve el entero más pequeño más cercano
```python
import numpy as np
array6 = np.array([4.1, 5.2, 6.3])

print("Parte entera menor más cercana al array6:", np.floor(array6))
#Parte entera menor más cercana al array6: [4. 5. 6.]
```
### Ceil: Devuelve el entero mayor más cercano

```python
import numpy as np
array7 = np.array([7.1, 8.2, 9.3])

print("Parte entera mayor más cercana al array7:", np.ceil(array7))
#Parte entera mayor más cercana al array7: [ 8.  9. 10.]
```
### Fix: Devuelve el entero más cercano a 0

```python
import numpy as np
array8 = np.array([-1.2, 2.5, 4.7, 6.9])

print("Parte entera más cercana al cero del array8:", np.fix(array8))
#Parte entera más cercana al cero del array8: [-1.  2.  4.  6.]
```
### exp y log: Funciones expontenciales y logaritmicas

```python
import numpy as np
#exp
exp_array = np.exp(array1)

print("Exponencial de array:", exp_array)

#log
log_array = np.log(array2)

print("Logaritmo de array:", log_array)
#Exponencial de array: [ 2.71828183  7.3890561  20.08553692]
#Logaritmo de array: [1.38629436 1.60943791 1.79175947]
```
### sqrt: Raíz cuadrada de un Array
```python
import numpy as np
raizCuadrada = np.sqrt(array1)

print(raizCuadrada)
#[1.         1.41421356 1.73205081]
```
## Métodos Estadísticos
### Mean: Promedio

```python
import numpy as np
mean_array = np.mean(array1)

print("Promedio de array1:", mean_array)
#Promedio de array1: 2.0
```
### Var: Varianza
```python
import numpy as np
var_array = np.var(array2)

print("Varianza de array2:", var_array)
#Varianza de array2: 0.6666666666666666
```
### std: Desviación Estándar
```python
import numpy as np
std_array = np.std(array3)

print("Desviación Estándar de array3:", std_array)
#Desviación Estándar de array3: 0.816496580927726
```
### Sum: Suma Total(se suman todos los indices array1=([1, 2, 3]) = 1 + 2 + 3 = 3 + 3 = 6)

```python
import numpy as np
suma_array = np.sum(array1)

print("Suma de array1:", suma_array)
#Suma de array1: 6
```
### cumsum : Las sumas acumuladas de un array
```python
import numpy as np
cumsum_array = np.cumsum(array1)

print("Suma Acumulada de array1:", cumsum_array)

#El primer elemento del array de salida es igual al primer elemento del array de entrada.
#El segundo elemento del array de salida es la suma del primer y segundo elemento del array de entrada.
#El tercer elemento del array de salida es la suma del primer, segundo y tercer elemento del array de entrada.
# Suma Acumulada de array1: [1 3 6]
```
### Max, Min: El máximo y mínimo de un Array
```python
import numpy as np
max_array = np.max(array1)
min_array = np.min(array1)

print("Máximo de array1:", max_array)
print("Mínimo de array1:", min_array)
#Máximo de array1: 3
#Mínimo de array1: 1
```
### argmax y argmin: índices del máx y min.
```python
import numpy as np
argmax_array = np.argmax(array1)
argmin_array = np.argmin(array1)

print("Máximo índice de array1:", argmax_array)
print("Mínimo índice de array1:", argmin_array)
#Máximo índice de array1: 2
#Mínimo índice de array1: 0
```
