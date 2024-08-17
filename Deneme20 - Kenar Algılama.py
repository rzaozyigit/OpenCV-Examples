import cv2
import numpy as np
image = cv2.imread("indir.png")
gray  = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur  = cv2.GaussianBlur(gray,(5,5),0)

canny = cv2.Canny(blur,75,225)

cv2.imshow("Original Image", image)
cv2.imshow("Blurred Image", blur)
cv2.imshow("Canny Image", canny)

cv2.waitKey(0)
cv2.destroyAllWindows()