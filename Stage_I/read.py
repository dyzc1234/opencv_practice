import cv2 as cv

# img = cv.imread('F:/opencv_learning/photos/Doraemen.jpg')

# cv.imshow('Doraemen',img)

# cv.waitKey(0)

capture = cv.VideoCapture('F:/opencv_learning/photos/video2.mp4')

while True:
    success,frame = capture.read()

    cv.imshow("video",frame)

    if 0xff == ord('q'):
      break

capture.realease()
cv.destroyAllWindows()