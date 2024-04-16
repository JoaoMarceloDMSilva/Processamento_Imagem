import cv2 as cv

img = cv.imread("images/woman.jpg")
cv.imshow("Sorcerer", img)
cv.waitKey(0)