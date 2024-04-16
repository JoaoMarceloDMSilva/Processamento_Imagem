# O PRESENTE ARQUIVO ESTÁ DIVIDIDO EM TRÊS QUESTÕES. 
# NÃO EXECUTE A QUESTÃO 03 SIMULTANEAMENTE ÀS DUAS PRIMEIRAS!

# #   QUESTÃO 1: FAÇA A REDUÇÃO DA RESOLUÇÃO DE UMA IMAGEM TOMANDO POR BASE A ELIMINAÇÃO DOS PIXELS DA VIZINHANÇA-8;
import cv2
import numpy as np

# Carregando a imagem
imagem = cv2.imread('images/woman.jpg')

# Fator de redução (Vale para as 2 QUESTÕES)
fator_reducao = 2

# Redução da resolução pela eliminação de pixels da vizinhança-8 [Numpy: Indexação Fancy]
imagem_reduzida = imagem[::fator_reducao, ::fator_reducao, :]

# Exibindo a imagem original e a imagem reduzida
cv2.imshow('Imagem Original', imagem)
cv2.imshow('Vizinhanca-8', imagem_reduzida)
# Remover comantário para testar individualmente
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#############################################################################
# QUESTÃO 2: FAÇA A REDUÇÃO DA RESOLUÇÃO DE UMA IMAGEM TOMANDO POR BASE A MÉDIA DOS PIXELS DA VIZINHANÇA-8;

altura, largura, canais = imagem.shape

# Criando uma imagem vazia com a metade das dimensões originais
nova_altura = altura // fator_reducao
nova_largura = largura // fator_reducao
imagem_reduzida = np.zeros((nova_altura, nova_largura, canais), dtype=np.uint8)

# Redução da resolução pela média dos pixels na vizinhança-8 (Vai demorar alguns segundos :/ )
for i in range(0, nova_altura):
    for j in range(0, nova_largura):
        for k in range(0, canais):
            vizinhos = [
                imagem[i * fator_reducao, j * fator_reducao, k],
                imagem[i * fator_reducao, (j * fator_reducao) + 1, k],
                imagem[(i * fator_reducao) + 1, j * fator_reducao, k],
                imagem[(i * fator_reducao) + 1, (j * fator_reducao) + 1, k]
            ]
            media = int(np.mean(vizinhos))
            imagem_reduzida[i, j, k] = media

# Exibindo a imagem original e a imagem reduzida
# cv2.imshow('Imagem Original', imagem)
cv2.imshow('Vizinhanca-8(Media)', imagem_reduzida)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ###############################################################################################
# ## QUESTÃO 03: APLIQUE UM EFEITO DE RUÍDO DO TIPO SAL E PIMENTA EM UM ARQUIVO DE VÍDEO OU IMAGEM DA WEBCAM, VARIANDO SUA INTENSIDADE
# ##             POR COMANDO DE TECLADO
# import cv2
# import numpy as np

# # Função para adicionar ruído sal e pimenta à imagem
# def adicionar_ruido_sal_pimenta(imagem, proporcao_ruido):
#     altura, largura, _ = imagem.shape
#     ruido = np.random.rand(altura, largura)

#     imagem_ruido = np.copy(imagem)
#     imagem_ruido[ruido < proporcao_ruido / 2] = 0  # Ruído de sal
#     imagem_ruido[ruido > 1 - proporcao_ruido / 2] = 255  # Ruído de pimenta

#     return imagem_ruido

# # Inicialização da webcam (caso esteja utilizando)
# cap = cv2.VideoCapture(0)

# # Leitura de um arquivo de vídeo
# # caminho_video = "videos/formatura_tg.mp4"
# # cap = cv2.VideoCapture(caminho_video)

# # Variável para controlar a intensidade do ruído
# intensidade_ruido = 0.02

# while True:
#     ret, frame = cap.read()

#     if not ret:
#         break

#     # Adiciona ruído à imagem
#     frame_ruido = adicionar_ruido_sal_pimenta(frame, intensidade_ruido)

#     # Exibe a imagem resultante
#     cv2.imshow('Video com Ruído', frame_ruido)

#     # Captura e processa os comandos de teclado
#     key = cv2.waitKey(1)
#     if key == ord('z'):  # Aumenta a intensidade do ruído
#         intensidade_ruido += 0.01
#         print(f'Intensidade do ruído aumentada para {intensidade_ruido}')
#     elif key == ord('x'):  # Diminui a intensidade do ruído
#         intensidade_ruido = max(0, intensidade_ruido - 0.01)
#         print(f'Intensidade do ruído diminuída para {intensidade_ruido}')
#     elif key == ord('c'):  # Fecha a janela
#         break

# # Libera os recursos
# cap.release()
# cv2.destroyAllWindows()
