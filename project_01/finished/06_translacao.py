import cv2
import numpy as np

# Carregar a imagem
image = cv2.imread('images/knight.jpg')

# Definir a quantidade de translação em pixels (horizontal, vertical)
tx = 50  # Translação horizontal
ty = 30  # Translação vertical

# Definir a matriz de translação
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])

# Aplicar a translação na imagem
translated_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))

# Exibir a imagem original e a imagem translatada
cv2.imshow('Original Image', image)
cv2.imshow('Translated Image', translated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
