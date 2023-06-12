import cv2
import matplotlib.pyplot as plt

# Carregando a imagem
img = cv2.imread('043.jpg',0) # 0 para carregar em escala de cinza

# Tamanhos de kernel para experimentar
kernels = [3, 5, 7]

# Para cada tamanho de kernel
for k in kernels:
    
    # Aplicando um filtro de média
    blur_img = cv2.blur(img, (k,k))
    
    # Aplicando um filtro de mediana
    median_img = cv2.medianBlur(img, k)
    
    # Aplicando um filtro gaussiano
    gauss_img = cv2.GaussianBlur(img, (k,k), 0)

    # Plotando as imagens
    plt.figure(figsize=(15,5))

    plt.subplot(131)
    plt.imshow(blur_img, cmap='gray')
    plt.title('Filtro de média com kernel {}'.format(k))
    plt.axis('off')

    plt.subplot(132)
    plt.imshow(median_img, cmap='gray')
    plt.title('Filtro de mediana com kernel {}'.format(k))
    plt.axis('off')

    plt.subplot(133)
    plt.imshow(gauss_img, cmap='gray')
    plt.title('Filtro gaussiano com kernel {}'.format(k))
    plt.axis('off')

    plt.tight_layout()
    plt.show()
