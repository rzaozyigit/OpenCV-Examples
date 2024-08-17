import cv2
import numpy as np
cam = cv2.VideoCapture(0)
kernel = np.ones((5,5),np.uint8)
while cam.isOpened():
    _, frame = cam.read()
    img = frame.copy()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    ret, thresh1 = cv2.threshold(hsv, 127, 255, cv2.THRESH_BINARY)
    gauss = cv2.GaussianBlur(ret,(5, 5),0)
    lower = np.array([160,100,100])
    upper = np.array([180,255,255])
    mask  = cv2.inRange(hsv,lower,upper)
    mask  = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask  = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    res   = cv2.bitwise_and(frame,frame,mask=mask)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        epsilon = 0.01 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)
        cv2.drawContours(img, [approx], 0, (0), 3)
        x, y = approx[0][0]
        if len(approx) == 3:
            cv2.putText(img, "Ucgen", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
        elif len(approx) == 4:
            cv2.putText(img, "Dortgen", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
        elif len(approx) == 5:
            cv2.putText(img, "Besgen", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
        elif 6 < len(approx) < 12   :
            cv2.putText(img, "Elips", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
        else:
            cv2.putText(img, "Daire", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
    cv2.imshow("frame", frame)
    cv2.imshow("res", res)
    cv2.imshow("img", img)
    if cv2.waitKey(5) == ord("q"):
     print("görüntü sonlandırıldı")
     break
cam.release()
cv2.destroyAllWindows()