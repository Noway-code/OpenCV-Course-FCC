import cv2 as cv
import numpy as np

# Create a blank image
blank = np.zeros((500, 500, 3), dtype='uint8')  # uint8 is the data type for images, 3 is the number of channels (BGR),
# 500x500 is the size of the image, and 0 is the value of the pixels. np.zeros creates a black image.
cv.imshow('Blank', blank)  # Display the blank image

# blank[:] = 255, 255, 0  # Change the color of the image to green. [:] means the entire image.
# cv.imshow('Cyan', blank)  # Value in '' is the name of the window and blank is the image to be displayed.

# Draw a rectangle using the blank image
rectangle = np.zeros((500, 500, 3), dtype='uint8')
rectangle[200:300, 100:500] = 0, 0, 255  # Change the color of the image to red. [200:300, 300:400] is the region of the image to be changed.
cv.imshow('Gradient', rectangle)

# Draw a rectangle using a built-in function
cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=cv.FILLED)  # Draw a green rectangle on the blank image
cv.imshow('Rectangle', blank)



cv.waitKey(0)

