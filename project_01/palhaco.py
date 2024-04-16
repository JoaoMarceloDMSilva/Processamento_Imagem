import cv2 as cv
import numpy as np

def frequency_spectrum(image):
    # Transformada de Fourier
    f_transform = np.fft.fft2(image)
    f_transform_shifted = np.fft.fftshift(f_transform)

    # IMPORTANTE PARA ACHAR AS FREQUÊNCIAS (NÃO PODE FALTAR)
    magnitude_spectrum = 20 * np.log(np.abs(f_transform_shifted))

    return magnitude_spectrum

# Carregamento da imagem

image = cv.imread('images/clown.jpg', 0)
# image = cv.imread('input_image.jpg', cv.IMREAD_GRAYSCALE)

# Calcula o espectro de frequência
magnitude_spectrum = frequency_spectrum(image)

# Exibe o espectro de frequência
cv.imshow('Frequency Spectrum', magnitude_spectrum.astype(np.uint8))
cv.waitKey(0)
cv.destroyAllWindows()