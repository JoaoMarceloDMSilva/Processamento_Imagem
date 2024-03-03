import cv2
import numpy as np

# Função callback para o evento de mouse
def draw_circle(event, x, y):
    global drawing, color, ix, iy

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(frame, (x, y), 5, color, -1)
        cv2.circle(mask, (x, y), 5, color, -1)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.circle(frame, (x, y), 5, color, -1)
            cv2.circle(mask, (x, y), 5, color, -1)

# Carregar o arquivo de vídeo
video_path = 'videos/formatura_tg.mp4'
cap = cv2.VideoCapture(video_path)

# Verificar se o vídeo foi aberto corretamente
if not cap.isOpened():
    print("Erro ao abrir o vídeo.")
    exit()

# Definir as propriedades do vídeo
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Criar uma janela e associar a função de callback do mouse a ela
cv2.namedWindow('Video')
cv2.setMouseCallback('Video', draw_circle)

# Inicializar variáveis
drawing = False
color = (0, 0, 255)  # Inicialmente vermelho
ix, iy = -1, -1

# Criar uma máscara para armazenar os rabiscos
mask = np.zeros((height, width, 3), dtype=np.uint8)

# Loop principal
while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Aplicar a máscara no frame
    result = cv2.addWeighted(frame, 1, mask, 0.7, 0)

    # Exibir o resultado na janela
    cv2.imshow('Video', result)

    # Lidar com eventos do teclado
    key = cv2.waitKey(30)

    if key == 32:  # Tecla espaço para limpar os rabiscos
        mask = np.zeros((height, width, 3), dtype=np.uint8)

    elif key == ord('c'):  # Tecla 'c' para alterar a cor
        color = (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))

    elif key == 27:  # Tecla Esc para sair
        break

# Salvar o vídeo resultante
output_path = 'video_com_rascunhos.avi'
out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'DIVX'), fps, (width, height))
cap.release()

# Criar um novo vídeo com os rabiscos
cap = cv2.VideoCapture(video_path)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    result = cv2.addWeighted(frame, 1, mask, 0.7, 0)
    out.write(result)

# Liberar os recursos e fechar as janelas
cap.release()
out.release()
cv2.destroyAllWindows()
