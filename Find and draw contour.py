import numpy as np
import cv2

img = cv2.imread("opencv-logo.png")
imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imggray,127,255,0)
contour,hierarchy = cv2.findContours(imggray,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print("Length of Contour =" + str(len(contour)))
print(contour[0])

cv2.drawContours(img,contour,-1,(0,255,0),3)

cv2.imshow("Image",img)
cv2.imshow("Image Gray",imggray)
cv2.waitKey(0)
cv2.destroyAllWindows()