# Importa a biblioteca OpenCV
import cv2
import numpy as np

# Carrega a imagem original
img = cv2.imread('Aula 02/original.jpeg')

# Redimensiona a imagem para o tamanho desejado (350x505 pixels)
img = cv2.resize(img, (350, 505))

# Converte a imagem de BGR para HSV (Hue, Saturation, Value)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Cria uma cópia da imagem original para processamento
gray = img.copy()

# Obtém as dimensões da imagem (número de linhas e colunas)
(row, col) = img.shape[0:2]

# Loop sobre todos os pixels da imagem
for i in range(row):
    for j in range(col):
        # Verifica se o componente Hue (matiz) do pixel está fora do intervalo desejado (170-200)
        if (hsv[i, j][0] < 170) or (hsv[i, j][0] > 200):
            # Calcula o valor do pixel na imagem em tons de cinza
            gray[i, j] = sum(img[i, j]) * 0.33

# Exibe as imagens original, em HSV e o resultado final
cv2.imshow('Original', img)
cv2.imshow('HSV', hsv)
cv2.imshow('Result', gray)

# Aguarda até que uma tecla seja pressionada e, em seguida, fecha todas as janelas
cv2.waitKey(0)
cv2.destroyAllWindows()
