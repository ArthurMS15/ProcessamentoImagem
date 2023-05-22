import cv2
import numpy as np
import matplotlib.pyplot as plt

# Leitura da imagem da Lena em cores
image = cv2.imread('lena.png')

# Conversão para escala de cinza
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicação de uma transformação não-linear (exemplo: inversão de intensidade)
transformed_image = 255 - gray_image

# Cálculo do histograma da imagem original e transformada
hist_original = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
hist_transformed = cv2.calcHist([transformed_image], [0], None, [256], [0, 256])

# Plotagem dos histogramas
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(hist_original, color='black')
plt.title('Histograma da Imagem Original')
plt.xlabel('Intensidade')
plt.ylabel('Frequência')

plt.subplot(1, 2, 2)
plt.plot(hist_transformed, color='black')
plt.title('Histograma da Imagem Transformada')
plt.xlabel('Intensidade')
plt.ylabel('Frequência')

# Exibição das imagens original e transformada
cv2.imshow('Imagem Original', gray_image)
cv2.imshow('Imagem Transformada', transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
