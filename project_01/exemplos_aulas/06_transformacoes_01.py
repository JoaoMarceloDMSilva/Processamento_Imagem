# coding=utf-8  # Define a codificação do arquivo como UTF-8

import cv2

# Carrega a imagem 'opencv_low.png'
img = cv2.imread('opencv_low.png')

# Calcula a nova largura e altura multiplicando as dimensões originais por 10
w, h = (int(10 * img.shape[0]), int(10 * img.shape[1]))

# Redimensiona a imagem usando o método de interpolação INTER_CUBIC
res1 = cv2.resize(img, (h, w), interpolation=cv2.INTER_CUBIC)

# Redimensiona a imagem usando o método de interpolação INTER_NEAREST
res2 = cv2.resize(img, (h, w), interpolation=cv2.INTER_NEAREST)

# Exibe as imagens redimensionadas em duas janelas separadas
cv2.imshow('res1', res1)
cv2.imshow('res2', res2)

# Aguarda até que uma tecla seja pressionada e, em seguida, fecha todas as janelas
cv2.waitKey(0)
cv2.destroyAllWindows()
