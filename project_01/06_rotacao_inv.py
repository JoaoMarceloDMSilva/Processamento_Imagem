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

# Obter a matriz de rotação inversa
inverse_rotation_matrix = cv2.invertAffineTransform(rotation_matrix)

# Criar uma nova imagem vazia para armazenar a imagem rotacionada
rotated_image = np.zeros_like(image)

for y in range(height):
    for x in range(width):
        # Aplicar a transformação inversa para encontrar as coordenadas originais do pixel
        original_x = inverse_rotation_matrix[0, 0] * x + inverse_rotation_matrix[0, 1] * y + inverse_rotation_matrix[0, 2]
        original_y = inverse_rotation_matrix[1, 0] * x + inverse_rotation_matrix[1, 1] * y + inverse_rotation_matrix[1, 2]
        
        # Arredondar as coordenadas originais do pixel
        original_x = int(round(original_x))
        original_y = int(round(original_y))
        
        # Verificar se as coordenadas originais do pixel estão dentro dos limites da imagem original
        if 0 <= original_x < width and 0 <= original_y < height:
            # Copiar o pixel da imagem original para a posição correta na imagem rotacionada
            rotated_image[y, x] = image[original_y, original_x]

# Exibir a imagem rotacionada
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
