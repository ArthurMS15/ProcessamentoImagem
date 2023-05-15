import os
import matplotlib.pyplot as plt
import numpy as np

# Diretório contendo as imagens
dir_name = "C:/Users/Aluno/Desktop/teste" #caminhoparaodiretorio

# Obter uma lista de todos os arquivos no diretório
filenames = [f for f in os.listdir(dir_name) if os.path.isfile(os.path.join(dir_name, f))]

for filename in filenames:
    # Verificar se o arquivo é uma imagem (por exemplo, verificar a extensão do arquivo)
    if filename.lower().endswith(('.png')):
        # Ler o arquivo de imagem
        image = plt.imread(os.path.join(dir_name, filename))

        # Somar (100/255) unidades a cada pixel em cada canal de cor
        image_mod = np.clip(image + (100/255), 0, 1)

        # Salvar a imagem modificada
        new_filename = os.path.join(dir_name, f"mod_{filename}")
        plt.imsave(new_filename, image_mod)

