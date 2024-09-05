import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
import time

INICIO = time.time()
INFLUENCE_DEGR_CONSTANT = 0.5

#Se crean los cuatro mapas que se van a unir
noise1 = PerlinNoise(octaves=3, seed=4)
noise2 = PerlinNoise(octaves=6, seed=4)
noise3 = PerlinNoise(octaves=12, seed=4)
noise4 = PerlinNoise(octaves=24, seed=4)
noise5 = PerlinNoise(octaves=48, seed=4)

#Se crea un nuevo mapa, representado con una lista de listas, en donde por cada casilla
#se añaden cada uno de los mapas (noise 1 - noise 4) cada uno con cada vez menor influencia
xpix, ypix = 31600,31600
pic = []
for i in range(xpix):
    row = []
    for j in range(ypix):
        noise_val = noise1([i/xpix, j/ypix])
        noise_val += 0.5 * noise2([i/xpix, j/ypix])
        #noise_val += 0.25 * noise3([i/xpix, j/ypix])
        #noise_val += 0.125 * noise4([i/xpix, j/yp ix])
        #noise_val += 0.0625 * noise5([i/xpix, j/ypix])
        row.append(noise_val)
    pic.append(row)

FIN = time.time()
tiempo_final = ((FIN - INICIO))
print("time taken:  ", tiempo_final)
#Se guarda una img en formato png del mapa usando la libreria matplotlib
#print(pic)
#plt.imshow(pic, cmap='gray')
#plt.savefig('perlin_noise.png')