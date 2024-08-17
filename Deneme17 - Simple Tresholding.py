import cv2
image = cv2.imread("apple.jpeg",0)

ret,thresh1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
#ret,thresh2 = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
#ret,thresh3 = cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
#ret,thresh4 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
#ret,thresh5 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)

cv2.imshow("orijinal Resim",image)
cv2.imshow("THRESH1",thresh1)
#cv2.imshow("THRESH2",thresh2)
#cv2.imshow("THRESH3",thresh3)
#cv2.imshow("THRESH4",thresh4)
#cv2.imshow("THRESH5",thresh5)

cv2.waitKey(0)
cv2.destroyAllWindows()