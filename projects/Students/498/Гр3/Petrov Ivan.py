import cv2
import numpy as np
cap = cv2.VideoCapture( 0 )

def findContour ( frame_mask, out ):
    cont, h = cv2.findContours( frame_mask,
                                cv2.RETR_TREE,
                                cv2.CHAIN_APPROX_SIMPLE)
    cont = sorted(cont, key = cv2.contourArea, reverse = True)
    cv2.drawContours ( out, cont, 0, (0,255,0), 2 )

while True:
    rt, frame = cap.read()
    frame_HSV = cv2.cvtColor (frame,
                              cv2.COLOR_BGR2HSV)
    clr_low = (0, 0, 110)
    clr_high = (180, 70, 255)

    frame_clr = cv2.inRange ( frame_HSV,
                              clr_low,
                              clr_high )
    frame_clr = np.where(frame_clr == 255, np.uint8(0), np.uint8(255))
    findContour ( frame_clr, frame)

    cv2.imshow('mask', frame_clr)
    cv2.imshow('main', frame)
    
    if cv2.waitKey(1) == ord('q'):
         break

cap.release()
cv2.destroyAllWindows()
