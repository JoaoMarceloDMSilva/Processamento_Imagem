import cv2 as cv
import numpy as np

img = cv.imread("images/color_red.jpg")

# Convertendo a imagem para o espaço de cores HSV
img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
blur = cv.medianBlur(img_hsv, 7)

lower_color = np.array([0, 141, 77])
upper_color = np.array([179, 193, 215])


# lower_color = np.array([0, 16, 32])
# upper_color = np.array([179, 193, 215])


mask = cv.inRange(blur, lower_color, upper_color)
res = cv.bitwise_and(img, img, mask= mask)

# cv.imshow("Original", img)
cv.imshow("Filtrada", mask)
cv.imshow("Filtrada Vermelho", res)

cv.waitKey(0)
cv.destroyAllWindows()
