import cv2
import numpy as np
img = cv2.imread("model/satranc.jpg")
img_copy = img.copy()
gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 30, 50)
lines = cv2.HoughLines(edges, 1, np.pi/180, 150)
# lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, 0)
# if not isinstance(lines, type(None)):
#     for line in lines:
#         for x1,y1,x2,y2 in line:
#             cv2.line(img_copy, (x1,y1), (x2,y2), (0,0,255), 2)
if not isinstance(lines, type(None)): # Çizgillerin içi boş mu dolu mu kontrolü yapılır
   for line in lines:  # Tespit edilen tüm çizgileri tek tek çizdirme işlemi yapılır
       for rho, theta in line: # r ve theta değerleri yazılır
           a = np.cos(theta)
           b = np.sin(theta)
           x0 = a * rho
           y0 = b * rho
           x1 = int(x0 + 1000 * (-b))
           y1 = int(y0 + 1000 * (a))
           x2 = int(x0 - 1000 * (-b))
           y2 = int(y0 -    1000 * (a))
           cv2.line(img_copy, (x1,y1), (x2,y2), (0,0,255), 2)
cv2.imshow("orjinal", img)
cv2.imshow("Lines", img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()