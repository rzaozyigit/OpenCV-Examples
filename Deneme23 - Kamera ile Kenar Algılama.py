import cv2
import numpy as np
camera = cv2.VideoCapture(1)

while True:
    _, frame = camera.read()
    framegri = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frameblur = cv2.GaussianBlur(framegri,(5,5),0)
    canny = cv2.Canny(frameblur,25,225)
    cv2.imshow("kenar algılama",canny)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()