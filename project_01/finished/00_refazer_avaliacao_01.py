import cv2
import numpy as np
import random

# Carregar o vídeo
video_path = 'videos/formatura_tg.mp4'
cap = cv2.VideoCapture(video_path)

# Verificar se o vídeo foi aberto corretamente
if not cap.isOpened():
    print("Erro ao abrir o vídeo.")
    exit()

# Obter as propriedades do vídeo
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Carregar a logomarca
logo_path = 'images/logo-if-vertical.png'
logo = cv2.imread(logo_path, cv2.IMREAD_UNCHANGED)
logo_height, logo_width, _ = logo.shape

# Calcular as novas dimensões da logomarca
new_logo_width = int(frame_width * 0.2)
new_logo_height = int((new_logo_width / logo_width) * logo_height)
new_logo = cv2.resize(logo, (new_logo_width, new_logo_height))

# Definir o intervalo para mudança de localização da marca d'água
change_location_interval = 100
current_frame = 0

# Loop para processar cada frame do vídeo
while True:
    # Ler um frame do vídeo
    ret, frame = cap.read()

    # Verificar se o frame foi lido corretamente
    if not ret:
        break

    # Verificar se é hora de mudar a localização da marca d'água
    if current_frame % change_location_interval == 0:
        # Gerar uma nova posição aleatória para a marca d'água
        new_x = random.randint(0, frame_width - new_logo_width)
        new_y = random.randint(0, frame_height - new_logo_height)

    # Criar uma máscara para a logomarca
    mask = new_logo[:, :, 3] / 255.0

    # Extrair os canais RGB da logomarca
    logo_rgb = new_logo[:, :, :3]

    # Copiar a região da imagem correspondente à logomarca
    roi = frame[new_y:new_y+new_logo_height, new_x:new_x+new_logo_width]

    # Aplicar a logomarca na imagem de forma ponderada
    frame[new_y:new_y+new_logo_height, new_x:new_x+new_logo_width] = (1 - mask[:, :, np.newaxis]) * roi + mask[:, :, np.newaxis] * logo_rgb

    # Exibir o frame processado
    cv2.imshow('Watermarked Video', frame)

    # Salvar o frame processado
    # writer.write(frame)

    # Aguardar 1 milissegundo. Pressione 'q' para sair
    if cv2.waitKey(15) & 0xFF == ord('q'):
        break

    # Atualizar o contador de frames
    current_frame += 1

# Liberar o objeto VideoCapture e fechar todas as janelas
cap.release()
cv2.destroyAllWindows()

