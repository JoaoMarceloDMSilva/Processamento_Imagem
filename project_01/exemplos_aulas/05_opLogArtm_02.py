# Importação das bibliotecas necessárias
import cv2
import numpy as np

# Carregamento das duas imagens a serem utilizadas
img1 = cv2.imread("drawing_1.png")
img2 = cv2.imread("drawing_2.png")

# Aplicação de operações bitwise entre as imagens

# Bitwise AND: realiza a operação AND bit a bit entre os pixels das duas imagens
bit_and = cv2.bitwise_and(img2, img1)

# Bitwise OR: realiza a operação OR bit a bit entre os pixels das duas imagens
bit_or = cv2.bitwise_or(img2, img1)

# Bitwise XOR: realiza a operação XOR bit a bit entre os pixels das duas imagens
bit_xor = cv2.bitwise_xor(img1, img2)

# Bitwise NOT: inverte os bits dos pixels da primeira imagem
bit_not = cv2.bitwise_not(img1)

# Bitwise NOT: inverte os bits dos pixels da segunda imagem
bit_not2 = cv2.bitwise_not(img2)

# Exibição das imagens e das operações bitwise realizadas em janelas separadas

# Exibição da primeira imagem
cv2.imshow("img1", img1)

# Exibição da segunda imagem
cv2.imshow("img2", img2)

# Exibição do resultado da operação bitwise AND
cv2.imshow("bit_and", bit_and)

# Exibição do resultado da operação bitwise OR
cv2.imshow("bit_or", bit_or)

# Exibição do resultado da operação bitwise XOR
cv2.imshow("bit_xor", bit_xor)

# Exibição do resultado da operação bitwise NOT aplicada à primeira imagem
cv2.imshow("bit_not", bit_not)

# Exibição do resultado da operação bitwise NOT aplicada à segunda imagem
cv2.imshow("bit_not2", bit_not2)

# Aguarda que uma tecla seja pressionada para fechar as janelas
cv2.waitKey(0)

# Fecha todas as janelas ao sair do programa
cv2.destroyAllWindows()
