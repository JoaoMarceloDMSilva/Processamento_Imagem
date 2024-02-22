import cv2 as cv
import numpy as np

img = cv.imread("images/color_red.jpg")

img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
blur = cv.medianBlur(img_hsv, 7)

# FAIXA VERMELHA 
#[python get_color.py -i 'images/color_red.jpg' >> Selecionar costas mulher >> Tecla C]
lower_color = np.array([0, 141, 77])
upper_color = np.array([179, 193, 215])

# lower_color = np.array([0, 16, 32])
# upper_color = np.array([179, 193, 215])

mask = cv.inRange(blur, lower_color, upper_color)
res = cv.bitwise_and(img, img, mask= mask)


# Máscara inversa (negativa)
inverse_mask = cv.bitwise_not(mask)
cv.imshow("Máscara Vermelha Inversa", inverse_mask)


# BGR >> GRAY >> BGR
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Original", gray_img)
gray_img = cv.cvtColor(gray_img, cv.COLOR_GRAY2BGR)
# cv.imshow("Original", gray_img)

# MÁSCARA INVERSA + IMAGEM CINZA
final_img = cv.bitwise_and(gray_img, gray_img, mask=inverse_mask)

# VERMELHO ISOLADO
result = cv.add(final_img, res)

cv.imshow("Original", img)
cv.imshow("Filtrada Vermelho", res)
cv.imshow("Imagem Final", result)

cv.waitKey(0)
cv.destroyAllWindows()