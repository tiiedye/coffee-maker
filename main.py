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
