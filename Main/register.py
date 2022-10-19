import cv2

from Main.login import *


def isUsernameExists(username):
    for existsName in className:
        if username == existsName:
            return True
    return False


def register():
    global bestImage
    loadImages()
    encodingKnownList = findEncodings(images)
    print("Warning: username must be unique and can't be change")
    while True:
        name = input("Input username: ")
        if isUsernameExists(name):
            print("This username is already assigned. Please try again\n")
        else:
            break

    cap = cv2.VideoCapture(0)
    now = datetime.datetime.now()
    cv2.startWindowThread()

    while datetime.datetime.now().second - now.second < 20:
        success, frame = cap.read()
        originImg = frame.copy()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = face_recognition.face_locations(frame)
        if not faces:
            continue
        encodes = face_recognition.face_encodings(frame, faces)[0]

        for encode, face in zip(encodes, faces):
            matches = face_recognition.compare_faces(encodingKnownList, encode)
            faceDis = face_recognition.face_distance(encodingKnownList, encode)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                print("You have been registered before, please login instead\n")
                cap.release()
                cv2.destroyAllWindows()
                return ""
            else:
                caseCade = cv2.CascadeClassifier(cv2.data.haarcascades + f'{dataFolder}../Models/haarcascade_frontalface_default.xml')
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                face = caseCade.detectMultiScale(gray)
                if 0 < len(face) < 2:
                    print("Register successfully\n")
                    cv2.imwrite(os.path.join(dataFolder, name.lower() + ".jpg"), frame)
                    cap.release()
                    cv2.destroyAllWindows()
                    return name
    return ""
