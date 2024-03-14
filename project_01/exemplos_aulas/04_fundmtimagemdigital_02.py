import cv2
import numpy as np
import random

# Carrega a imagem em escala de cinza
img = cv2.imread('logo-if.jpg', cv2.IMREAD_GRAYSCALE)

# Define a função para adicionar ruído de sal e pimenta
def add_noise(image, prob):
    output = np.zeros(image.shape, np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0  # ruído de sal
            elif rdn > thres:
                output[i][j] = 255  # ruído de pimenta
            else:
                output[i][j] = image[i][j]
    return output

# Chama a função para adicionar ruído à imagem
noisy_img = add_noise(img, 0.03)

# Exibe a imagem com ruído de sal e pimenta
cv2.imshow('Salt & Pepper', noisy_img)
 
# Aguarda até que uma tecla seja pressionada e, em seguida, fecha todas as janelas
cv2.waitKey(0)
cv2.destroyAllWindows()
