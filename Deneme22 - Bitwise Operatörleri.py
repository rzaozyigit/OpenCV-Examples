import cv2
import numpy as np
ilkresim = cv2.imread("ilk resim.png")
ikinciresim = cv2.imread("ikinci resim.png")
resim1 = cv2.resize(ilkresim, None, fx=0.3,fy=0.3)
resim2 = cv2.resize(ikinciresim, None, fx=0.3,fy=0.3)
bit_And = cv2.bitwise_and(resim1,resim2)
bit_Or  = cv2.bitwise_or(resim1,resim2)
bit_Xor = cv2.bitwise_xor(resim1,resim2)
bit_Not1 = cv2.bitwise_not(resim1)
bit_Not2 = cv2.bitwise_not(resim2)

cv2.imshow("ilk resim",resim1)
cv2.imshow("ikinci resim",resim2)
#cv2.imshow("And islemi",bit_And)
#cv2.imshow("Or islemi", bit_Or)
#cv2.imshow("Xor islemi", bit_Xor)
cv2.imshow("ilk resim Not islemi", bit_Not1)
cv2.imshow("ikinci resim Not islemi", bit_Not2)

cv2.waitKey(0)
cv2.destroyAllWindows()