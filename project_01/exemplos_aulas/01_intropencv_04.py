# Importa a biblioteca OpenCV
import cv2

# Carrega a imagem 'logo-if.jpg' em cores (RGB) e armazena na variável 'img'
img = cv2.imread('logo-if.jpg', cv2.IMREAD_COLOR)

# Carrega a imagem 'logo-if.jpg' em escala de cinza e armazena na variável 'gray'
gray = cv2.imread('logo-if.jpg', cv2.IMREAD_GRAYSCALE)

# Imprime a forma (shape) e o tamanho (size) da imagem colorida 'img'
print(img.shape)  # Shape: retorna uma tupla representando as dimensões da imagem (altura, largura, número de canais)
print(img.size)   # Size: retorna o número total de pixels na imagem (altura x largura x número de canais)
print('=' * 20)

# Imprime a forma (shape) e o tamanho (size) da imagem em escala de cinza 'gray'
print(gray.shape)  # Shape: retorna uma tupla representando as dimensões da imagem (altura, largura)
print(gray.size)   # Size: retorna o número total de pixels na imagem em escala de cinza (altura x largura)

# Exibe a imagem colorida 'img' em uma janela com o título 'Logo IF'
cv2.imshow('Logo IF', img)

# Exibe a imagem em escala de cinza 'gray' em uma janela com o título 'Gray'
cv2.imshow('Gray', gray)

# Aguarda que uma tecla seja pressionada para fechar as janelas
cv2.waitKey(0)

# Fecha todas as janelas ao sair do programa
cv2.destroyAllWindows()
