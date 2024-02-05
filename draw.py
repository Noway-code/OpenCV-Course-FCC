import cv2 as cv
import numpy as np

# Create a blank image
blank = np.zeros((500, 500, 3), dtype='uint8')  # uint8 is image data type, 3 is the number of channels (BGR). np.zeros creates a black image.
# cv.imshow('Blank', blank)  # Display the blank image

# blank[:] = 255, 255, 0  # Change the color of the image to green. [:] means the entire image.
# cv.imshow('Cyan', blank)  # Value in '' is the name of the window and blank is the image to be displayed.

# Draw a rectangle using the blank image
# rectangle = np.zeros((500, 500, 3), dtype='uint8')
# rectangle[200:300, 100:500] = 0, 0, 255  # Change the color of the image to red. [200:300, 300:400] is the region of the image to be changed.
# cv.imshow('Gradient', rectangle)

# Draw a rectangle using a built-in function
cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=-1)  # dimension of half of the image

# Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=cv.FILLED)  # (blank.shape[1]//2, blank.shape[0]//2) is the center of the circle

# Draw a line
cv.line(blank, (100, 250), (300, 400), (255, 255, 255), thickness=2)  # (100, 250) is the starting point of the line, (300, 400) is the ending point of the line

# Write text.
cv.putText(blank, 'Hello, my name is Camilo', (0, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)  # (255, 255) is the starting point of the text
cv.imshow('Text', blank)

cv.waitKey(0)

