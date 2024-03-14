# Importa a biblioteca OpenCV
import cv2

# Inicializa a captura de vídeo a partir do arquivo "IFMA Campus Caxias.mp4"
capture = cv2.VideoCapture("IFMA Campus Caxias.mp4")

# Obtém a largura, a altura e a taxa de quadros (FPS) do vídeo
frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)

# Imprime as informações obtidas
print("CV_CAP_PROP_FRAME_WIDTH: '{}'".format(frame_width))
print("CV_CAP_PROP_FRAME_HEIGHT : '{}'".format(frame_height))
print("CAP_PROP_FPS : '{}'".format(fps))

# Verifica se o vídeo foi aberto corretamente
if not capture.isOpened():
    print("Erro ao acessar a câmera")
else:
    # Define o codec de vídeo e inicializa o objeto de gravação de vídeo
    fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
    output = cv2.VideoWriter("video_cinza.avi", fourcc, int(fps), (int(frame_width), int(frame_height)), False)
    
    # Loop principal para processar e gravar os frames do vídeo
    while capture.isOpened():
        # Captura o próximo frame do vídeo
        ret, frame = capture.read()
        
        # Verifica se o frame foi capturado com sucesso
        if ret is True:
            # Converte o frame para escala de cinza
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Grava o frame em escala de cinza no arquivo de vídeo de saída
            output.write(gray)

            # Exibe o frame em escala de cinza em uma janela com o título 'Cinza'
            cv2.imshow('Cinza', gray)
            
            # Aguarda 20ms pela pressão da tecla 'q' para sair do loop
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

            # Aguarda 20ms pela pressão da tecla 'w' para salvar o frame atual como 'print.jpg'
            if cv2.waitKey(20) & 0xFF == ord('w'):
                print("Salvando frame...")
                cv2.imwrite('print.jpg', gray)
            
        else:
            break  # Sai do loop se não houver mais frames para capturar

# Libera o objeto de captura de vídeo e o objeto de gravação de vídeo
capture.release()
output.release()

# Fecha todas as janelas abertas pelo OpenCV
cv2.destroyAllWindows()
