import cv2
from matplotlib import pyplot as plt
import numpy as np
import skimage

# Abrimos imagen para trabajar.
imagen = cv2.imread('1.jpg')
imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

# Agregamos ruido Salt and Pepper en tres niveles de ruido distintos.
imagen_sp_1 = skimage.util.random_noise(imagen, mode='s&p', amount=0.1)
imagen_sp_2 = skimage.util.random_noise(imagen, mode='s&p', amount=0.5)
imagen_sp_3 = skimage.util.random_noise(imagen, mode='s&p', amount=0.9)

# Agregamos ruido Gaussiano en tres niveles de ruido distintos.
imagen_gauss_1 = skimage.util.random_noise(imagen, mode='gaussian', var=0.1)
imagen_gauss_2 = skimage.util.random_noise(imagen, mode='gaussian', var=0.5)
imagen_gauss_3 = skimage.util.random_noise(imagen, mode='gaussian', var=0.9)

# Agregamos ruido Poisson en 1 nivel de ruido distintos.
imagen_poisson_1 = skimage.util.random_noise(imagen, mode='poisson')


# Mostramos las imagenes con ruido.

# Resultados para ruido Salt and Pepper en distintos niveles.
plt.figure(1)

plt.subplot(232)
plt.title('Imagen original')
plt.axis('off')
plt.imshow(imagen)

plt.subplot(234)
plt.title('Imagen con ruido Salt and Pepper 10%')
plt.axis('off')
plt.imshow(imagen_sp_1)

plt.subplot(235)
plt.title('Imagen con ruido Salt and Pepper 50%')
plt.axis('off')
plt.imshow(imagen_sp_2)

plt.subplot(236)
plt.title('Imagen con ruido Salt and Pepper 90%')
plt.axis('off')
plt.imshow(imagen_sp_3)


# Resultados para ruido Gaussiano en distintos niveles.
plt.figure(2)
plt.subplot(232)
plt.title('Imagen original')
plt.axis('off')
plt.imshow(imagen)

plt.subplot(234)
plt.title('Imagen con ruido Gaussiano 10%')
plt.axis('off')
plt.imshow(imagen_gauss_1)

plt.subplot(235)
plt.title('Imagen con ruido Gaussiano 50%')
plt.axis('off')
plt.imshow(imagen_gauss_2)

plt.subplot(236)
plt.title('Imagen con ruido Gaussiano 90%')
plt.axis('off')
plt.imshow(imagen_gauss_3)

# Resultados para ruido Poisson en distintos niveles.
plt.figure(3)

plt.subplot(121)
plt.title('Imagen original')
plt.axis('off')
plt.imshow(imagen)

plt.subplot(122)
plt.title('Imagen con ruido Poisson')
plt.axis('off')
plt.imshow(imagen_poisson_1)

plt.show()