import cv2
import numpy as np
def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, " , " ,y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + "," + str(y)
        cv2.putText(img,strXY,(x,y),font,0.5,(0,255,255),2)
        cv2.imshow("Image",img)

img = cv2.imread("messi5.jpg")
cv2.imshow("Image",img)
cv2.setMouseCallback("Image",click_event)

#cv2.waitkey(0)
#cv2.waitKey(0)
cv2.waitKey(0)
cv2.destroyAllWindows()