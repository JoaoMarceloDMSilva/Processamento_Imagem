import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('images/clown.jpg', 0)

new_width = 400

# Calcular a proporção de redimensionamento
ratio = new_width / img.shape[1]

# Calcular a nova altura com base na proporção
new_height = int(img.shape[0] * ratio)

# Redimensionar a imagem
resized_image = cv2.resize(img, (new_width, new_height))

dft = np.fft.fft2(img)
dft_shift = np.fft.fftshift(dft)

magnitude_spectrum = np.log(np.abs(dft_shift)) / 20

# Criar a máscara
mask = np.ones_like(img) * 255

# Coordenadas dos pontos a serem removidos da máscara
points = [(596, 535), (511, 586), (533, 548), (575, 572)]

# Remover os pontos da máscara
for point in points:
    cv2.circle(mask, point, radius=7, color=0, thickness=-1)

# Aplicar um desfoque gaussiano à máscara
mask = cv2.GaussianBlur(mask, (19, 19), 0)

# Aplicar a máscara invertida ao deslocamento da transformada de Fourier
dft_shift_masked = np.multiply(dft_shift, mask) / 255
back_ishift_masked = np.fft.ifftshift(dft_shift_masked)

# Filtrar a imagem na frequência
img_filtered = np.fft.ifft2(back_ishift_masked)
img_filtered = np.abs(img_filtered).clip(0, 255).astype(np.uint8)

# Redimensionar a imagem filtrada
resized_image_filtred = cv2.resize(img_filtered, (new_width, new_height))

# Exibir as imagens usando matplotlib
plt.figure(figsize=(15, 5))
plt.subplot(1, 4, 1), plt.imshow(resized_image, cmap='gray')
plt.title('Imagem'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 4, 2), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Espectro'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 4, 3), plt.imshow(mask, cmap='gray')
plt.title('Máscara'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 4, 4), plt.imshow(resized_image_filtred, cmap='gray')
plt.title('Resultado'), plt.xticks([]), plt.yticks([])
plt.show()
