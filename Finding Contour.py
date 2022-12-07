import cv2
import numpy as np
img2 = cv2.imread("Finding Contour.jpg",cv2.IMREAD_COLOR)
img = cv2.imread("Finding Contour.jpg",cv2.IMREAD_GRAYSCALE)

_,thresh = cv2.threshold(img,110,255,cv2.THRESH_BINARY)
contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    epsilon = 0.009*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)
    cv2.drawContours(img2,[approx],0,(0,0,255),5)
    i = 0
    n = approx.ravel()
    for j in n:

        if i%2 == 0:
            x = n[i]
            y = n[i+1]
            text = str(x) + " " + str(y)

            if i == 0:
                cv2.putText(img2,"Arrow Tip",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0))
            else:
                cv2.putText(img2,text,(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0))

        i+=1

cv2.imshow("Image",img2)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()