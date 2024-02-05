import cv2 as cv

# Reading Images
# img = cv.imread('Photos/cat_large.jpg')
#
# cv.imshow('Cat', img)
#
# cv.waitKey(0)  # 0 means wait for any key to be pressed before closing the window
#

# Reading Videos

# capture webcam
# capture = cv.VideoCapture(0)
# while True:
#     isTrue, frame = capture.read()
#
#     cv.imshow('Video', frame)
#
#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break
#
# capture.release()

# capture video file
# capture = cv.VideoCapture('Videos/dog.mp4')
# while True:
#     # isTrue is a boolean value that tells us if the frame was read successfully
#     # frame is the frame that was read from the video
#     isTrue, frame = capture.read()
#
#     cv.imshow('Video', frame)
#
#     # if the letter d is pressed, break out of the loop. 0xFF is a 64-bit number that is used to compare the key that was pressed
#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break
#
# capture.release()
# cv.destroyAllWindows()
# # video ran out of frames so it raised error Assertion Failed.


# Resizing and Rescaling
# We rescale so that the image or video fits on the screen and better for processing.
def rescale_frame(frame, scale=0.75):
    # Images, Videos and Live Videos
    # frame.shape[1] is the width of the image, frame.shape[0] is the height of the image
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    # dimensions is a tuple of the width and height
    dimensions = (width, height)
    # interpolation is the algorithm used to resize the image or video. cv.INTER_AREA is used to shrink the image or video.
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    # isTrue is a boolean value that tells us if the frame was read successfully
    # frame is the frame that was read from the video
    isTrue, frame = capture.read()

    frame_resized = rescale_frame(frame, scale=0.75)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    # if the letter d is pressed, break out of the loop. 0xFF is a 64-bit number that is used to compare the key that was pressed
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
