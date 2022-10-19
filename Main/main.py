from Main.login import login
from Main.register import register


def main():
    print("Welcome to face login")
    while True:
        print("1. Dang nhap\n")
        print("2. Dang xuat\n")
        actionType = input("Chon chuc nang (1, 2): ")
        result = False
        if actionType == "1":
            result = login()
            break
        elif actionType == "2":
            result = register()
            break
        else:
            print("Chuc nang nam ngoai pham vi phuc vu, vui long chon lai")
    if result:
        print("Thanh cong")
        return
    print("That bai")


if __name__ == "__main__":
    main()
