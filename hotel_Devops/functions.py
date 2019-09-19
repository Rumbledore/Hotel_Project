from hotel_Devops.hotel_func import *


def menu_text():
    print("Main Menu:".center(100))
    print("1.Search for available rooms".center(101))
    print("2.Search for specific date".center(99))
    print("3.Invitation".center(85))
    print("4.Cancel order".center(87))
    print("5.Extend your vacation/more rooms".center(107))
    print("6.Check for ongoing invitation".center(103))
    print("7.Leave".center(82))


def main_menu():
    menu_text()
    choice = int(input())

    if choice == 1:
        hotels.get_available_dates_and_rooms()
    elif choice == 2:
        hotels.search_available_room_by_date()
    elif choice == 3:
        hotels.invitation()
    elif choice == 4:
        print()
        # func4 call
    elif choice == 5:
        print()
        # func5 call
    elif choice == 6:
        print()
        # func6 call
    elif choice == 7:
        return






