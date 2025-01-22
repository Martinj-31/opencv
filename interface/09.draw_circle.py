import numpy as np
import cv2

orange, blue, cyan = (0, 165, 255), (255, 0, 0), (255, 255, 0)
white, black, green, magenta = (255, 255, 255), (0, 0, 0), (0, 255, 0), (255, 0, 255)

image = np.full((400, 600, 3), white, np.uint8)             # 

center = (300, 200)         		# 
pt1, pt2 = (200, 100), (450, 300)
shade = (pt2[0] + 2, pt2[1] + 2)                          # 그림자 좌표

cv2.circle(image, center, 100, blue)                         #  
cv2.circle(image, pt1, 50, orange, 2)                        #
cv2.circle(image, pt2, 70, cyan, -1)                   #  

font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image, "Hello World", (200, 200), font, 1.0, green, 2)
cv2.putText(image, "OpenCV Rocks", (400, 200), font, 0.8, magenta, 2)
cv2.putText(image, "Circle Cyan", shade, font, 1.2, black, 2) # 그림자 효과
cv2.putText(image, "Circle Cyan", pt2, font, 1.2, cyan, 1)

title = "Draw circles"
cv2.namedWindow(title)
cv2.imshow(title, image)
cv2.waitKey(0)