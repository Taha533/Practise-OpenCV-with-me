import cv2
import numpy as np

cap = cv2.VideoCapture('vtest.avi')
#fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
fgbg = cv2.createBackgroundSubtractorKNN(detectShadows=True)
#fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()

while (1):
    ret,frame =  cap.read()
    fg = fgbg.apply(frame)
    cv2.imshow("ForeGround",fg)
    cv2.imshow("Video", frame)

    if cv2.waitKey(30) & 0xff == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
