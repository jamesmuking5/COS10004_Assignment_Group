import os
from variable import Variable
from ccc import CCC

# Init Central Control Unit (CCC)
ccc = CCC()


# Init tests
# try:
#     ccc.randomiseVariables()
# except Exception as e:
#     print("Error:", e)


def printBanner():
    print("Welcome to the Central Control Unit (CCC)!")
    print("********** Main Menu ***********")
    print("1. Toggle manual switch")
    print("2. Run Multiplexer (Mux)")
    print("3. Set system variables")
    print("4. Exit")


def printSystems():
    print("Central Control Unit Systems:")
    for i in range(len(ccc.all_systems)):
        print(f"{i + 1}. {ccc.all_systems[i].name}")


def clear_screen():
    # Clear the screen based on the operating system
    if os.name == "nt":  # For Windows
        os.system("cls")
    else:  # For Unix-like systems (Linux, macOS)
        os.system("clear")


# Main loop
while True:
    clear_screen()
    printBanner()
    try:
        choice = int(input("Enter choice: "))
        if choice == 1:
            clear_screen()
            printSystems()
            print("6. Exit")
            index = int(input("Enter system index to toggle: "))
            if index == 6:
                continue
            ccc.setManualSwitch(index)
            clear_screen()
            ccc.printManualSwitches()
            input()
        elif choice == 2:
            while True:
                clear_screen()
                try:
                    print("********* Multiplexer (Mux) Menu *********")
                    s1 = int(input("Enter s1: "))
                    s2 = int(input("Enter s2: "))
                    s3 = int(input("Enter s3: "))
                    print(f"Output: {ccc.runMux(s1, s2, s3)}")
                except IndexError as e:
                    print("Invalid Input: ", e)
                continue_choice = input("Continue? (y/n): ")
                if continue_choice.lower() != "y":
                    break  # Exit the loop
        elif choice == 3:
            while True:
                clear_screen()
                print("********* System Variables Menu *********")
                print("1. View current system variables")
                print("2. Set all variables to True")
                print("3. Set all variables to False")
                print("4. Randomise all variables")
                print("5. Exit to main menu")
                choice = int(input("Enter choice: "))
                if choice == 1:
                    clear_screen()
                    ccc.printVariables()
                    print("\nPress Enter to continue...")
                    input()
                elif choice == 2:
                    ccc.setVariablesTrue()
                elif choice == 3:
                    ccc.setVariablesFalse()
                elif choice == 4:
                    ccc.randomiseVariables()
                elif choice == 5:
                    break  # Exit the loop
                else:
                    print("Invalid choice!")
        elif choice == 4:
            break  # Exit the program
        else:
            print("Invalid choice!")
    except Exception as e:
        print("Error:", e)
