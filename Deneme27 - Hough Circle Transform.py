import cv2
import numpy as np

img = cv2.imread("daireler,.jpg")
img = cv2.medianBlur(img,5)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

min_dist = img.shape[0]/8
pt1 = 200
pt2 = 35
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, min_dist,
                           param1=pt1,param2=pt2,minRadius=0,maxRadius=0)
circles =  np.uint16(np.around(circles)) # float tipinde değer döndürdüğü için, (16 bitlik pozitif integer) ortalama bir değere yuvarlanır.
if circles is not None: # circles ların içi boş değilse devam et
    for x,y,r , in circles[0,:]: # sıfırıncı indeksinden tamamına kadar koordinat ve yarıçap değerlerini al
        cv2.circle(img,(x,y),r,(255,0,0),3) # daire tespitini çizdirme
        cv2.circle(img, (x,y), 2, (0,255,0), 3) # merkez noktasını çizdirme
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()