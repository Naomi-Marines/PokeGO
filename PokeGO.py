# ===============================================================
# Autor: Rodolfo Ferro Pérez
# Email: ferro@cimat.mx
# Twitter: @FerroRodolfo
#
# Script: Cómo simular datos válidos a partir de una muestra
# ===============================================================

# Importamos paquetes:
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
import scipy

# Muestra de tiempos:
tiempos = np.array([2.50, 4.93, 5.01, 1.11, 4.93, 3.51,
                    1.86, 0.10, 0.10, 0.05, 1.06, 1.06,
                    3.86, 0.75, 0.48, 1.53, 0.48, 1.18,
                    1.25, 2.78, 0.66, 5.36, 0.05, 2.13,
                    0.25, 2.28, 5.88, 18.45])

# PASO 1 - Creamos histograma.
n, bins, patches = plt.hist(tiempos, 16, normed=True,
                            facecolor='green', alpha=0.75)
plt.show()

# PASO 2 - Proponemos un modelo.

# PASO 3 - Estimamos parámetros.
# Estimador de parámetros:

# PASO 4 - Validamos nuestro modelo.
# Función de Distribución Empírica (FDE):
# Gráfica cuantil-cuantil:
# Densidad sobre histograma:

# PASO 5 - Simular datos.
# Validar con nube de puntos:
# Simulamos una muestra de 100 datos:
# Media y suma total:
