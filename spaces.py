import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

# plt.imshow(img)
# plt.show()
# # Convert to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)
#
# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)
# HSV is a color space that represents hue, saturation, and value. It is often used in color detection.

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('LAB', lab)
# L*a*b is a color space that represents lightness, green-red, and blue-yellow.

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)
# BGR to RGB. In OpenCV, the default color space is BGR. In other libraries, the default color space is RGB.
# We use BGR in OpenCV because it was the default color space for the Windows operating system when OpenCV was created.

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)
plt.imshow(rgb)
plt.show()
# Now its in RGB color space. The image is displayed in a window and in a plot. OpenCV now shows the image in RGB color space ( so it looks inverted).

# you cant convert to grayscale and then convert to color space. You have to convert to color space first and then convert to grayscale.

hsv_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('HSV to BGR', hsv_bgr)


cv.waitKey(0)
