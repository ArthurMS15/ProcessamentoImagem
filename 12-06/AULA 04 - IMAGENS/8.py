import cv2
import matplotlib.pyplot as plt

# Carregando a imagem
img = cv2.imread('croppedBike.png',0) # 0 para carregar em escala de cinza

# Aplicando um filtro passa-baixa (filtro de média)
blur_img = cv2.blur(img, (5,5))

# Aplicando um detector de bordas (Canny)
edges = cv2.Canny(blur_img, 100, 200)

# Plotando as imagens
plt.figure(figsize=(15,5))

plt.subplot(131)
plt.imshow(img, cmap='gray')
plt.title('Imagem original')
plt.axis('off')

plt.subplot(132)
plt.imshow(blur_img, cmap='gray')
plt.title('Imagem com filtro de média')
plt.axis('off')

plt.subplot(133)
plt.imshow(edges, cmap='gray')
plt.title('Detecção de bordas com Canny')
plt.axis('off')

plt.tight_layout()
plt.show()
