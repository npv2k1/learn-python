import cv2 as cv

def rescaleFrame(frame, scale=0.5):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('image.jpg', cv.IMREAD_GRAYSCALE)
img = rescaleFrame(img, 0.5)
# print(img.shape)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if (img[i][j]==255):
            print(0,end='')
        else:
            print(1,end='')
    print()
        

# cv.waitKey(0)

# capture = cv.VideoCapture('Videos/1.mp4')
# capture = cv.VideoCapture(0) # camera
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow("Video",frame)
#     if cv.waitKey(100) & 0xFF == ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()
