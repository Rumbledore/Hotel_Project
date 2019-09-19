import datetime

# this will change for different machines
file_path = "D:/Programing/HotelProject-master/Files/room"


class hotels():

    # option-1
    def find_free_rooms():
        with open(file_path + "1.txt", "r") as f:
            print("\nfor room1 with 2 adults:\n" + str(f.read()))
            f.close()
        with open(file_path + "2.txt", "r") as f:
            print("for room2 with 2 adults:\n" + str(f.read()))
            f.close()
        with open(file_path + "3.txt", "r") as f:
            print("for room3 with 3 adults:\n" + str(f.read()))
            f.close()
        with open(file_path + "4.txt", "r") as f:
            print("for room4 with 3 adults:\n" + str(f.read()))
            f.close()

    # option-2
    # add for how long(days) as bonus
    def searchdate():
        days = 7  # set number for now
        date_array = input("Enter date: (year-day-month)").split("-")
        if len(date_array) == 3:
            date = str(datetime.date(int(date_array[0]), int(date_array[2]), int(date_array[1])))

        boolean = 0
        while boolean == 0:
            adults = int(input("Enter number of adults: (2/3)"))
            room_empty_text = "*You can invite " + str(days) + " days from " + str(date) + ", for " + \
                              str(adults) + " adults in room"
            room_occupied_text = "is occupied in these dates.*"

            if adults == 2:
                with open(file_path + "1.txt", "r") as f:
                    room1_list = list(f.read().splitlines())
                    if date in room1_list:
                        print("\n" + room_empty_text + "1*\n")
                    else:
                        print("\n*room1 " + room_occupied_text)
                    f.close()

                with open(file_path + "2.txt", "r") as f:
                    room2_list = list(f.read().splitlines())
                    if date in room2_list:
                        print(room_empty_text + "2*\n")
                    else:
                        print("\n*room2 " + room_occupied_text + "\n")
                    f.close()

                boolean = 1
            elif adults == 3:
                with open(file_path + "3.txt", "r") as f:
                    room3_list = list(f.read().splitlines())
                    if date in room3_list:
                        print("\n" + room_empty_text + "3*\n")
                    else:
                        print("\n*room3 " + room_occupied_text)
                    f.close()

                with open(file_path + "4.txt", "r") as f:
                    room4_list = list(f.read().splitlines())
                    if date in room4_list:
                        print(room_empty_text + "4*\n")
                    else:
                        print("\n*room4 " + room_occupied_text + "\n")
                    f.close()

                boolean = 1
            else:
                print("Invalid input!, try again.")










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
