# pylint:disable=no-member

import cv2 as cv

# img = cv.imread('../Resources/Photos/cat.jpg')
# cv.imshow('Cat', img)
# Reading Videos
capture = cv.VideoCapture(0)


def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    # Live video
    capture.set(2, width)
    capture.set(4, height)


changeRes(640, 480)  # Set resolution to 640x480

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
