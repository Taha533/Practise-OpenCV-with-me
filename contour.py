import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("Irregular Shape3.png")
height = img.shape[0]
width = img.shape[1]

mask = np.zeros((height, width), dtype=np.uint8)
points = np.array([[[251,405],[243,327],[169,308],[200,207],[354,226],[410,322],[345,385],[251,405]]])
cv2.fillPoly(mask, points, (255))

res = cv2.bitwise_and(img,img,mask = mask)

rect = cv2.boundingRect(points) # returns (x,y,w,h) of the rect
cropped = res[rect[1]: rect[1] + rect[3], rect[0]: rect[0] + rect[2]]
print(rect)

cv2.imshow("cropped" , cropped )
cv2.imshow("same size" , res)
img_crop = cv2.cvtColor(cropped,cv2.COLOR_BGR2RGB)
plt.imshow(img_crop)
plt.savefig("Black dots.png")
plt.show()
cv2.waitKey(0)