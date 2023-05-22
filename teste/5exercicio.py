import cv2
import matplotlib.pyplot as plt
import numpy as np

# Carregue a imagem colorida
imagem = cv2.imread('testandoescalacinza.png')

# Converta a imagem para escala de cinza
imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Aumente o contraste da imagem
imagem_contraste = cv2.equalizeHist(imagem_gray)

# Mostre a imagem original em escala de cinza, a imagem com contraste aumentado e seus histogramas
plt.figure(figsize=(20, 4))

# Imagem original em escala de cinza
plt.subplot(141), plt.imshow(imagem_gray, cmap='gray')
plt.title('Imagem Original'), plt.xticks([]), plt.yticks([])

# Histograma da imagem original
plt.subplot(142), plt.hist(imagem_gray.ravel(),256,[0,256])
plt.title('Histograma da Imagem Original')

# Imagem com contraste aumentado
plt.subplot(143), plt.imshow(imagem_contraste, cmap='gray')
plt.title('Imagem com Contraste Aumentado'), plt.xticks([]), plt.yticks([])

# Histograma da imagem com contraste aumentado
plt.subplot(144), plt.hist(imagem_contraste.ravel(),256,[0,256])
plt.title('Histograma da Imagem com Contraste Aumentado')

plt.show()
