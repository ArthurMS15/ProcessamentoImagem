import cv2
import matplotlib.pyplot as plt

# Carregando as imagens
img1 = cv2.imread('dental.jpeg',0) # 0 para carregar em escala de cinza
img2 = cv2.imread('parrot.jpeg',0) # 0 para carregar em escala de cinza
img3 = cv2.imread('skull.jpeg',0) # 0 para carregar em escala de cinza

# Lista de imagens
images = [img1, img2, img3]

# Títulos para os plots
titles = ['dental.jpeg', 'parrot.jpeg', 'skull.jpeg']

# Para cada imagem na lista de imagens
for i, img in enumerate(images):
    
    # Criando um objeto de equalização de histograma adaptativa
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

    # Aplicando a equalização de histograma adaptativa
    clahe_img = clahe.apply(img)

    # Plotando as imagens
    plt.figure(figsize=(10,4))
    
    plt.subplot(121)
    plt.imshow(img, cmap='gray')
    plt.title('Imagem original: '+titles[i])
    plt.axis('off')

    plt.subplot(122)
    plt.imshow(clahe_img, cmap='gray')
    plt.title('Imagem com CLAHE: '+titles[i])
    plt.axis('off')

    plt.tight_layout()
    plt.show()
