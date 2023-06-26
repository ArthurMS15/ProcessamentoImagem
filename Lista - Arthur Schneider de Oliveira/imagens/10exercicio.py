import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('hw2_cone.jpg')

img_hsl = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

low_laranja = np.array([0, 100, 100], dtype=np.uint8)
up_laranja = np.array([20, 255, 255], dtype=np.uint8)

mask = cv2.inRange(img_hsl, low_laranja, up_laranja)

contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Imagem Original')
plt.show()

plt.imshow(cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB))
plt.title('Cones Detectados')
plt.show()
