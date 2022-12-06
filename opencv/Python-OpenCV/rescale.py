import cv2 as cv

img = cv.imread('Photos/1.jpg')


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

cv.imshow("Scale", rescaleFrame(img,0.5))
cv.waitKey(0)



# capture = cv.VideoCapture('Videos/1.mp4')

# while True:
#     isTrue, frame = capture.read()
#     frame_scale = rescaleFrame(frame)
#     cv.imshow("Video", frame)
#     cv.imshow("Scale",frame_scale)
#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()
