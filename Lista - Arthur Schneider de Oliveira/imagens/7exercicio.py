import cv2
import matplotlib.pyplot as plt

img = cv2.imread('hw3_license_plate_noisy.png')

#Filtro de Média
img_filt = cv2.medianBlur(img, 3, 3)

# Mostrar as imagens
plt.imshow(img)
plt.title('Imagem com Ruído')
plt.show()

plt.imshow(img_filt)
plt.title('Imagem Filtrada')
plt.show()
