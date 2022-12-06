import cv2 as cv
import numpy as np
img = cv.imread('love.png', 0)


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# print(img.shape)
img = rescaleFrame(img, 1)
# w=img.shape[1]
# h=img.shape[0]
# print(w)
# print(h)

# with open('arr.txt','w') as f:
#     for i in range(0,img.shape[0]):
#         for j in range(0,img.shape[1]):
#             if(img[i][j]!=0):
#                 f.write('{%s} : {%s} : {%s} \n' % (i, j, img[i][j]))


# for j in range(0, img.shape[1]):
#     for i in range(img.shape[0]-1,0,-1):
#         if(img[i][j] != 0):
#             f.write('{'+f'"x":{j} ,"y":{i}'+'},'+'\n')
#             break


a = set()
w = img.shape[1]
h = img.shape[0]

black = np.zeros((w, h, 3), dtype='uint8')


for x in range(0, w):
    for y in range(0, h):
        if(img[y][x] != 0):
            black[y][x] = 255, 0, 0
            a.add('{'+f'x:{x},y:{y}'+'},')
            break
for x in range(0, w):
    for y in range(h-1, 0, -1):
        if (img[y][x] != 0):
            black[y][x] = 255, 0, 0
            a.add('{'+f'x:{x},y:{y}'+'},')
            break
for y in range(0, h):
    for x in range(0, w):
        if(img[y][x] != 0):
            black[y][x] = 255, 0, 0
            a.add('{'+f'x:{x},y:{y}'+'},')
            break
for y in range(0, h):
    for x in range(w-1, 0, -1):
        if(img[y][x] != 0):
            black[y][x] = 255, 0, 0
            a.add('{'+f'x:{x},y:{y}'+'},')
            break

with open("c.txt",'w') as f:
    for i in a:
        f.write(i+'\n')

cv.imshow("black", black)


# x=0
# y=0
# with open('al.txt', 'w') as f:
#     for i in img:
#         x=0
#         for j in i:
#             if(j!=0):
#                 f.write('{'+f'"x":{x} ,"y":{y}'+'},'+'\n')
#                 break
#             x+=1
#         y+=1


print(img)

cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()
