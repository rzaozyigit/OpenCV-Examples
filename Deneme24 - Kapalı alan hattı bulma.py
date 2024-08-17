import cv2
import numpy as np
from random import randint as rnd #2 tane parametre girip o değerler arasında rastgele sayı veriyor
cam = cv2.VideoCapture(0)
kernel = np.ones((5,5),np.uint8)
while cam.isOpened():
    _, frame = cam.read()
    img = frame.copy()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([160,100,100])
    upper = np.array([180,255,255])
    mask  = cv2.inRange(hsv,lower,upper)
    mask  = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask  = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    res   = cv2.bitwise_and(frame,frame,mask=mask)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for i, cnt in enumerate(contours): # belli bir alanın hattını bulma
        area = cv2.contourArea(cnt)
        if area > 50000 or area <200: #cismin alanı 500x500 ile 20x20 piksel aralığında ise devam et
            continue
        x,y,w,h = cv2.boundingRect(cnt) # nesnenin koordinatlarını, genişlik ve yüksekliklerini bulmak için cnt listesini gönderiyoruz.
        print(x,y,w,h)
        color = (rnd(0,255), rnd(0,255), rnd(0,255)) #bu kod sayesinde rastgele renk değerleri görmüş oluruz
        cv2.drawContours(img, contours, i, color, 2, cv2.LINE_8,hierarchy,0) # bulduğumuz değerleri çizdiriyoruz.
        text = str((x,y)) 
        cv2.putText(img, text, (x,y), cv2.FONT_HERSHEY_COMPLEX, 1, color, 2)
    cv2.imshow("frame",frame)
    cv2.imshow("res", res)
    cv2.imshow("img", img)
    if cv2.waitKey(5) == ord("q"):
     print("görüntü sonlandırıldı")
     break
cam.release()
cv2.destroyAllWindows()