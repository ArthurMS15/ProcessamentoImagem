import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregando a imagem
img = cv2.imread('parrot.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Convertendo de BGR para RGB

# Ajustando o brilho
bright_img = cv2.convertScaleAbs(img, alpha=1.2, beta=0)

# Plotando as imagens
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

# Imagem original
ax[0].imshow(img)
ax[0].set_title("Imagem original")

# Imagem com brilho ajustado
ax[1].imshow(bright_img)
ax[1].set_title("Imagem com brilho ajustado")

# Removendo os eixos para ambos os plots
for axes in ax:
    axes.set_xticks([])
    axes.set_yticks([])

plt.show()
