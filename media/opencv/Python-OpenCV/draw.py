import cv2 as cv
import numpy as np
black = np.zeros((500,500,3),dtype='uint8')
# cv.imshow("Black",black)

# todo: vẽ tất cả
# black[200:300, 300:400]=255,0,0
# cv.imshow("Blue",black)

# todo: vẽ hình vuông
cv.rectangle(black,(0,0),(100,100),(10,50,30),thickness=3)
cv.imshow('img',black)


















cv.waitKey(0)
# https://www.youtube.com/watch?v=oXlwWbU8l2o&t=1569s
