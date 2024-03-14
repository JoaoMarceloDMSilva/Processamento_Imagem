# Importa as bibliotecas necessárias
import cv2
import numpy as np

# Carrega a imagem 'ifma-caxias.jpg'
img = cv2.imread('ifma-caxias.jpg')

# Obtém as dimensões da imagem
rows, cols = img.shape[:2]

# Define a matriz de transformação para uma translação de (100, 50)
M = np.float32([[1, 0, 100], [0, 1, 50]])

# Aplica a transformação de translação usando a função warpAffine
# A terceira dimensão da matriz de transformação é a largura e altura da imagem de saída
res = cv2.warpAffine(img, M, (cols, rows))

# Exibe a imagem original e a imagem transformada
cv2.imshow('img', img)
cv2.imshow('res', res)

# Aguarda até que uma tecla seja pressionada e, em seguida, fecha todas as janelas
cv2.waitKey(0)
cv2.destroyAllWindows()
