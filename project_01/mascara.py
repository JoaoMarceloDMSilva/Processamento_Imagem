import cv2

# Carregar a imagem em escala de cinza
image = cv2.imread('images/bear.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar o limiar
_, mask = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Exibir a máscara
cv2.imshow('Máscara', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
