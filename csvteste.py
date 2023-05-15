import numpy as np
import matplotlib.pyplot as plt

# Ler o arquivo CSV
image_data = np.genfromtxt('caminho/para/seu/arquivo.csv', delimiter=',')

# Normalizar a matriz para a faixa de 0 a 1
image_data = (image_data - np.min(image_data)) / (np.max(image_data) - np.min(image_data))

# Salvar a matriz como uma imagem em escala de cinza
plt.imsave('caminho/para/sua/imagem.png', image_data, cmap='gray')
