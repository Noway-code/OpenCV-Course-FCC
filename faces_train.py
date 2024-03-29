import os
import cv2 as cv
import numpy as np

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
DIR = r'/home/noway/PycharmProjects/openCV/OpenCV Course FCC/Faces/train'

haar_cascade = cv.CascadeClassifier('haar_face.xml')

features = []
labels = []


def create_train():
    for person in people:
        # os.path.join() is used to join the path of the directory and the name of the person.
        path = os.path.join(DIR, person)
        label = people.index(person)

        # iterate through the images in the directory.
        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            # read the image, grayscale it, and detect the face via haar cascade.
            img_array = cv.imread(img_path)
            if img_array is None:
                continue

            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y + h, x:x + w]
                features.append(faces_roi)
                labels.append(label)


create_train()
print('Training done ---------------')

# convert the features and labels to numpy arrays.
features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# train the recognizer
face_recognizer.train(features, labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)

# save the trained model
