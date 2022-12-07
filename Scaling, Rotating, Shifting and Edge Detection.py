import cv2
import numpy as np

#creating translation Matrix
M = np.float32([[1,0,150],[0,1,200]])
try:
    img = cv2.imread("lena.jpg")
    print(f"Image Shape: {img.shape}")
    cv2.imshow("Original Image", img)
    edges = cv2.Canny(img,100,200)
    #height,width = img.shape[:2]
    #rows, cols = img.shape[:2]
    #M = cv2.getRotationMatrix2D((cols/2,rows/2), 45, 1)
    #res = cv2.warpAffine(img,M,(cols,rows))
    #res = cv2.resize(img, (int(width/2),int(height/2)),interpolation= cv2.INTER_CUBIC)
    #cv2.imwrite("result.jpg",res)
    print(f"Resized Image Shape: {edges.shape}")
    cv2.imshow("Canny Edges", edges)

    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()

except IOError:
    print("Error while reading Files!!")

