#Log Transformation
import cv2
import numpy as np
img = cv2.imread("sample.jpg")

'''c = 255/(np.log(1+np.max(img)))
s = c*np.log(1+img)

log_transformed = np.array(s,dtype= np.uint8)
cv2.imshow("Image",img)
cv2.imshow("Log Transformed",log_transformed)
if cv2.waitKey(0) & 0xff == ord("q"):
    cv2.destroyAllWindows()'''

#Power-Law (Gamma) Transformation

g = [0.1,0.5,1.1,2.2]
for gamma in g:
    gamma_corrected = np.array(255*(img/255)**gamma, dtype= "uint8")
    cv2.imshow("Gamma Transformation" + str(gamma), gamma_corrected)

if cv2.waitKey(0) & 0xff == ord("q"):
    cv2.destroyAllWindows()