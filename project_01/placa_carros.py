import cv2
import numpy as np

img = cv2.imread('images/placa_mercosul.jpg', cv2.IMREAD_GRAYSCALE)

def resize_image(image, scale_percent):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(image, dim, interpolation=cv2.INTER_AREA) 

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))

# Top Hat
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# Black Hat
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

scale_percent = 50 
img_resized = resize_image(img, scale_percent)
tophat_resized = resize_image(tophat, scale_percent)
blackhat_resized = resize_image(blackhat, scale_percent)

cv2.imshow('Original Image', img_resized)
cv2.imshow('Top Hat', tophat_resized)
cv2.imshow('Black Hat', blackhat_resized)

cv2.waitKey(0)
cv2.destroyAllWindows()