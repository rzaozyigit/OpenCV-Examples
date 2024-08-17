import cv2
image = cv2.imread("apple.jpeg",0)
image = cv2.blur(image,(3,3))
# Simple Thresholding
ret, thresh = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
# Adaptive Thresholding
thresh2 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,15,8)
thresh3 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,15,8)
cv2.imshow("Mean", image)
cv2.imshow("simple", thresh)
cv2.imshow("adaptive", thresh2)
cv2.imshow("adaptive2", thresh3)
cv2.waitKey(0)
cv2.destroyAllWindows()