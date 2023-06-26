import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('ifc_vda.jpeg', cv2.IMREAD_GRAYSCALE)

#limiarização
_, img_thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

#hist
hist_original = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_thresh = cv2.calcHist([img_thresh], [0], None, [256], [0, 256])

plt.imshow(img, cmap='gray')
plt.title('Imagem Original (em Escala de Cinza)')
plt.show()

plt.plot(hist_original, color='black')
plt.title('Histograma Original')
plt.show()

plt.imshow(img_thresh, cmap='gray')
plt.title('Imagem Limiarização')
plt.show()

plt.plot(hist_thresh, color='black')
plt.title('Histograma Limiarização')
plt.show()
