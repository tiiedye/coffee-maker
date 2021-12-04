# Coffee Machine Project
# TODO 1. Create menu options function
# TODO 2. create functions to print report, order, refill resources, check payment, and turn off
# TODO 3. create loop until user chooses off option

from coffee_menu import MENU, resources


def print_menu():
    print("Welcome to the Coffee Maker, choose an option: ")
    print("\tOrder Coffee [1]")
    print("\tCheck Resources [2]")
    print("\tTurn Off [3]")
    option = input("\n Enter 1, 2, or 3: ")

    while option != "1" or option != "2" or option != "3":
        option = input("Invalid option, Enter 1, 2 or 3: ")

    return option


def check_resources():
    print("Resource Amounts:")
    print(f"\tWater: {resources['water']}")
    print(f"\tMilk: {resources['milk']}")
    print(f"\tCoffee: {resources['coffee']}")

    option = input("Would you like to refill resources? [Y/N]: ").lower()

    if option == "y":
        add_resources()
    else:
        print("Returning to main menu")


def add_resources():
    return_to_menu = False

    while not return_to_menu:
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")

        print("What would you like to refill?")
        print("\tWater [1]")
        print("\tMilk [2]")
        print("\tCoffee [3]")
        print("\tReturn to Menu [4]")

        option = input("Enter 1, 2, 3, or 4: ")

        while option != "1" or option != "2" or option != "3" or option != "4":
            option = input("Invalid option, Enter 1, 2, 3, or 4: ")

        if option == "1":
            if resources['water'] == 300:
                print("Already full")
            else:
                resources['water'] = 300
                print("Water filled")
        elif option == "2":
            if resources['milk'] == 200:
                print("Already full")
            else:
                resources['milk'] = 200
                print("Milk filled")
        elif option == "3":
            if resources['coffee'] == 100:
                print("Already full")
            else:
                resources['coffee'] = 100
                print("Coffee filled")
        else:
            print("Returning to Menu")

