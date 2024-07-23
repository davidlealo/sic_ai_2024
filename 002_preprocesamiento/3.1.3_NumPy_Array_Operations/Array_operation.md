# Numpy Array Operations 
## Suma
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

## Resta

```python
import numpy as np
```

## Multiplicación 
```python
import numpy as np
```
## Repeat & Tile
```python
import numpy as np
```

## Método Mosaico
```python
import numpy as np
```
## Funciones Universales y Métodos Estadísticos 
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