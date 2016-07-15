# Rodolfo Ferro Pérez
# Google Developer Group
# Cómo simular datos válidos a partir de una muestra

# Liberar memoria:
rm(list=ls())

# Muestra de tiempos:
tiempos = c(2.50, 4.93, 5.01, 1.11, 4.93, 
            3.51, 1.86, 0.10, 0.10, 0.05, 
            1.06,  1.06, 3.86, 0.75, 0.48, 
            1.53, 0.48, 1.18, 1.25, 2.78, 
            0.66, 5.36, 0.05, 2.13, 0.25, 
            2.28, 5.88, 18.45)

# PASO 1 - Creamos histograma:
#png('histograma_tiempos_adj=0.8.png') # Para iniciar el guardado de imagen
hist(tiempos,freq=F,main="Histograma de tiempos \n Densidad ajustada",
     xlab="Tiempos",ylab="Frecuencia de tiempos",
     border="white", col="steelblue", breaks=20)
lines(density(tiempos, adjust=0.8), col="red", lwd=2)
#dev.off() # Fin de guardado de imagen

# PASO 2 - Proponemos un modelo.
# De acuerdo a los datos obtenidos, proponemos la distribución Weibull.

# PASO 3 - Estimamos parámetros:
# Estimador de parámetros
library(MASS) ## loading package MASS
fitdistr(tiempos,densfun=dweibull,start=list(shape = 1, scale = 1)) # Init params

# PASO 4 - Validamos nuestro modelo.
# Función de Distribución Empírica (FDE):
#png('FDE.png') # Para iniciar el guardado de imagen
curve(pweibull(x,0.8217399,2.3512539) ,col="navy", lwd=4,
      main="FDE vs FDT",from=0,to=20)
lines(ecdf(tiempos), col="lightseagreen")
#dev.off() # Fin de guardado de imagen

# Gráfica cuantil-cuantil:
N = length(tiempos)
int = seq((1/(N+1)),(N/(N+1)),by=(1/(N+1)))
vec = qweibull(int,0.8217399,2.3512539)
#png('QQ.png') # Para iniciar el guardado de imagen
plot(sort(tiempos),sort(vec),main="Gráfica Q-Q", col="navy", lwd=3)
abline(0,1,col="red",lwd="2")
#dev.off() # Fin de guardado de imagen

# Densidad sobre histograma
#png('histograma_density.png') # Para iniciar el guardado de imagen
hist(tiempos,freq=F,main="Histograma de tiempos \n Densidad estimada",
     xlab="Tiempos",ylab="Frecuencia de tiempos",
     border="white", col="steelblue", breaks=20)
lines(density(tiempos, adjust=0.8), col="red", lwd=1)
curve(dweibull(x,0.8217399,2.3512539),col="green",add = T, lwd=2)
#dev.off() # Fin de guardado de imagen

# PASO 5 - Simular datos:
# Validar con nube de puntos
m = matrix(qweibull(runif(N*50),0.8217399,2.3512539), nrow = 50, ncol = N, byrow = T)

#png('QQ_nube.png') # Para iniciar el guardado de imagen
plot(sort(tiempos),sort(vec),main="Nube de puntos en Q-Q")
for (i in 1:50) {
  points(sort(tiempos),sort(m[i,1:N]),col='lightseagreen',add=T)
}
abline(0,1,col="red",lwd="2")
points(sort(tiempos),sort(vec),col="navy", lwd=3)
#dev.off() # Fin de guardado de imagen

# Simulamos una muestra de 100 datos:
num_datos = 100
datos_unif = runif(num_datos)
simulados = qweibull(datos_unif,0.8217399,2.3512539)
simulados

# Media y suma total:
mean(simulados)
sum(simulados)