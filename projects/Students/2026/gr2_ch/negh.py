import cv2
import numpy as np

cap = cv2.VideoCapture ( 0 )

while True:
    tr, frame = cap.read()
    frame_HSV = cv2.cvtColor (frame, cv2.COLOR_BGR2HSV)
    clr_low = ( 0, 210, 110 )
    clr_high = ( 15, 255, 255 )

    frame_clr = cv2.inRange( frame_HSV, clr_low, clr_high )


    cv2.imshow('mask', frame_clr)
    cv2.imshow('main', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()