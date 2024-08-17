import cv2
import numpy as np
image = cv2.imread("people.jpg")
imagegray = cv2.imread("people.jpg",0)
print("Resmin Boyutu:", str(image.size))
print("Resmin Boyutu:", str(imagegray.size))
image[50,30] = [255,255,255]
cv2.imshow("deger", image)
cv2.waitKey(0)
cv2.destroyWindow()