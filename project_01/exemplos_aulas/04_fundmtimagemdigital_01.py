# Importa a biblioteca OpenCV e a biblioteca NumPy
import cv2
import numpy as np
import random

# Carrega a imagem 'logo-if.jpg' em escala de cinza
img = cv2.imread('logo-if.jpg', cv2.IMREAD_GRAYSCALE)

# Define uma função para adicionar ruído de sal e pimenta à imagem
def noise(image, prob):
    # Cria uma matriz de zeros com a mesma forma que a imagem de entrada
    output = np.zeros(image.shape, np.uint8)
    # Calcula o limiar para determinar quando adicionar ruído de sal e pimenta
    thres = 1 - prob 
    # Loop sobre todos os pixels da imagem
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            # Gera um número aleatório entre 0 e 1
            rdn = random.random()
            # Se o número aleatório for menor que a probabilidade, adiciona ruído de sal
            if rdn < prob:
                output[i][j] = 0  # ruído de sal (pixel preto)
            # Se o número aleatório for maior que o limiar, adiciona ruído de pimenta
            elif rdn > thres:
                output[i][j] = 255  # ruído de pimenta (pixel branco)
            # Caso contrário, mantém o valor do pixel da imagem original
            else:
                output[i][j] = image[i][j]
    return output

# Chama a função noise para adicionar ruído de sal e pimenta à imagem com uma probabilidade de 0.03
noisy_img = noise(img, 0.03)

# Exibe a imagem com ruído de sal e pimenta em uma janela com o título 'Salt & Pepper'
cv2.imshow('Salt & Pepper', noisy_img)

# Aguarda até que uma tecla seja pressionada e, em seguida, fecha todas as janelas
cv2.waitKey(0)
cv2.destroyAllWindows()
