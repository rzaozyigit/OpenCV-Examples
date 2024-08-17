import cv2
import numpy as np

image = cv2.imread("Tahtelbahirlogosiyah.png")
kernel = np.ones((5,5),np.uint8) # uint8 --> pozitif sayılardan oluşan 8 bitlik data türü

erosion  = cv2.erode(image,kernel,iterations=1)
dilation = cv2.dilate(erosion,kernel,iterations=1)

cv2.imshow("orjinal resim", image)
cv2.imshow("erosion", erosion)
cv2.imshow("dilation", dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()
