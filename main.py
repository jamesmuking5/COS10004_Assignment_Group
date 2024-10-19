import os
from variable import Variable
from ccc import CCC

# Init Central Control Unit (CCC)
ccc = CCC()


def printBanner():
    print("Welcome to the Central Control Unit (CCC)!")
    print("********** Main Menu ***********")
    print("1. Toggle Manual Switch")
    print("2. Run Multiplexer (Mux)")
    print("3. Set System Variables")
    print("4. End Program")


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


def mux_menu(manual=True):
    if manual:
        while True:
            clear_screen()
            try:
                print("********* Multiplexer (Mux) Menu *********")
                print(" Manual Switch included")
                s1 = int(input("Enter S1 (0 or 1): "))
                s2 = int(input("Enter S2 (0 or 1): "))
                s3 = int(input("Enter S3 (0 or 1): "))
                print(f"Output: {ccc.runMuxManual(s1, s2, s3)}")
            except IndexError as e:
                print("Invalid Input: ", e)
            except ValueError as e:
                print("Invalid Input: ", e)
            continue_choice = input("Continue? (y/n): ")
            if continue_choice.lower() != "y":
                break  # Exit the loop
    else:
        while True:
            clear_screen()
            try:
                print("********* Multiplexer (Mux) Menu *********")
                print(" Manual Switch not included")
                s1 = int(input("Enter S1 (0 or 1): "))
                s2 = int(input("Enter S2 (0 or 1): "))
                s3 = int(input("Enter S3 (0 or 1): "))
                print(f"Output: {ccc.runMux(s1, s2, s3)}")
            except IndexError as e:
                print("Invalid Input: ", e)
            except ValueError as e:
                print("Invalid Input: ", e)
            continue_choice = input("Continue? (Y/N): ")
            if continue_choice.lower() != "y":
                break


# Main loop
while True:
    clear_screen()
    printBanner()
    try:
        choice = int(input("Enter Choice: "))
        if choice == 1:
            while True:
                clear_screen()
                ccc.printManualSwitches()
                switch_index = int(input("Enter System Index to Toggle (0 to exit): "))
                if switch_index < 0 or switch_index > 5:
                    print("Invalid Index!")
                    input()
                    continue
                if switch_index == 0:
                    break
                ccc.setManualSwitch(switch_index)
        elif choice == 2:
            while True:
                clear_screen()
                print("********* Multiplexer (Mux) Menu *********")
                print("Include Manual Switch in the Systems Input?")
                print("1. Yes")
                print("2. No")
                print("3. Exit to Main Menu")
                choice = int(input("Enter Choice: "))
                if choice == 1:
                    mux_menu(True)
                elif choice == 2:
                    mux_menu(False)
                elif choice == 3:
                    break
                else:
                    print("Invalid Choice!")
                    input()
        elif choice == 3:
            while True:
                clear_screen()
                print("********* System Variables Menu *********")
                print("*** Manual Switch cannot be set here ***")
                print("1. View current System Variables")
                print("2. Set all Variables to True")
                print("3. Set all Variables to False")
                print("4. Randomise all Variables")
                print("5. Exit to Main Menu")
                choice = int(input("Enter Choice: "))
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
                    print("Invalid Choice!")
        elif choice == 4:
            break  # Exit the program
        else:
            print("Invalid Choice!")
    except Exception as e:
        print("Error:", e)
