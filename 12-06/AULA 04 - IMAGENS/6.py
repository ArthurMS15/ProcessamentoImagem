import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregando as imagens
img1 = cv2.imread('bay.jpeg',0) # 0 para carregar em escala de cinza
img2 = cv2.imread('brain.jpeg',0) # 0 para carregar em escala de cinza
img3 = cv2.imread('moon.jpeg',0) # 0 para carregar em escala de cinza

# Lista de imagens
images = [img1, img2, img3]

# Títulos para os plots
titles = ['bay.jpeg', 'brain.jpeg', 'moon.jpeg']

# Para cada imagem na lista de imagens
for i, img in enumerate(images):

    # Equalizando o histograma
    equ = cv2.equalizeHist(img)

    # Calculando histogramas
    hist_orig = cv2.calcHist([img],[0],None,[256],[0,256])
    hist_equ = cv2.calcHist([equ],[0],None,[256],[0,256])

    # Plotando os histogramas
    plt.figure(figsize=(10,4))

    plt.subplot(121)
    plt.imshow(img, cmap='gray')
    plt.title('Imagem original: '+titles[i])
    plt.axis('off')

    plt.subplot(122)
    plt.imshow(equ, cmap='gray')
    plt.title('Imagem equalizada: '+titles[i])
    plt.axis('off')

    plt.figure(figsize=(10,4))
    
    plt.subplot(121)
    plt.plot(hist_orig)
    plt.title('Histograma original: '+titles[i])

    plt.subplot(122)
    plt.plot(hist_equ)
    plt.title('Histograma equalizado: '+titles[i])

    plt.tight_layout()
    plt.show()
