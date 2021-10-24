import cv2 as cv

img = cv.imread('F:/opencv_learning/photos/Doraemen.jpg')
cv.imshow('Doraemen',img)

def rescaleFrame(frame,scale = 0.75):
    #photos videos live videos
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def changeRes(width,height):
    #Live Video Only
    capture.set(3,width)
    capture.set(4,height)

#resize your photo
resize_img = rescaleFrame(img,.3)
cv.imshow('resized photo',resize_img)

#Reading videos
capture = cv.VideoCapture('F:\opencv_learning\photos/video2.mp4')
#capture = cv.VideoCapture(0) get your camo

while True:
    isTrue,frame = capture.read()

    frame_resize = rescaleFrame(frame,.5)

    cv.imshow("video",frame)

    cv.imshow("rescale_video",frame_resize)

    if cv.waitKey(50) & 0xff == ord('q'):
      break

capture.release()
cv.destroyAllWindows()