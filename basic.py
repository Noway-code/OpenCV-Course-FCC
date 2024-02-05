import cv2 as cv

img = cv.imread('Photos/park.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # BGR means Blue, Green, Red. This converts the image to grayscale.
cv.imshow('gray', gray)

# Blur. Takes in an image and a kernel size. The kernel size must be an odd number. The larger the kernel size, the more the image is blurred.
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)  # (7, 7) is the kernel size
cv.imshow('Blur', blur)

# Edge Cascade. Cannny is an edge detection algorithm. It takes in an image and two threshold values.
canny = cv.Canny(blur, 125, 175)  # 125 is the lower threshold, 175 is the upper threshold
cv.imshow('Canny Edges', canny)

# Dilating the image. This makes the edges thicker.
dilated = cv.dilate(canny, (7, 7), iterations=3)  # (7, 7) is the kernel size, 3 is the number of iterations
cv.imshow('Dilated', dilated)
# takes in cannny image and kernel size and number of iterations

# Eroding. This makes the edges thinner.
eroded = cv.erode(dilated, (7, 7), iterations=3)  # (7, 7) is the kernel size, 3 is the number of iterations
cv.imshow('Eroded', eroded)
# looks very similar to canny edges because the dilation. Essentially, undoes the dilation.

# Resize
resized = cv.resize(img, (200, 500), interpolation=cv.INTER_CUBIC)  # specify new dimensions of the image. INTER_CUBIC is slow but good for enlarging.
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]  # specify the region of the image to be cropped
cv.imshow('Cropped', cropped)

cv.waitKey(0)
