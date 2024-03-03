import cv2
import numpy as np

def ajustar_brilho_contraste(img, brilho, contraste):
    # Ajusta o brilho e contraste da imagem
    img = cv2.convertScaleAbs(img, alpha=contraste, beta=brilho)
    return img

def aplicar_efeito_negativo(img):
    # Inverte os valores dos pixels para criar o efeito negativo
    img_negativo = cv2.bitwise_not(img)
    return img_negativo

# Carrega uma imagem
imagem = cv2.imread('images/woman.jpg')

# Inicializa os valores de brilho e contraste
brilho = 0
contraste = 1.0

while True:
    # Aplica os ajustes de brilho e contraste
    imagem_ajustada = ajustar_brilho_contraste(imagem, brilho, contraste)

    # Exibe a imagem resultante
    cv2.imshow('Imagem Ajustada', imagem_ajustada)

    # Captura e processa os comandos de teclado
    key = cv2.waitKey(1)
    if key == ord('a'):  # Aumenta o brilho
        brilho += 10
    elif key == ord('z'):  # Diminui o brilho
        brilho -= 10
    elif key == ord('s'):  # Aumenta o contraste
        contraste += 0.1
    elif key == ord('x'):  # Diminui o contraste
        contraste -= 0.1
    elif key == ord('n'):  # Aplica o efeito negativo
        imagem = aplicar_efeito_negativo(imagem)
        print('Efeito negativo aplicado')

    elif key == 27:  # Tecla 'ESC' para fechar a janela
        break

# Libera os recursos
cv2.destroyAllWindows()
