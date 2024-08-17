import cv2
camera = cv2.VideoCapture(0)
while True:
    ret, Frame = camera.read()
    cv2.rectangle(Frame,(250,50),(450,300),(0,255,102),5)
    cv2.putText(Frame,"Riza",(250,330),cv2.FONT_HERSHEY_DUPLEX,1,(0,255,102),2)
    cv2.imshow("Riza",Frame)
    if cv2.waitKey(1) == ord("q"):
        break
camera.release()
cv2.destroyAllWindows()