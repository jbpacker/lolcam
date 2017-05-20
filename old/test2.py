import numpy as np
import cv2

cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)

while(True):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    #less1 = cv2.fastNlMeansDenoisingColored(frame1,None,10,10,7,21)
    #less2 = cv2.fastNlMeansDenoisingColored(frame2,None,10,10,7,21)

    gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray_edge = cv2.Canny(gray, 100, 200)
    edges = cv2.Canny(frame2, 220, 210)

    cv2.imshow('gray_edge', gray_edge)
    cv2.imshow('frame', gray)
    cv2.imshow('wide', frame2)
    cv2.imshow('other', edges)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()
