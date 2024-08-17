import cv2
import numpy as np
img = cv2.imread("conq.png",0)
cv2.imshow("foto",img)
k = cv2.waitKey(0)

if k==27:
    print("ESC tuşuna basıldı")
elif k==ord("q"):
    print("q tuşuna basıldı, fotoğraf kaydedildi")
    cv2.imwrite("conqgri.png",img)
#cv2.destroyAllWindows()