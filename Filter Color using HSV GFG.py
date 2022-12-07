import numpy as np
import cv2

#lower_blue = np.array([60,35,140])
#upper_blue = np.array([180,255,255])
def nothing(x):
    pass

cv2.namedWindow("Tracking")
cv2.createTrackbar("l_h","Tracking",0,255,nothing)
cv2.createTrackbar("l_s","Tracking",0,255,nothing)
cv2.createTrackbar("l_v","Tracking",0,255,nothing)

cv2.createTrackbar("u_h","Tracking",255,255,nothing)
cv2.createTrackbar("u_s","Tracking",255,255,nothing)
cv2.createTrackbar("u_v","Tracking",255,255,nothing)

while True:
    img = cv2.imread("smarties.png")
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lh = cv2.getTrackbarPos("l_h","Tracking")
    ls = cv2.getTrackbarPos("l_s","Tracking")
    lv = cv2.getTrackbarPos("l_v","Tracking")

    uh = cv2.getTrackbarPos("u_h","Tracking")
    us = cv2.getTrackbarPos("u_s", "Tracking")
    uv = cv2.getTrackbarPos("u_v", "Tracking")

    l_b = np.array([lh,ls,lv])
    u_b = np.array([uh,us,uv])
    mask = cv2.inRange(hsv, l_b, u_b)
    result = cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("Real Image", img)
    cv2.imshow("HSV",hsv)
    cv2.imshow("Filter Color",result)

    if cv2.waitKey(1) & 0xff == 27:
            break
cv2.destroyAllWindows()
