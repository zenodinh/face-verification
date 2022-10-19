import datetime
import os
import numpy as np
import cv2
import face_recognition

dataFolder = "../Resources/RegisteredImages"
images = []
className = []
myList = os.listdir(dataFolder)


def loadImages():
    for cl in myList:
        curImg = cv2.imread(f'{dataFolder}/{cl}')
        images.append(curImg)
        className.append(os.path.splitext(cl)[0])
    print("List of user: ", className)


def login():
    loadImages()
    cap = cv2.VideoCapture(0)
    now = datetime.datetime.now()
    encodingKnownList = findEncodings(images)
    cv2.startWindowThread()

    while datetime.datetime.now().second - now.second < 30:
        success, frame = cap.read()
        show = frame.copy()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = face_recognition.face_locations(frame)
        if not faces:
            continue
        encodes = face_recognition.face_encodings(frame, faces)[0]

        if faces and len(faces) > 3:
            cv2.rectangle(show, (faces[3], faces[0]), (faces[1], faces[2]), (255, 0, 0), 3)
        cv2.imshow("Face", show)
        for encode, face in zip(encodes, faces):
            matches = face_recognition.compare_faces(encodingKnownList, encode)
            faceDis = face_recognition.face_distance(encodingKnownList, encode)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = className[matchIndex]
                print("Welcome back, ", name)
                cap.release()
                cv2.destroyAllWindows()
                return True
    cap.release()
    cv2.destroyAllWindows()
    return False


def findEncodings(knownImages):
    encodings = []
    for img in knownImages:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodings.append(encode)
    return encodings
