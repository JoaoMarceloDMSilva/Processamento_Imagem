import cv2
import numpy as np

img = cv2.imread('images/noise.jpg')

ksize=7

kernel = np.ones((ksize,ksize),np.float32)/(ksize*ksize)

median = cv2.medianBlur(img,ksize)


cv2.imshow('Img',img)
cv2.imshow('Median',median)

cv2.waitKey(0)
cv2.destroyAllWindows()