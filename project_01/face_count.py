import cv2

# Carregar o classificador em cascata Haar pré-treinado para detecção de faces
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Capturar o vídeo da câmera (ou de um arquivo de vídeo)
# video_capture = cv2.VideoCapture("videos/formatura_tg.mp4")  # Use '0' para capturar da webcam ou o caminho do vídeo
video_capture = cv2.VideoCapture(0)
while True:
    # Capturar frame a frame
    ret, frame = video_capture.read()
    
    if not ret:
        break

    # Converter o frame para tons de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar faces no frame

    # Detectar faces na imagem

    # "scaleFactor": Este parâmetro especifica o quanto a imagem é reduzida em cada escala da imagem. 
    # Um valor menor detecta mais detalhes, mas pode gerar mais falsos positivos.

    # "minNeighbors": Especifica quantos vizinhos cada retângulo candidato precisa ter para ser considerado uma face. 
    # Um número maior reduz falsos positivos, mas pode perder faces mais difíceis de detectar.

    # "minSize": O tamanho mínimo para considerar uma face, definido em pixels.
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(10, 10))

    # Contar o número de faces detectadas
    num_faces = len(faces)

    # Desenhar retângulos ao redor das faces detectadas e mostrar o número de faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Mostrar o número de faces no frame
    cv2.putText(frame, f'Faces: {num_faces}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    # Exibir o frame com as detecções
    cv2.imshow('Video', frame)

    # Sair do loop com a tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar a captura e fechar as janelas
video_capture.release()
cv2.destroyAllWindows()
