import cv2
import numpy as np

# Carregar a imagem
image = cv2.imread('images/woman.jpg')

# Definir o ângulo de rotação em graus
angle = 45

# Obter as dimensões da imagem
height, width = image.shape[:2]

# Calcular o centro da imagem
center = (width // 2, height // 2)

# Criar a matriz de rotação
rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

# Criar uma nova imagem vazia para armazenar a imagem rotacionada
rotated_image = np.zeros_like(image)

# Aplicar a rotação pixel a pixel
for y in range(height):
    for x in range(width):
        # Transformar as coordenadas do pixel original
        rotated_x = rotation_matrix[0, 0] * x + rotation_matrix[0, 1] * y + rotation_matrix[0, 2]
        rotated_y = rotation_matrix[1, 0] * x + rotation_matrix[1, 1] * y + rotation_matrix[1, 2]
        
        # Arredondar as coordenadas do pixel rotacionado
        rotated_x = int(round(rotated_x))
        rotated_y = int(round(rotated_y))
        
        # Verificar se as coordenadas do pixel rotacionado estão dentro dos limites da nova imagem
        if 0 <= rotated_x < width and 0 <= rotated_y < height:
            # Copiar o pixel da imagem original para a posição correta na imagem rotacionada
            rotated_image[rotated_y, rotated_x] = image[y, x]

# Exibir a imagem rotacionada
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
