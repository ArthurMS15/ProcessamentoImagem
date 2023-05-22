import cv2
from matplotlib import pyplot as plt

# Carregar a imagem em escala de cinza
img = cv2.imread('testandoescalacinza.png')
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Calcular o histograma da imagem
hist = cv2.calcHist([grayscale],[0],None,[256],[0,256])

# Plotar o histograma
plt.plot(hist, color='k')
plt.title('Histograma da Imagem em Escala de Cinza')
plt.show()
