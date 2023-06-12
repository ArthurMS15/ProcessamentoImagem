import cv2
import numpy as np

# Carregar as imagens
img1 = cv2.imread('mask1.png', 0) # 0 para carregar em escala de cinza
img2 = cv2.imread('mask2.png', 0) # 0 para carregar em escala de cinza

# Verificar se as imagens têm a mesma forma
if img1.shape != img2.shape:
    print("As imagens têm formas diferentes. Elas não são iguais.")
else:
    # Verificar se as imagens são iguais
    difference = cv2.subtract(img1, img2)    # Subtrair os dois arrays
    result = not np.any(difference)          # se não houver nenhuma diferença, o resultado será True
    
    if result is True:
        print("As imagens são iguais.")
    else:
        print("As imagens não são iguais.")

# Calcular a diferença absoluta entre as duas imagens
diff = cv2.absdiff(img1, img2)

# Salvar a imagem da diferença
cv2.imwrite('diff.png', diff)
