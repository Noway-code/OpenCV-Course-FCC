import cv2 as cv

img = cv.imread('Photos/cats.jpg')

cv.imshow('Park', img)
# Blur is applied by averaging the pixels in the kernel area. The larger the kernel, the more the blur.
# Values are taken from the surrounding pixels and averaged out to give the new pixel value.

# Averaging. The kernel is a square. The size of the kernel must be an odd number.
average = cv.blur(img, (7, 7))
cv.imshow('Average Blur', average)

# Gaussian Blur. Instead of averaging the pixels, the pixels are given different weights. This gives a more natural blur.

gauss = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur. The median value of the pixels in the kernel area is used as the new pixel value.
# This is effective in removing salt and pepper noise. Not great at removing Gaussian noise.
median = cv.medianBlur(img, 7)
cv.imshow('Median Blur', median)

# Bilateral. This is the most effective blur. It retains the edges of the image.
# It takes in the image, the diameter of the pixel neighborhood, the sigma color, and the sigma space.
# The diameter of the pixel neighborhood is the area around the pixel that will be used to average the pixel.
# The sigma color is the color space. The larger the sigma color, the more colors will be considered.
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)


cv.waitKey(0)
