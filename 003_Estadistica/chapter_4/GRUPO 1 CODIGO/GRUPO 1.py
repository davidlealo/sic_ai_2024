
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson

# Ejemplo de Distribución Binomial
def distribucion_binomial(n, p, k):
    probabilidad = binom.pmf(k, n, p)
    print(f"La probabilidad de obtener exactamente {k} éxitos en {n} ensayos es {probabilidad:.4f}")
    
    # Visualización
    k_vals = np.arange(0, n+1)
    probabilidades = binom.pmf(k_vals, n, p)
    plt.bar(k_vals, probabilidades)
    plt.xlabel('Número de éxitos (k)')
    plt.ylabel('Probabilidad')
    plt.title('Distribución Binomial')
    plt.show()

# Ejemplo de Distribución de Poisson
def distribucion_poisson(lambd, k):
    probabilidad = poisson.pmf(k, lambd)
    print(f"La probabilidad de que ocurran exactamente {k} eventos cuando la tasa promedio es {lambd} es {probabilidad:.4f}")
    
    # Visualización
    k_vals = np.arange(0, 15)
    probabilidades = poisson.pmf(k_vals, lambd)
    plt.bar(k_vals, probabilidades)
    plt.xlabel('Número de eventos (k)')
    plt.ylabel('Probabilidad')
    plt.title('Distribución de Poisson')
    plt.show()

# Parámetros de ejemplo
n = 10  # número de ensayos
p = 0.5  # probabilidad de éxito
k_binomial = 3  # número de éxitos en la binomial
lambd = 2  # tasa promedio para Poisson
k_poisson = 3  # número de eventos en Poisson

# Llamar a las funciones de ejemplo
distribucion_binomial(n, p, k_binomial)
distribucion_poisson(lambd, k_poisson)
'''
Explicación Lógica
Distribución Binomial
Concepto: La distribución binomial se utiliza cuando se tienen varios ensayos (experimentos repetidos) con dos posibles resultados (éxito o fracaso). Cada ensayo es independiente, y la probabilidad de éxito es constante.
Aplicaciones: Lanzar una moneda varias veces, pruebas de calidad en una línea de producción.
Distribución de Poisson
Concepto: La distribución de Poisson se utiliza para modelar el número de eventos que ocurren en un intervalo de tiempo fijo, cuando estos eventos son independientes y ocurren con una tasa constante.
Aplicaciones: Número de llamadas a un centro de atención en una hora, número de llegadas de clientes a una tienda en un día.
Conclusión
Las distribuciones de probabilidad discreta son herramientas fundamentales en la teoría de la probabilidad y la estadística, permitiendo modelar y entender fenómenos en los que los resultados posibles son discretos. Con las distribuciones binomial y de Poisson, podemos calcular probabilidades y hacer inferencias sobre datos en diversas aplicaciones prácticas.
'''