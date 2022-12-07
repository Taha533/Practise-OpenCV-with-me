import numpy as np
import matplotlib.pyplot as plt
import cv2

x = np.random.uniform(0,1,100)*9
y = np.random.uniform(0,1,100)*9

plt.figure(figsize=(8,8))
plt.scatter(x,y,c = "black",s = 30)
#i = [(2.5,5),(4.5,4.5),(4.5,3),(4,2.5),(2.5,2),(2.5,5)]
irr_x = [2.5,5.8,7,5.6,3.6,3.4,1.8,2.5]
irr_y = [6.2,5.8,3.6,2.2,1.7,3.5,3.9,6.2]
plt.plot(irr_x,irr_y, "r-",linewidth = 3)
plt.savefig("Irregular Shape2.png")
plt.show()


# cropping image
'''import numpy as np
import matplotlib.pyplot as plt
import cv2
'''
img = cv2.imread("Irregular Shape3.png")
height = img.shape[0]
width = img.shape[1]

mask = np.zeros((height, width), dtype=np.uint8)
points = np.array([[[251,405],[243,327],[169,308],[200,207],[354,226],[410,322],[345,385],[251,405]]])
cv2.fillPoly(mask, points, (255))

res = cv2.bitwise_and(img,img,mask = mask)

rect = cv2.boundingRect(points) # returns (x,y,w,h) of the rect
cropped = res[rect[1]: rect[1] + rect[3], rect[0]: rect[0] + rect[2]]

#cv2.imshow("cropped" , cropped )
#cv2.imshow("same size" , res)
img_crop = cv2.cvtColor(cropped,cv2.COLOR_BGR2RGB)
#plt.imshow(img_crop)
plt.savefig("Black dots.png")
#plt.show()
#cv2.waitKey(0)

#counting points
path ="Black dots.png"
gray = cv2.imread(path, 0)
th, threshed = cv2.threshold(gray, 100, 255,
       cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
#findcontours
cnts = cv2.findContours(threshed, cv2.RETR_LIST,
                    cv2.CHAIN_APPROX_SIMPLE)[-2]

# filter by area
s1 = 3
s2 = 15
#s = 30
xcnts = []
for cnt in cnts:
    if s1<cv2.contourArea(cnt) <s2:
    #if cv2.contourArea(cnt)  == 7:
        xcnts.append(cnt)
print("\nDots number: {}".format(len(xcnts)))

N = 100
M = len(xcnts)
F = (M/N)* 64
print(f"Area of Irregular Figure: {F}")
