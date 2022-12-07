import numpy as np
import cv2

img = cv2.imread("cat_damaged.png")
mask = cv2.imread("cat_mask.png",0)

inpaint = cv2.inpaint(img,mask,3,cv2.INPAINT_NS)

cv2.imshow("Inpaint Image", inpaint)
cv2.imshow("Real Image", img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()