import cv2 as cv

img = cv.imread('Photos/cats.jpg')

cv.imshow('cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding, we use a threshold value to classify the pixel values. we learned about this in a previous section.
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded', thresh)

# just like the previous threshold, but the inverse of the previous threshold. set values of less than 150 to 255 and values greater than 150 to 0.
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Inverse', thresh_inv)

# Adaptive Thresholding, the threshold value is calculated for smaller regions of the image.
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 9)
cv.imshow('Adaptive Thresholding', adaptive_thresh)
# The threshold value is the mean of the pixel values in the region minus the constant value.





cv.waitKey(0)
