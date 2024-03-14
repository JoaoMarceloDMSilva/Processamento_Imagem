# Importa a biblioteca OpenCV
import cv2

# Carrega a imagem 'logo-if.jpg' e armazena na variável 'img'
img = cv2.imread('logo-if.jpg')

# Define uma região de interesse (ROI) na imagem original 'img'
# A região de interesse é definida pelos valores de corte [100:250, 0:150]
# Isso significa que estamos selecionando uma área retangular da imagem, 
# que vai da linha 100 à linha 250 e da coluna 0 à coluna 150
roi = img[100:250, 0:150]

# Exibe a região de interesse 'roi' em uma janela com o título 'Logo IF'
cv2.imshow('Logo IF', roi)

# Aguarda que uma tecla seja pressionada para fechar a janela
cv2.waitKey(0)

# Fecha todas as janelas ao sair do programa
cv2.destroyAllWindows()
