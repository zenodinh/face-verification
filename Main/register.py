import cv2

from Main.login import *


def isUsernameExists(username):
    for existsName in className:
        if username == existsName:
            return True
    return False


def register():
    windowName = "Register"
    alignWindow(windowName)
    loadImages()
    encodingKnownList = findEncodings(images)

    cap = cv2.VideoCapture(0)
    now = datetime.datetime.now()

    showTemp(windowName, cap, now)

    while datetime.datetime.now().second - now.second < 7:
        success, frame = cap.read()
        cv2.imshow(windowName, frame)
        origin = frame.copy()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = face_recognition.face_locations(frame)
        encodes = face_recognition.face_encodings(frame, faces)

        for encode, face in zip(encodes, faces):
            matches = face_recognition.compare_faces(encodingKnownList, encode)
            faceDis = face_recognition.face_distance(encodingKnownList, encode)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                print("You have been registered before, please login instead\n")
                cv2.destroyAllWindows()
                cv2.waitKey(1)
                cap.release()
                return ""
            else:
                print("Register successfully\n")
                print("Warning: username must be unique and can't be change")
                cv2.destroyAllWindows()
                cv2.waitKey(1)
                cap.release()
                while True:
                    name = input("Input username: ")
                    if isUsernameExists(name.lower()):
                        print("This username is already assigned. Please try again\n")
                    else:
                        break
                cv2.imwrite(os.path.join(dataFolder, name.lower() + ".jpg"), origin)
                return name
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    cap.release()
    return ""
