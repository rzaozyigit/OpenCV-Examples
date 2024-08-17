import cv2
import numpy as np
resim = np.zeros((512,512,3), np.uint8)

cv2.line(resim,(0,0),(511,511),(120,50,45),5)
cv2.line(resim,(50,300),(100,500),(0,50,0),5)
cv2.rectangle(resim,(100,350),(50,300),[0,0,255],5)
resim[300,50]=[255,255,255]
cv2.imshow("Beyaz Kutu", resim)
print(resim[(300,50)])
cv2.waitKey(0)
cv2.destroyAllWindows()