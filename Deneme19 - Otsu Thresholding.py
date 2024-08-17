import cv2
image = cv2.imread("apple.jpeg",0)

# Simple Thresholding
ret, thresh = cv2.threshold(image,127,255,cv2.THRESH_BINARY)

# Otsu Thresholding
ret2, thresh2 = cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("Orijinal",image)
cv2.imshow("Simple",thresh)
cv2.imshow("Otsu",thresh2)
print(ret2)

cv2.waitKey(0)
cv2.destroyAllWindows()