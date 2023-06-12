import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregando as imagens
img1 = cv2.imread('mask.jpeg', 0) # 0 para carregar em escala de cinza
img2 = cv2.imread('live.jpeg', 0) # 0 para carregar em escala de cinza

# Certifique-se de que as imagens têm a mesma forma
if img1.shape != img2.shape:
    print("As imagens devem ter a mesma forma!")
    exit()

# Calculando a diferença absoluta entre as duas imagens
diff = cv2.absdiff(img1, img2)

# Equalização do histograma na imagem de diferença
equ = cv2.equalizeHist(diff)

# Mostrando a imagem original e a equalizada
plt.figure(figsize=(10, 6))
plt.subplot(121), plt.imshow(diff, cmap='gray'), plt.title('Imagem de diferença')
plt.subplot(122), plt.imshow(equ, cmap='gray'), plt.title('Imagem equalizada')
plt.show()
