import datetime

from hotel_Devops import functions
import hotel_Devops

# this will change for different machines


file_path = "D:/Programing/HotelProject-master/Files/room"
num_of_rooms = 4


class hotels:

    # option-1
    def get_available_dates_and_rooms():
        for i in range(num_of_rooms):
            with open(file_path + str(i + 1) + ".txt", "r") as f:
                if i == 0 or i == 1:
                    print("\nfor room" + str(i + 1) + " with 2 adults:\n" + str(f.read()))
                elif i == 2 or i == 3:
                    print("\nfor room" + str(i + 1) + " with 3 adults:\n" + str(f.read()))
                f.close()

    # option-2
    # TODO: add for how long(days) as bonus
    def search_available_room_by_date():
        days = 7  # defined number for now
        date_array = input("Enter date: (year-day-month)").split("-")
        if len(date_array) == 3:
            date = str(datetime.date(int(date_array[0]), int(date_array[2]), int(date_array[1])))

        boolean = 0
        while boolean == 0:
            adults = int(input("Enter number of adults: (2/3)"))
            room_empty_text = "*You can invite " + str(days) + " days from " + str(date) + ", for " + \
                              str(adults) + " adults in room"
            room_occupied_text = " is occupied in these dates.*"

            if adults == 2:
                for i in range(int(num_of_rooms/2)):
                    with open(file_path + str((i + 1)) + ".txt", "r") as f:
                        room1_list = list(f.read().splitlines())
                        if date in room1_list:
                            print("\n" + room_empty_text + str((i + 1)) + "*\n")
                        else:
                            print("\n*room" + str((i + 1)) + room_occupied_text)
                        f.close()
                    boolean = 1
            elif adults == 3:
                for i in range(2, num_of_rooms):
                    with open(file_path + str((i + 1)) + ".txt", "r") as f:
                        room1_list = list(f.read().splitlines())
                        if date in room1_list:
                            print("\n" + room_empty_text + str((i + 1)) + "*\n")
                        else:
                            print("\n*room" + str((i + 1)) + room_occupied_text + "\n")
                        f.close()
                    boolean = 1
            else:
                print("Invalid input!, try again.")

    # option-3
    def invitation():
        room1_price = 1000
        room2_price = 1200
        room3_price = 800
        room4_price = 1500

        answer = input("Witch room would you like to get?")
        if answer == "1":
            order = int(input("Are you sure you to order room" + answer + " for " + str(room1_price) +
                              "$ per day?\n1 = Yes\n2 = No"))
            order_logic(answer, order)
        elif answer == "2":
            order = int(input("Are you sure you to order room" + answer + " for " + str(room2_price) +
                              "$ per day?\n1 = Yes\n2 = No"))
            order_logic(answer, order)
        elif answer == "3":
            order = int(input("Are you sure you to order room" + answer + " for " + str(room3_price) +
                              "$ per day?\n1 = Yes\n2 = No"))
            order_logic(answer, order)
        elif answer == "4":
            order = int(input("Are you sure you to order room" + answer + " for " + str(room4_price) +
                              "$ per day?\n1 = Yes\n2 = No"))
            order_logic(answer, order)
        else:
            print("No such room, room" + answer)
            functions.main_menu()


def order_logic(answer, order):
    if order == 1:
        print("\nCongrats you successfully ordered room" + answer + "\n")
    elif order == 2:
        print("\nToo bad.\n")
        functions.main_menu()
    else:
        print("\nInvalid input.\n")
        functions.main_menu()

# print('''
#  welcome to Net4U Hotel!
#
#  Menu:
#
#  1) חיפוש תאריכים פנויים לפי מס מבוגרים ותאריך
#  2) מכניס את כמות האנשים ותאריך ומקבל תשובה מה פנוי
#  3) ביצוע הזמנה,לעשות קנייה חישוב עלות הכנסת פרטים אישיים
#  4) בוטול הזמנה קיימת ומחייב בכנס של 10%
#  5) הוספת חדרים או ימים להזמנה קיימת
#  6) חיפוש הזמנה קיימת
#  ''')
#
