import cv2
img = cv2.imread("lena.jpg",1)
img = cv2.line(img,(0,0),(255,255),(0,255,0),5)
img = cv2.arrowedLine(img,(0,255),(255,255),(255,0,0),5)
img = cv2.rectangle(img,(384,0),(510,128),(0,0,255),5)
img = cv2.circle(img,(447,63),63,(0,255,0),-1)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,"OpenCV",(10,500),font,4,(255,255,255),10,cv2.LINE_AA)

cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()