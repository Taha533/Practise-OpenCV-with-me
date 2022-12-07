import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("chessboard1.png")
cv2.imshow("img",img)
#plt.imshow(img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

dst = cv2.cornerHarris(gray,2,3,0.04)
dst = cv2.dilate(dst,None)
print(dst.max())
img[dst > 0.01 * dst.max()] = [0,0,255]
cv2.imshow("dst",img)
#plt.imshow(img)
#plt.show()

if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()