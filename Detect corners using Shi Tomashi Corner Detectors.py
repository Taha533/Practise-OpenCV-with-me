import cv2
import numpy as np
img = cv2.imread("pic1.png")
cv2.imshow("img",img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray,100,0.01,10)
corners = np.int0(corners)
for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,(255,0,0),-1)
cv2.imshow("Shi Tomashi Corners",img)
if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()