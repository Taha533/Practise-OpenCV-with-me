import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("pic2.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

kernel = np.ones((5,5), np.float32)/25

dst = cv2.filter2D(img,-1,kernel)
blur = cv2.blur(img,(5,5))
gblur = cv2.GaussianBlur(img,(5,5),0)
medianblur = cv2.medianBlur(img,5,)
bilateralfilter = cv2.bilateralFilter(img,9,75,75)

titles = ["image","2D Convolution","blur","gblur","medianblur","bilateralfilter"]
images = [img,dst,blur,gblur,medianblur,bilateralfilter]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()