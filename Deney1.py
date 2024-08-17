import cv2
import numpy as np
resim = cv2.imread("people.jpg",0)
cv2.imshow("resim", resim)
k = cv2.waitKey(0)
if k == 27:
    print("ESC Tuşuna Basıldı")
elif k == ord("q"):
 print("q tuşuna basıldı, resim kaydedildi")
 cv2.imwrite("peoplegray.jpg",resim)
#cv2.destroyAllWindows()
