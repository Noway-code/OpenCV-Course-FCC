import cv2 as cv

img = cv.imread('Photos/group 1.jpg')
cv.imshow('lady', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

# scale factor: how much the image size is reduced at each image scale.
# minNeighbors: how many neighbors each candidate rectangle should have to retain it.
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
print(f'Number of faces found = {len(faces_rect)}')

# using faces_rect to draw rectangles around the faces
# haar cascade is extremely sensitive to the scale of the image.
for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow('Detected faces', img)
# haar cascades are good for simple face detection, but not for complex face detection.
# for complex face detection, use deep learning.


cv.waitKey(0)
