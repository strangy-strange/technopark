import cv2
cap = cv2.VideoCapture (0)
while True :
    ret, frame = cap.read()
    frame_HSV = cv2.cvtColor( frame, cv2.COLOR_BGR2HSV )
    clr_low = (60, 110, 110,)
    clr_high = (120, 255, 255)
    frame_clr = cv2.inRange( frame_HSV, clr_low, clr_high)
    cv2.imshow('main', frame )
    frame[frame_clr==255]=(100, 0, 200)
    cv2.imshow('ch', frame )
    cv2.imshow ('frame mask', frame_clr)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
    
