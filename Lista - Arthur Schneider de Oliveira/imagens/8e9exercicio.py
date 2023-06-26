import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('placa.png', 0)

img_blur = cv2.GaussianBlur(img, (5, 5), 0)

_, img_thresh = cv2.threshold(img_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

kernel = np.ones((5, 5), np.uint8)

img_er = cv2.erode(img_thresh, kernel, iterations=1)

img_dil = cv2.dilate(img_er, kernel, iterations=1)

img_op = cv2.morphologyEx(img_thresh, cv2.MORPH_OPEN, kernel)


img_cl = cv2.morphologyEx(img_thresh, cv2.MORPH_CLOSE, kernel)

plt.imshow(img, cmap='gray')
plt.title('Imagem Original')
plt.show()

plt.imshow(img_blur, cmap='gray')
plt.title('Suavização (Filtro Gaussiano)')
plt.show()

plt.imshow(img_thresh, cmap='gray')
plt.title('Limiarização (Otsu)')
plt.show()

plt.imshow(img_er, cmap='gray')
plt.title('Erosão')
plt.show()

plt.imshow(img_dil, cmap='gray')
plt.title('Dilatação')
plt.show()

plt.imshow(img_cl, cmap='gray')
plt.title('Fechamento')
plt.show()
