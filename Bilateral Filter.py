import cv2
img = cv2.imread("taj.jpg")
bilateral = cv2.bilateralFilter(img,15,75,75)
blur = cv2.blur(img,(5,5))
gaussian = cv2.GaussianBlur(img,(5,5),0)
medianBlurr = cv2.medianBlur(img,5)

cv2.imshow("image",img)
cv2.imshow("Bilateral",bilateral)
cv2.imshow("Blur",blur)
cv2.imshow("Gaussian",gaussian)
cv2.imshow("medianBlurr",medianBlurr)

if cv2.waitKey(0) & 0xff == ord('q'):
    cv2.destroyAllWindows()
