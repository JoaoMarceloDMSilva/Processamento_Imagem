# Importa a biblioteca OpenCV
import cv2
# Importa a função randint da biblioteca random para gerar números aleatórios
from random import randint

# Define algumas cores usando a notação BGR (Blue, Green, Red)
BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)

# Lista de cores disponíveis
COLORS = [BLUE, GREEN, RED, BLACK, GRAY]

# Função de desenho de círculos em resposta a eventos do mouse
def draw_circle(event, x, y, flags, param):
    # Verifica se ocorreu um clique do botão esquerdo do mouse
    if event == cv2.EVENT_LBUTTONDOWN:
        # Escolhe uma cor aleatória da lista COLORS
        c = randint(0, len(COLORS) - 1)
        # Desenha um círculo na posição do clique com a cor escolhida
        cv2.circle(img, (x, y), 3, COLORS[c], -1)

# Carrega a imagem 'logo-if.jpg'
img = cv2.imread('logo-if.jpg')

# Cria uma janela chamada 'Logo IF' e associa a função draw_circle ao evento de mouse
cv2.namedWindow('Logo IF')
cv2.setMouseCallback('Logo IF', draw_circle)

# Loop principal para exibir a imagem e aguardar eventos de teclado
while True:
    # Exibe a imagem na janela 'Logo IF'
    cv2.imshow('Logo IF', img)
    
    # Aguarda 20ms pela pressão da tecla 'q' para sair do loop
    if cv2.waitKey(20) & 0xFF == ord('q'):
        # Salva a imagem com os círculos desenhados ao sair do loop
        cv2.imwrite('mouse.jpg', img)
        break

# Fecha todas as janelas ao sair do loop
cv2.destroyAllWindows()
