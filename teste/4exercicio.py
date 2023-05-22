import cv2
import matplotlib.pyplot as plt
import numpy as np

# Carregue a imagem em escala de cinza
imagem = cv2.imread('testandoescalacinza.png', cv2.IMREAD_GRAYSCALE)

# Aplique a limiarização
_, imagem_limiarizada = cv2.threshold(imagem, 127, 255, cv2.THRESH_BINARY)

# Mostre a imagem original e a imagem limiarizada e seus histogramas
plt.figure(figsize=(20, 4))

# Imagem original
plt.subplot(141), plt.imshow(imagem, cmap='gray')
plt.title('Imagem Original'), plt.xticks([]), plt.yticks([])

# Histograma da imagem original
plt.subplot(142), plt.hist(imagem.ravel(),256,[0,256])
plt.title('Histograma da Imagem Original')

# Imagem limiarizada
plt.subplot(143), plt.imshow(imagem_limiarizada, cmap='gray')
plt.title('Imagem Limiarizada'), plt.xticks([]), plt.yticks([])

# Histograma da imagem limiarizada
plt.subplot(144), plt.hist(imagem_limiarizada.ravel(),256,[0,256])
plt.title('Histograma da Imagem Limiarizada')

plt.show()
