import cv2
import numpy as np

# Carregar a imagem original
image = cv2.imread('imagem_original.jpg')

# Criar uma máscara onde as áreas a serem inpainted são brancas (255) e o resto é preto (0)
# Aqui assumimos que a máscara já está disponível; caso contrário, deve ser criada ou obtida
mask = cv2.imread('mascara.png', cv2.IMREAD_GRAYSCALE)

# Aplicar o método Telea de Inpainting
inpainted_image_telea = cv2.inpaint(image, mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)

# Aplicar o método Navier-Stokes de Inpainting
inpainted_image_ns = cv2.inpaint(image, mask, inpaintRadius=3, flags=cv2.INPAINT_NS)

# Mostrar as imagens
cv2.imshow('Imagem Original', image)
cv2.imshow('Máscara', mask)
cv2.imshow('Inpainting - Telea', inpainted_image_telea)
cv2.imshow('Inpainting - Navier-Stokes', inpainted_image_ns)

# Esperar por uma tecla e fechar as janelas
cv2.waitKey(0)
cv2.destroyAllWindows()
