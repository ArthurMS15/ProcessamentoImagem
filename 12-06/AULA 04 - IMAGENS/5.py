import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregando a imagem
img = cv2.imread('parrot.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Convertendo de BGR para RGB

# Criando a tabela de ajuste de gamma
gamma = 1.5
table = np.array([((i / 255.0) ** gamma) * 255
    for i in np.arange(0, 256)]).astype("uint8")

# Aplicando o ajuste de gamma na imagem
gamma_img = cv2.LUT(img, table)

# Plotando as imagens
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

# Imagem original
ax[0].imshow(img)
ax[0].set_title("Imagem original")

# Imagem com ajuste de gamma
ax[1].imshow(gamma_img)
ax[1].set_title("Imagem com ajuste de gamma")

# Removendo os eixos para ambos os plots
for axes in ax:
    axes.set_xticks([])
    axes.set_yticks([])

plt.show()
