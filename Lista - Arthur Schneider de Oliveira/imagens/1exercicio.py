import cv2
import matplotlib.pyplot as plt

#carregar img
img = cv2.imread('ifc_vda.jpeg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#conversão para escala de cinza
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#conversão HSL
img_hsl = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

plt.imshow(img_rgb)
plt.title('RGB')
plt.show()

plt.imshow(img_gray, cmap='gray')
plt.title('Escala de cinza')
plt.show()

plt.imshow(img_hsl)
plt.title('HSL')
plt.show()
