import cv2
import numpy as np
 
img = cv2.imread('tp4-ia.png',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
 
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,140,
                            param1=80,param2=20,minRadius=20,maxRadius=30)
 
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # Dibuja la circusnferencia del círculo
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # dibuja el centro del círculo
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
 
cv2.imshow('círculos detectados',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()