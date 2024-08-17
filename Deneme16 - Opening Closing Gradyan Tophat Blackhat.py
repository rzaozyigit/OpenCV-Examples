import cv2
import numpy as np

image    = cv2.imread("Tahtelbahirlogosiyah.png")
kernel   = np.ones((5,5),np.uint8) # uint8 --> pozitif sayılardan oluşan 8 bitlik data türü
opening  = cv2.morphologyEx(image, cv2.MORPH_OPEN,kernel)
closing  = cv2.morphologyEx(image, cv2.MORPH_CLOSE,kernel)
gradyan  = cv2.morphologyEx(image, cv2.MORPH_GRADIENT,kernel)
tophat   = cv2.morphologyEx(image, cv2.MORPH_TOPHAT,kernel)
blackhat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT,kernel)

cv2.imshow("orjinal resim", image)
cv2.imshow("opening", opening)
cv2.imshow("gradyan", gradyan)
cv2.imshow("closing", closing)
cv2.imshow("tophat", tophat)
cv2.imshow("blackhat", blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()