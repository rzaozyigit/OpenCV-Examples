import cv2
image = cv2.imread("ab.png")
#meanfilter  = cv2.blur(image,(3,3))
#meanfilter2 = cv2.blur(image,(5,5))
#meanfilter3 = cv2.blur(image,(7,7))

#medianfilter  = cv2.medianBlur(image,3)
#medianfilter2 = cv2.medianBlur(image,5)
#medianfilter3 = cv2.medianBlur(image,7)

gauss = cv2.GaussianBlur(image,(3,3),0)
gauss2 = cv2.GaussianBlur(image,(5,5),0)
gauss3 = cv2.GaussianBlur(image,(15,15),0)

cv2.imshow("orjinal Resim", image)
#cv2.imshow("Mean Filter 3*3", meanfilter)
#cv2.imshow("Mean Filter 5*5", meanfilter2)
#cv2.imshow("MEan Filter 7*7", meanfilter3)

#cv2.imshow("Median Filter", medianfilter)
#cv2.imshow("Median Filter2", medianfilter2)
#cv2.imshow("Median Filter3", medianfilter3)

cv2.imshow("Gauss Filter ", gauss)
cv2.imshow("Gauss Filter2 ", gauss2)
cv2.imshow("Gauss Filter3", gauss3)

cv2.waitKey(0)
cv2.destroyAllWindows()
