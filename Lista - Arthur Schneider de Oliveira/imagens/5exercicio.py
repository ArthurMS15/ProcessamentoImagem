import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('ifc_01.png')
img2 = cv2.imread('ifc_02.png')

#mesmo tamanho
if img1.shape != img2.shape:
    print("As imagens devem ter o mesmo tamanho para a operação AND")
else:
    # Realizar a operação lógica AND
    img_and = cv2.bitwise_and(img1, img2)

    # Imagem 1
    plt.imshow(img1)
    plt.title('Imagem 1')
    plt.show()

    # Imagem 2
    plt.imshow(img2)
    plt.title('Imagem 2')
    plt.show()

    # Imagem resultante
    plt.imshow(img_and, cmap='gray')
    plt.title('Imagem Resultante (AND)')
    plt.show()

