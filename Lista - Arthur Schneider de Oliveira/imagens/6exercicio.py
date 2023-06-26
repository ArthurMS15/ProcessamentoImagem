import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('mask1.png')
img2 = cv2.imread('mask2.png')

# Verificar se as imagens são iguais
if np.array_equal(img1, img2):
    print("As imgs são iguais.")
else:
    print("As imgs são diferentes.")
    img_diff = cv2.subtract(img1, img2)

    plt.imshow(img_diff)
    plt.title('Diferença entre as imagens')
    plt.show()
