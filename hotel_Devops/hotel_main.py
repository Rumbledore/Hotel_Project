from hotel_Devops.functions import main_menu

spaces = "-=========~~~~~~=========-".center(100)


print("\n" + spaces)
print("--Welcome to NET4U Hotel--".center(100))
print(spaces + "\n")

main_menu()

while True:
    answer = input("Are you sure you want to leave, or go back to the main menu?\n1 = Main Menu\n2 = Leave")

    if answer == "2":
        break
    elif answer == "1":
        main_menu()
    else:
        print("Invalid input, try again.")


