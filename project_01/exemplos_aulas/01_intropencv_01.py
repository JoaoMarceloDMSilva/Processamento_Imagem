# Importação da biblioteca OpenCV
import cv2

# Carrega uma imagem do arquivo 'woman.jpg' e armazena na variável 'img'
img = cv2.imread('images/woman.jpg')

# Separa os canais de cor da imagem em azul (B), verde (G) e vermelho (R)
b, g, r = cv2.split(img)

# Exibe a imagem original em BGR (azul, verde, vermelho)
cv2.imshow('BGR', img)

# Exibe o canal de cor vermelho isolado
cv2.imshow('Red', r)

# Exibe o canal de cor verde isolado
cv2.imshow('Green', g)

# Exibe o canal de cor azul isolado
cv2.imshow('Blue', b)

# Mescla os canais de cor na ordem correta (RGB) e exibe a imagem resultante
res = cv2.merge([r, g, b])
cv2.imshow('RGB', res)

# Aguarda que uma tecla seja pressionada para fechar as janelas
cv2.waitKey(0)

# Fecha todas as janelas ao sair do programa
cv2.destroyAllWindows()
