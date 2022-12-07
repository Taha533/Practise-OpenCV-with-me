import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
img = cv2.imread("bear.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,15)
'''cv2.imshow("Real Image",img)
cv2.imshow("Denoising Img",dst)'''
plt.subplot(121),plt.imshow(img)
plt.subplot(122),plt.imshow(dst)
#if cv2.waitKey(0) & 0xff == 27:
 #   cv2.destroyAllWindows()
plt.show()