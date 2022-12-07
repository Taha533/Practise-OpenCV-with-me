import cv2
import numpy as np

def nothing(x):
    print(x)

cv2.namedWindow("Image")
cv2.createTrackbar("cp", "Image", 10, 400, nothing)

switch = "Color/Gray"

cv2.createTrackbar(switch, "Image", 0, 1, nothing)

while (1):
    img = cv2.imread("lena.jpg")
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    pos = cv2.getTrackbarPos("cp", "Image")
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,str(pos),(50,150),font,6,(0,0,255),10)

    s = cv2.getTrackbarPos(switch, "Image")

    if s == 0:
        pass
    else:
       img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    cv2.imshow("Image", img)

cv2.destroyAllWindows()

