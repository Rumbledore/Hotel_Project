from hotel_Devops.hotel_func import *
from hotel_Devops.functions import menu

spaces = "-=========~~~~~~=========-".center(100)


print("\n" + spaces)
print("--Welcome to NET4U Hotel--".center(100))
print(spaces + "\n")

menu()

while True:
    boolean = input("Would you like to go back to the Main Menu or leave?\n1 = Main Menu\n2 = Leave")

    if boolean == "2":
        break
    elif boolean == "1":
        menu()
    else:
        print("Invalid input, try again.")


