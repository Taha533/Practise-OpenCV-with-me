import  cv2
import numpy as np
def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        '''cv2.circle(img,(x,y),3,(0,0,255),-1)
        points.append((x,y))
        if len(points) >= 2:
            cv2.line(img,points[-1],points[-2],(0,255,0),5)'''
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]
        cv2.circle(img,(x,y),2,(0,255,0),-1)
        coloredimage =  np.zeros((512,512,3),np.uint8)
        coloredimage[:] = [blue,green,red]
        cv2.imshow("Selected Color",coloredimage)


points = []
#img = np.zeros((512,512,3),np.uint8)
img = cv2.imread("lena.jpg")
cv2.imshow("Image",img)
cv2.setMouseCallback("Image",click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
