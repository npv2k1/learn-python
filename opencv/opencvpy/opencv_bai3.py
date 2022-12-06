import numpy as np
import cv2

img =cv2.imread('test.png',1)
#cv2.line(img,(0,0),(300,400),(10,20,38),10)
#cv2.imwrite('a.jpg',img)

#cv2.rectangle(img,(0,0),(200,200),(192,222,29),10)
# for i in range(0,200):
#     for j in range(0,10):
#         img[j,i]=1

#print(img[0,0,2])


#img2=img[0:200,0:200]

#print(img2.shape)
# B G R || RGB

print(img[0,0])
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()