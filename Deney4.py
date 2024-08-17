import cv2
import numpy as np
cam = cv2.VideoCapture(0)
while cam.isOpened():
    _, frame = cam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([50,50,50])
    upper = np.array([70,255,255])
    mask = cv2.inRange(hsv, lower, upper)
    res  = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("pc kamerası",frame)
    cv2.imshow("hsv", mask)
    cv2.imshow("res", res)
    if cv2.waitKey(1) == ord("q"):
        print("görüntü sonlandırıldı")
        break
cv2.destroyAllWindows()