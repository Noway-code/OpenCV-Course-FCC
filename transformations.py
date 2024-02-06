import os
import cv2 as cv
import numpy as np

os.environ["QT_QPA_PLATFORM"] = "xcb"

img = cv.imread('Photos/park.jpg')

cv.imshow('Park', img)


# Translation. x and y are the number of pixels to move the image in the x and y directions respectively.
def translate(img, x, y):
    # list of lists. matrix that will be used to translate the image
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    # img.shape[1] is the width of the image, img.shape[0] is the height of the image
    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, transMat, dimensions)


# x: - means left, + means right
# y: - means up, + means down

translated = translate(img, -5, -100)
cv.imshow('Translated', translated)


# Rotation. angle is the angle of rotation, scale is the scale of the image after rotation.
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    # // is floor division. rotPoint is the point around which the image will be rotated.
    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, -90)
cv.imshow('Rotated', rotated)

# Resizing, again
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping. 0 means flip vertically, 1 means flip horizontally, -1 means flip both vertically and horizontally.
flip = cv.flip(img, -1)
cv.imshow('Flip', flip)

# Cropping, again
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)




cv.waitKey(0)
