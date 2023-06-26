import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('pout.tif')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_norm = cv2.equalizeHist(img_gray)

#calcular hist
hist_original = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_norm = cv2.calcHist([img_norm], [0], None, [256], [0, 256])

plt.imshow(img, cmap='gray')
plt.title('Imagem Original')
plt.show()

plt.plot(hist_original, color='black')
plt.title('Histograma Original')
plt.show()

plt.imshow(img_norm, cmap='gray')
plt.title('Imagem Contraste Melhorado')
plt.show()

plt.plot(hist_norm, color='black')
plt.title('Histograma da Imagem Contraste Melhorado')
plt.show()
