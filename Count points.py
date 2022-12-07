import cv2
# path ="C:/Users/Personal/Downloads/black dot.jpg"
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