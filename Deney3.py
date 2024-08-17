import cv2
cam = cv2.VideoCapture(0)
mahmut = cv2.VideoWriter_fourcc(*'XVID')
ismail = cv2.VideoWriter("video.avi", mahmut, 30.0,(500,500))
while True:
    ret, frame = cam.read()
    if not ret:
        print("kameradan görüntü okunamıyor")
        break
    ismail.write(frame)
    cv2.imshow("kamera",frame)
    if cv2.waitKey(1) == ord("q"):
        print("görüntü sonlandırıldı")
        break
cam.release()
cv2.destroyAllWindows()