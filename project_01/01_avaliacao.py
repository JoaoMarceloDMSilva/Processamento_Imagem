import cv2
import numpy as np
import random

def rescaleFrame(frame, scale: float = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[1] * scale)
    dimensions = (width, height)
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

def addImg(img1,img2):
    res = np.zeros(img1.shape, np.uint8)
    for y in range(0, img1.shape[0]):
        for x in range(0, img1.shape[1]):
            pixel1 = img1[y, x].astype(np.int32)
            pixel2 = img2[y, x].astype(np.int32)
            
            # Adição dos valores dos pixels, limitando o resultado entre 0 e 255
            res[y, x] = np.maximum(np.minimum(pixel1 + pixel2, (255, 255, 255)), (0, 0, 0))
    return res

# Unicamente para rodar o video (ruído 0.00)
def adicionar_ruido_sal_pimenta(imagem, proporcao_ruido):
    altura, largura, _ = imagem.shape
    ruido = np.random.rand(altura, largura)

    imagem_ruido = np.copy(imagem)
    imagem_ruido[ruido < proporcao_ruido / 2] = 0  
    imagem_ruido[ruido > 1 - proporcao_ruido / 2] = 255

    return imagem_ruido

caminho_imagem = "images/logo-if-vertical.png"
imagem = cv2.imread(caminho_imagem)
cv2.imshow("Out", imagem)
imagem_resize = rescaleFrame(imagem)
cv2.imshow("Img Menor",imagem_resize)
caminho_video = "videos/formatura_tg.mp4"
cap = cv2.VideoCapture(caminho_video)

intensidade_ruido = 0.00

while True:
    ret, frame = cap.read()

    if not ret:
        break
    frame_ruido = adicionar_ruido_sal_pimenta(frame, intensidade_ruido)

    # frame_com_img = addImg(frame_ruido, imagem_resize)
    # cv2.imshow('Video com Ruído', frame_com_img)
    cv2.imshow('Video com Ruído', frame_ruido)

    # Não utilizado
    key = cv2.waitKey(1)
    if key == ord('z'):  
        intensidade_ruido += 0.01
        print(f'Intensidade do ruído aumentada para {intensidade_ruido}')
    elif key == ord('x'): 
        intensidade_ruido = max(0, intensidade_ruido - 0.01)
        print(f'Intensidade do ruído diminuída para {intensidade_ruido}')
    elif key == ord('c'): 
        break

# Libera os recursos
cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
