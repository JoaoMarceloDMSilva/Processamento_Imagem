# TAMANHO REAL DAS MOEDAS: https://www.bcb.gov.br/dinheirobrasileiro/segunda-familia-moedas.html

import cv2 as cv
import numpy as np

img = cv.imread("images/coins.png")
img_copy = img.copy()
img = cv.GaussianBlur(img, (7,7),3) # BORRA PARA REMOVER RUÍDOS
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray, 217, 255, cv.THRESH_BINARY) # CRIA A MÁSCARA

contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
img_copy = cv.drawContours(img_copy, contours, -1, (0, 255, 0), 3) # DESENHA OS CONTORNOS

area = {}
for i in range(len(contours)):
    cnt = contours[i]
    ar = cv.contourArea(cnt)
    area[i] = ar
srt = sorted(area.items(), key = lambda x : x[1], reverse = True)
results = np.array(srt).astype("int")
# print(results) # VALOR DAS BORDAS IDENTIFIADAS
num_coins = np.argwhere(results[:, 1]<= 44666).shape[0] # "<= 44666" PORQUÊ ACIMA DISSO É O VALOR DA IMAGEM
print(f"Há {num_coins} moeda(s) na imagem.")

# VISUALIZAR
# cv.imshow("Tresh",thresh)
# cv.imshow("Original", img)
cv.imshow("Contours", img_copy)
cv.waitKey(0)
cv.destroyAllWindows()