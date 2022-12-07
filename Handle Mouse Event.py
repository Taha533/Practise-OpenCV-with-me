import cv2
import numpy as np
def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, " , ",y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + " , " +str(y)
        cv2.putText(img,strXY,(x,y),font,0.5,(0,255,255),2)
        cv2.imshow("Image",img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(blue) + " , " + str(green) + " , " + str(red)
        cv2.putText(img, strXY, (x, y), font, 0.5, (0, 255, 255), 2)
        cv2.imshow("Image", img)

#img = np.zeros((512,512,3), np.uint8)
img = cv2.imread("lena.jpg")
cv2.imshow("Image",img)
cv2.setMouseCallback("Image",click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()