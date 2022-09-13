# Importamos librerias a utilizar
from matplotlib import pyplot as plt
import numpy as np
import skimage
import math
from skimage import io

def PSNR(img1, img2):
    mse = np.mean((img1 - img2) ** 2)
    if mse == 0:
        return 100
    pm = 255.0
    return 20 * math.log10(pm / math.sqrt(mse))


# Abrimos imagen para trabajar.

imagen = skimage.io.imread('1.jpg')
imagen = skimage.img_as_float(imagen)

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

# Realizamos PSNR para cada imagen con ruido.
# PSNR para ruido Salt and Pepper en distintos niveles.
psnr_sp_1 = PSNR(imagen, imagen_sp_1)
psnr_sp_2 = PSNR(imagen, imagen_sp_2)
psnr_sp_3 = PSNR(imagen, imagen_sp_3)


# PSNR para ruido Gaussiano en distintos niveles.
psnr_gauss_1 = PSNR(imagen, imagen_gauss_1)
psnr_gauss_2 = PSNR(imagen, imagen_gauss_2)
psnr_gauss_3 = PSNR(imagen, imagen_gauss_3)

# PSNR para ruido Poisson en distintos niveles.
psnr_poisson_1 = PSNR(imagen, imagen_poisson_1)

# Mostramos los resultados de PSNR.
print('PSNR para ruido Salt and Pepper 10%: ', psnr_sp_1)
print('PSNR para ruido Salt and Pepper 50%: ', psnr_sp_2)
print('PSNR para ruido Salt and Pepper 90%: ', psnr_sp_3)
print('PSNR para ruido Gaussiano 10%: ', psnr_gauss_1)
print('PSNR para ruido Gaussiano 50%: ', psnr_gauss_2)
print('PSNR para ruido Gaussiano 90%: ', psnr_gauss_3)
print('PSNR para ruido Poisson: ', psnr_poisson_1)

