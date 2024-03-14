# Importa a biblioteca OpenCV
import cv2

# Inicializa a captura de vídeo da câmera padrão (ID 0) ou de um arquivo de vídeo
# Substitua '0' pelo caminho do arquivo de vídeo, se desejar carregar um arquivo
capture = cv2.VideoCapture(0)
# capture = cv2.VideoCapture("IFMA Campus Caxias.mp4")

# Obtém a largura e a altura do frame do vídeo
frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("WIDTH: '{}'".format(frame_width))
print("HEIGHT : '{}'".format(frame_height))

# Verifica se a câmera ou o vídeo foi aberto corretamente
if not capture.isOpened():
    print("Erro ao acessar a câmera ou abrir o vídeo")
else:
    # Loop principal para capturar e exibir os frames
    while capture.isOpened():
        # Captura o frame atual
        ret, frame = capture.read()
        
        # Verifica se o frame foi capturado com sucesso
        if ret is True:
            # Exibe o frame original em uma janela com o título 'Input'
            cv2.imshow('Input', frame)
            
            # Converte o frame para escala de cinza
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Exibe o frame em escala de cinza em uma janela com o título 'Cinza'
            cv2.imshow('Cinza', gray)
            
            # Aguarda 20ms pela pressão das teclas 'q' ou 'w' para sair do loop ou salvar os frames
            key = cv2.waitKey(20)
            if key & 0xFF == ord('q'):  # Tecla 'q': fecha o programa
                break
            elif key & 0xFF == ord('w'):  # Tecla 'w': salva os frames como 'print.jpg' e 'gray.jpg'
                print("Salvando frame...")
                cv2.imwrite('print.jpg', frame)  # Salva o frame colorido
                cv2.imwrite('gray.jpg', gray)    # Salva o frame em escala de cinza
        else:
            break  # Se o frame não puder ser capturado, sai do loop

# Libera o objeto de captura de vídeo
capture.release()

# Fecha todas as janelas
cv2.destroyAllWindows()
