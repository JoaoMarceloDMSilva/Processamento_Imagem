import cv2

# Carregar o classificador em cascata Haar pré-treinado para detecção de faces
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Carregar a imagem em que as faces devem ser detectadas
# image = cv2.imread('images/messager.jpg') # minNeighbors=15, minSize=(40, 40)
image = cv2.imread('images/woman_and_crow.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detectar faces na imagem

# "scaleFactor": Este parâmetro especifica o quanto a imagem é reduzida em cada escala da imagem. 
# Um valor menor detecta mais detalhes, mas pode gerar mais falsos positivos.

# "minNeighbors": Especifica quantos vizinhos cada retângulo candidato precisa ter para ser considerado uma face. 
# Um número maior reduz falsos positivos, mas pode perder faces mais difíceis de detectar.

# "minSize": O tamanho mínimo para considerar uma face, definido em pixels.

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=15, minSize=(40, 40))

# Desenhar retângulos ao redor das faces detectadas
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Mostrar a imagem com as faces detectadas
cv2.imshow('Detected Faces', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
