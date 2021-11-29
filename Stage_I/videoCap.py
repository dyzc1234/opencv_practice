import cv2 as cv


#Get Camera Data
capture = cv.VideoCapture(0)

while True:
    isTrue,frame = capture.read()
    cv.imshow('video data',frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()