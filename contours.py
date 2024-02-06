import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')

cv.imshow('cats', img)

# img.shape is a tuple of the height, width of img.
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

# Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# # Blur
# blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
#
# Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

# ret, thresh = cv.threshold(canny, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)

# Retr_List retrieves all the contours, but does not create any parent-child relationship. CHAIN_APPROX_SIMPLE removes redundant points.
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# contours is a list of contours. A contour is a numpy array of (x, y) coordinates of boundary points of the object.
# hierarchies is a numpy array of 4 values. The first value is the index of the next contour at the same hierarchical level.
# The second value is the index of the previous contour at the same hierarchical level. The third value is the index of the first child contour.
# The fourth value is the index of the parent contour.
# chain approximation method removes redundant points. It compresses the contour, saving only the endpoints.

# f'{}' is an f-string. It is used to format strings. {} can format any value. It is used to insert values into strings. (like str()).
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Contours Drawn', blank)
cv.waitKey(0)
