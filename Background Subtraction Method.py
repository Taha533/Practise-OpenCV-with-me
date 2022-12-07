import cv2 as cv
import numpy as np
cap = cv.VideoCapture("vtest.avi")

#fgbg = cv.bgsegm.createBackgroundSubtractorMOG()
#fgbg = cv.createBackgroundSubtractorMOG2(detectShadows=False)
#fgbg = cv.bgsegm.createBackgroundSubtractorGMG()
#kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(3,3))
fgbg = cv.createBackgroundSubtractorKNN(detectShadows=True)


while True:
    ret,frame = cap.read()
    if frame is None:
        break
    fgMask = fgbg.apply(frame)
    #fgMask = fgbg.apply(frame)
    #fgMask = cv.morphologyEx(fgMask,cv.MORPH_OPEN,kernel)

    cv.imshow("frame",frame)
    cv.imshow("FG Mask Frame",fgMask)
    keyword = cv.waitKey(30)
    if keyword == ord("q") or keyword == 27:
        break

cap.release()
cv.destroyAllWindows()