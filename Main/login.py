import datetime
import os
import numpy as np
import cv2
import face_recognition

dataFolder = "../Resources/RegisteredImages"
images = []
className = []
myList = os.listdir(dataFolder)


def alignWindow(windowName):
    cv2.namedWindow(windowName)
    cv2.moveWindow(windowName, 300, 100)
    cv2.startWindowThread()
def showTemp(windowName, cap, now):
    while datetime.datetime.now().second - now.second < 4:
        success, frame = cap.read()
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = face_recognition.face_locations(img)
        if len(faces) > 0:
            cv2.rectangle(frame, (faces[0][3], faces[0][0]), (faces[0][1], faces[0][2]), (0, 0, 255), 2)
        cv2.imshow(windowName, frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break


def loadImages():
    for cl in myList:
        curImg = cv2.imread(f'{dataFolder}/{cl}')
        images.append(curImg)
        className.append(os.path.splitext(cl)[0])


def login():
    loadImages()
    windowName = "Login"
    alignWindow(windowName)
    cap = cv2.VideoCapture(0)
    now = datetime.datetime.now()
    encodingKnownList = findEncodings(images)

    showTemp(windowName, cap, now)

    while datetime.datetime.now().second - now.second < 7:
        success, frame = cap.read()
        origin = frame.copy()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faceLocs = face_recognition.face_locations(frame)
        faceEncodes = face_recognition.face_encodings(frame, faceLocs)
        for encode, face in zip(faceEncodes, faceLocs):
            matches = face_recognition.compare_faces(encodingKnownList, encode)
            faceDis = face_recognition.face_distance(encodingKnownList, encode)
            matchIndex = np.argmin(faceDis)
            cv2.rectangle(origin, (face[3], face[0]), (face[1], face[2]), (0, 0, 255), 2)
            if matches[matchIndex]:
                name = className[matchIndex]
                print("Welcome back, ", name)
                cv2.destroyAllWindows()
                cv2.waitKey(1)
                cap.release()
                return name
        cv2.imshow(windowName, origin)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    cv2.waitKey(1)
    cap.release()
    return ""


def findEncodings(knownImages):
    encodings = []
    for img in knownImages:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodings.append(encode)
    return encodings
