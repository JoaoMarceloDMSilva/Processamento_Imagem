import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('images/clown.jpg',0)

new_width = 400

# Calcular a proporção de redimensionamento
ratio = new_width / img.shape[1]

# Calcular a nova altura com base na proporção
new_height = int(img.shape[0] * ratio)

# Redimensionar a imagem
resized_image = cv2.resize(img, (new_width, new_height))


dft = np.fft.fft2(img)
dft_shift = np.fft.fftshift(dft)

magnitude_spectrum = np.log(np.abs(dft_shift))/20

radius = 32
mask = np.zeros_like(img)
cy = mask.shape[0] // 2
cx = mask.shape[1] // 2
cv2.circle(mask, (cx,cy), radius, (255,255,255), -1)[0]
mask = 255 - mask
mask = cv2.GaussianBlur(mask, (19,19), 0)

dft_shift_masked = np.multiply(dft_shift,mask) / 255
back_ishift = np.fft.ifftshift(dft_shift)
back_ishift_masked = np.fft.ifftshift(dft_shift_masked)

img_filtered = np.fft.ifft2(back_ishift_masked)
img_filtered = np.abs(3*img_filtered).clip(0,255).astype(np.uint8)

resized_image_filtred = cv2.resize(img_filtered, (new_width, new_height))

plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1), plt.imshow(resized_image, cmap='gray')
plt.title('Imagem'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 2), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Espectro'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 3), plt.imshow(mask, cmap='gray')
plt.title('Máscara'), plt.xticks([]), plt.yticks([])
plt.show()

plt.imshow(resized_image_filtred, cmap='gray')
plt.title('Resultado'), plt.xticks([]), plt.yticks([])
plt.show()
