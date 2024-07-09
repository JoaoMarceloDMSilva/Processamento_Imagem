import cv2
import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv
import numpy as np

def resize_image(image, scale_percent):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

img = cv.imread('images/pdi_u.png', 0)
# assert img is not None, "file could not be read, check with os.path.exists()"

kernel_dilatation = np.array([
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [1, 1, 1, 1, 1],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],], dtype=np.uint8)

kernel_erosion = np.array([
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],], dtype=np.uint8)

borda = np.array([
                [0, 0, 1, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],], dtype=np.uint8)

step_1_erosion = cv.erode(img,kernel_erosion,iterations = 100)
dilation = cv.dilate(step_1_erosion,borda,iterations = 100)

scale_percent = 50
img_resized = resize_image(img, scale_percent)
erosion_resized = resize_image(step_1_erosion, scale_percent)
dilate_resized = resize_image(dilation, scale_percent)
cv2.imshow("Imagem", img_resized)
cv2.imshow("Erosion", erosion_resized)
cv2.imshow("Dilated", dilate_resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
