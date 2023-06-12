import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregando a imagem
img = cv2.imread('044.jpg',0) # 0 para carregar em escala de cinza

# Kernel Laplaciano para nitidez
kernel = np.array([[0, -1, 0], [-1, 5,-1], [0, -1, 0]])

# Aplicando o kernel na imagem
sharp_img = cv2.filter2D(img, -1, kernel)

# Plotando as imagens
plt.figure(figsize=(10,5))

plt.subplot(121)
plt.imshow(img, cmap='gray')
plt.title('Imagem original')
plt.axis('off')

plt.subplot(122)
plt.imshow(sharp_img, cmap='gray')
plt.title('Imagem com nitidez melhorada')
plt.axis('off')

plt.tight_layout()
plt.show()
