import cv2 as cv

cap = cv.VideoCapture('videos/formatura_tg.mp4')

while cap.isOpened():
    ret, frame = cap.read()  # LER UM QUADRO
    if not ret:
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    
    edges = cv.Canny(gray, 100, 200) # APLICA CANNY

    cv.imshow('Canny Edges', edges) # VER

    
    if cv.waitKey(1) & 0xFF == ord('q'): # SAIR
        break

cv.destroyAllWindows()
