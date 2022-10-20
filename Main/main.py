import cv2

from Main.login import login, dataFolder, alignWindow
from Main.register import register


def showYourImage(name):
    windowName = "Your face"
    curImg = cv2.imread(f'{dataFolder}/{name}.jpg')
    alignWindow(windowName)
    print("Here is your face. Press any key to exit")
    cv2.imshow(windowName, curImg)
    if cv2.waitKey(0):
        cv2.destroyAllWindows()
        cv2.waitKey(1)


def main():
    print("Welcome to face login")
    while True:
        print("1. Sign in\n")
        print("2. Sign up\n")
        print("3. Exit\n")
        actionType = input("Choose function (1, 2, 3): ")
        if actionType == "1":
            name = login()
            if name != "":
                showYourImage(name)
            else:
                print("You haven't login yet. Please register a new account")
        elif actionType == "2":
            name = register()
            if name != "":
                print("Welcome to Quan Dinh faceID login")
                print("Here is what we recognize you")
                showYourImage(name)
        elif actionType == "3":
            print("Goodbye")
            break
        else:
            print("Function is outside the menu. Please try again")


if __name__ == "__main__":
    main()
