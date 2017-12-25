# ===============================================================
# Autor: Rodolfo Ferro Pérez
# Email: ferro@cimat.mx
# Twitter: @FerroRodolfo
#
# Script: Cómo simular datos válidos a partir de una muestra
# ===============================================================

# Importamos paquetes:
import matplotlib.pyplot as plt
import scipy.stats as st
import seaborn as sns
import numpy as np


# Muestra de tiempos:
tiempos = np.array([2.50, 4.93, 5.01, 1.11, 4.93, 3.51,
                    1.86, 0.10, 0.10, 0.05, 1.06, 1.06,
                    3.86, 0.75, 0.48, 1.53, 0.48, 1.18,
                    1.25, 2.78, 0.66, 5.36, 0.05, 2.13,
                    0.25, 2.28, 5.88, 18.45])


# PASO 1 - Creamos histograma.
breaks = 20
x = np.linspace(0.5, breaks, 1000)
plt.figure(1)
plt.hist(tiempos, breaks, normed=True, facecolor='blue',
         alpha=0.75, ec='white', label="Histograma de tiempos")
plt.title("Histograma de tiempos")
plt.xlabel("Tiempos")
plt.ylabel("Frecuencia de tiempos")
# plt.show()


# PASO 2 - Proponemos un modelo.
dist_name = 'weibull_min'


# PASO 3 - Estimamos parámetros.
# Estimador de parámetros:
dist = getattr(st, dist_name)
param = dist.fit(tiempos)
pdf_fitted = dist.pdf(x, *param[:-2], loc=param[-2], scale=param[-1])
print("Parámetros obtenidos: {}".format(param))


# PASO 4 - Validamos nuestro modelo.
# Función de Distribución Empírica (FDE):
def ecdf(x):
    xs = np.sort(x)
    ys = np.arange(1, len(xs)+1)/float(len(xs))
    return xs, ys


# Gráfica cuantil-cuantil:


# Densidad sobre histograma:
plt.figure(4)
plt.hist(tiempos, breaks, normed=True, facecolor='blue',
         alpha=0.75, ec='white', label="Histograma de tiempos")
plt.plot(x, pdf_fitted)
plt.title("Histograma de tiempos \nDensidad ajustada")
plt.show()

# PASO 5 - Simular datos.
# Validar con nube de puntos:
# Simulamos una muestra de 100 datos:
# Media y suma total:
