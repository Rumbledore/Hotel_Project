from hotel_Devops.hotel_func import *

def menu_text():
    print("Main Menu:".center(100))
    print("1.search for available rooms".center(101))
    print("2.search for specific date".center(99))
    print("3.invitation".center(85))
    print("4.cancel order".center(87))
    print("5.add days/rooms".center(89))
    print("6.search for invitation".center(97))

def menu():
    menu_text()
    choice = int(input())

    if choice == 1:
        hotels.find_free_rooms()
    elif choice == 2:
        hotels.searchdate()
    elif choice == 3:
        # func3 call
        print()
    elif choice == 4:
        print()
        # func4 call
    elif choice == 5:
        print()
        # func5 call
    elif choice == 6:
        print()
        # func6 call






