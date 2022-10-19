import os

import cv2

from Main.login import login, dataFolder
from Main.register import register


def showYourImage():
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        cv2.imshow("Your face", frame)
        if cv2.waitKey(1) == ord('q'):
            return


def main():
    print("Welcome to face login")
    while True:
        print("1. Sign in\n")
        print("2. Sign up\n")
        print("3. Exit\n")
        actionType = input("Choose function (1, 2, 3): ")
        if actionType == "1":
            if login():
                print("Here is your face. Press q for exit")
                showYourImage()
            else:
                print("You haven't login yet. Please register a new account")
        elif actionType == "2":
            name = register()
            if name != "":
                print("Welcome to Quan Dinh faceID login")
                print("Here is what we recognize you")
                curImg = cv2.imread(f'{dataFolder}/{name}')
                cv2.imshow(name, curImg)
                cv2.destroyAllWindows()
        elif actionType == "3":
            print("Goodbye")
            break
        else:
            print("Function is outside the menu. Please try again")


if __name__ == "__main__":
    main()
