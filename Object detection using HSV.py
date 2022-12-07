import cv2
import numpy as np

def nothing():
    pass
cap = cv2.VideoCapture(0)

cv2.namedWindow("Tracking")
cv2.createTrackbar("L_H","Tracking",0,255,nothing)
cv2.createTrackbar("L_S","Tracking",0,255,nothing)
cv2.createTrackbar("L_V","Tracking",0,255,nothing)

cv2.createTrackbar("U_H","Tracking",255,255,nothing)
cv2.createTrackbar("U_S","Tracking",255,255,nothing)
cv2.createTrackbar("U_V","Tracking",255,255,nothing)

while True:
    #frame = cv2.imread("smarties.png")
    ret,frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos("L_H","Tracking")
    l_s = cv2.getTrackbarPos("L_S", "Tracking")
    l_v = cv2.getTrackbarPos("L_V", "Tracking")

    u_h = cv2.getTrackbarPos("U_H", "Tracking")
    u_s = cv2.getTrackbarPos("U_S", "Tracking")
    u_v = cv2.getTrackbarPos("U_V", "Tracking")

    l_b = np.array([l_h,l_s,l_v])
    u_b = np.array([u_h,u_s,u_v])
    mask = cv2.inRange(hsv,l_b,u_b)
    res = cv2.bitwise_and(frame,frame,mask = mask)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", res)

    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
