import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("messi5.jpg", cv2.IMREAD_GRAYSCALE)

lap = cv2.Laplacian(img,cv2.CV_64F,ksize=3)
lap = np.uint8(np.absolute(lap))
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1)
canny = cv2.Canny(img,100,200)

sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))
sobelcombined = cv2.bitwise_or(sobelx,sobely)

#sobelcombined = np.uint8(np.absolute(sobelcombined))



titles = ["image","Laplacian","sobelx","sobely","sobelcombined","canny"]
images = [img,lap,sobelx,sobely,sobelcombined,canny]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()