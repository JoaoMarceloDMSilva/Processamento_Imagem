# Importação das bibliotecas necessárias
import cv2
import numpy as np

# Leitura das imagens
imagem1 = cv2.imread('bandeira_cxs.jpg')
imagem2 = cv2.imread('bandeira_ma.jpg')

# Definição da função para adicionar duas imagens pixel a pixel
def addImg(img1,img2):
    # Inicialização de uma imagem de resultado com zeros, no mesmo formato da primeira imagem
    res = np.zeros(img1.shape, np.uint8)
    
    # Loop para percorrer todos os pixels das imagens
    for y in range(0, img1.shape[0]):
        for x in range(0, img1.shape[1]):
            # Conversão dos valores dos pixels para int32 para evitar estouro de dados
            pixel1 = img1[y, x].astype(np.int32)
            pixel2 = img2[y, x].astype(np.int32)
            
            # Adição dos valores dos pixels, limitando o resultado entre 0 e 255
            res[y, x] = np.maximum(np.minimum(pixel1 + pixel2, (255, 255, 255)), (0, 0, 0))
    
    # Retorno da imagem resultante
    return res

# Criação de uma janela para exibir as operações
cv2.namedWindow('Operacoes')

# Definição do valor inicial para alpha
alpha = 0.5

# Loop principal
while(1):
    # Aplicação da operação de mistura ponderada (weighted) nas duas imagens
    result = cv2.addWeighted(imagem1, alpha, imagem2, (1.0 - alpha), 0)
    
    # Exibição das imagens e do resultado em janelas separadas
    cv2.imshow('Caxias', imagem1)
    cv2.imshow('Maranhão', imagem2)
    cv2.imshow('Operacoes', result)
    
    # Aguarda uma tecla ser pressionada
    k = cv2.waitKey(20)
    
    # Verifica se a tecla Esc (27) foi pressionada para encerrar o programa
    if k == 27:
        break
    # Verifica se a tecla 'a' foi pressionada para aumentar o valor de alpha
    elif k == ord('a'):
        alpha = min(alpha + 0.1, 1.0)
    # Verifica se a tecla 'z' foi pressionada para diminuir o valor de alpha
    elif k == ord('z'):
        alpha = max(alpha - 0.1, 0.0)

# Fecha todas as janelas ao sair do loop
cv2.destroyAllWindows()
