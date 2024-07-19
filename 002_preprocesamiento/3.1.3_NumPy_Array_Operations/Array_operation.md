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
## Funciones Universales 
 Las funciones universales en NumPy son funciones eficientes que operan sobre arreglos de manera elemento por elemento, optimizadas para cálculos rápidos en arrays grandes mediante procesamiento en paralelo y optimizaciones de bajo nivel.
 ```python
import numpy as np
Resta:
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([[2, 1, 0], [1, 2, 1], [0, 1, 2]])
resultado = np.subtract(a, b)
print(resultado)
[[ -1   1   3]
 [  3   3   5]
 [  7   7   7]]
```
