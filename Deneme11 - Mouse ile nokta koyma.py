import cv2
import numpy as np
resm = np.zeros((512,512,3), np.uint8)
def draw (event, x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        resm[y,x] =[255,255,255]
    pass
cv2.namedWindow("Paint")
cv2.setMouseCallback("Paint", draw)
while(1):
        cv2.imshow("Kara Tahta", resm)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
cv2.destroyAllWindows()