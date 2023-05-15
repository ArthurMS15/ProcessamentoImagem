import numpy as np
import matplotlib.pyplot as plt

# Ler o arquivo de imagem em escala de cinza
filename = "imagemcolorida.png" #exercício 2: imagemcolorida.png
image = plt.imread(filename)

# Exibir a imagem original
plt.imshow(image)
plt.title('Imagem Original')
plt.show()

# Somar (100/255) unidades a cada pixel
image_mod = np.clip(image + (100/255), 0, 1)

# Exibir a imagem modificada
plt.imshow(image_mod)
plt.title('Imagem Modificada')
plt.show()

# Comparar as duas imagens lado a lado
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.imshow(image)
ax1.set_title('Imagem Original')
ax2.imshow(image_mod)
ax2.set_title('Imagem Modificada')
plt.show()

# Salvar a imagem modificada
new_filename = "imagemcolorida_mod.png" # exercício 2: imagemcolorida_mod.png
plt.imsave(new_filename, image_mod)
