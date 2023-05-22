import cv2
from matplotlib import pyplot as plt

# Carregar a imagem em escala de cinza
img = cv2.imread('testandoescalacinza.png')
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

equalized = cv2.equalizeHist(grayscale)

# Calcular o histograma da imagem
histgray = cv2.calcHist([grayscale],[0],None,[256],[0,256])
hist = cv2.calcHist([equalized],[0],None,[256],[0,256])

# Plotar a imagem em escala de cinza
plt.figure(figsize=(10,4))
plt.subplot(121), plt.imshow(grayscale, cmap='gray'), plt.title('Imagem convertida em escala de cinza')
plt.subplot(122), plt.plot(histgray, color='k'), plt.title('Histograma da Imagem em Escala de Cinza')
plt.show()

# Plotar a imagem equalizada e o histograma
plt.figure(figsize=(10,4))
plt.subplot(121), plt.imshow(equalized, cmap='gray'), plt.title('Imagem equalizada que havia sido convertida em escala de cinza')
plt.subplot(122), plt.plot(hist, color='k'), plt.title('Histograma da Imagem Equalizada em Escala de Cinza')
plt.show()
