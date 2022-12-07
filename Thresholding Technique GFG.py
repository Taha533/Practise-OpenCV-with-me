import numpy as np
import cv2

image = cv2.imread("lena.jpg")
gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

ret,thresh1 = cv2.threshold(gray_img,120,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(gray_img,120,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(gray_img,120,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(gray_img,120,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(gray_img,120,255,cv2.THRESH_TOZERO_INV)

thresh_type = ['Real Image','Gray image','THRESH_BINARY','THRESH_BINARY_INV','THRESH_TRUNC','THRESH_TOZERO','THRESH_TOZERO_INV']
thresh_img = [image,gray_img,thresh1,thresh2,thresh3,thresh4,thresh5]

for i in range(len(thresh_type)):
    cv2.imshow(thresh_type[i],thresh_img[i])

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()