# Importa as bibliotecas OpenCV e NumPy
import cv2
import numpy as np

# Define algumas cores usando a notação BGR (Blue, Green, Red)
BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)

# Carrega a imagem 'logo-if.jpg'
img = cv2.imread('logo-if.jpg')

# Desenha uma linha na imagem
# cv2.line(img, ponto_inicial, ponto_final, cor, espessura)
# cv2.line(img, (0,0), (150,150), BLUE, 2)
# cv2.line(img, (200,100), (200,250), BLACK, 7)

# Desenha um retângulo na imagem
# cv2.rectangle(img, ponto_superior_esquerdo, ponto_inferior_direito, cor, espessura)
# cv2.rectangle(img, (250,150), (300,250), RED, 3)

# Desenha um círculo na imagem
# cv2.circle(img, centro, raio, cor, espessura)
# cv2.circle(img, (350,200), 50, GREEN, -1)

# Desenha um polígono na imagem
# pts = np.array([ponto1, ponto2, ponto3, ...], dtype=np.int32)
# cv2.polylines(img, [pts], fechado, cor, espessura)
# pts = np.array([(400,270),(370,234),(450,85),(380,10)], np.int32)
# cv2.polylines(img, [pts], True, GRAY, 3)

# Adiciona texto à imagem
# cv2.putText(img, texto, posição, fonte, tamanho_fonte, cor, espessura_linha, tipo_de_linha)
# cv2.putText(img, 'Txt1', (510, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, RED, 2, cv2.LINE_4)
# cv2.putText(img, 'Txt2', (510, 70), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, GREEN, 2, cv2.LINE_8)
# cv2.putText(img, 'Txt3', (510, 110), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.9, BLUE, 2, cv2.LINE_AA)

# Exibe a imagem com as formas e textos desenhados
cv2.imshow('Logo IF', img)

# Aguarda que uma tecla seja pressionada para fechar a janela
cv2.waitKey(0)

# Fecha todas as janelas ao sair do programa
cv2.destroyAllWindows()
