# Coffee Machine Project
# TODO 1. Create menu options function
# TODO 2. create functions to print report, order, refill resources, check payment, and make drink
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


def check_payment(payment, order):
    if payment >= MENU[order]['cost']:
        print("Thank you!")
        change = payment - MENU[order]['cost']
        if change > 0:
            print(f"Printing change: ${change}")
        return True
    else:
        print(f"Not enough, refunding ${payment}")
        return False


def make_drink(order):
    print(f"Making {order}!")

    if order == "espresso":
        water_level = resources['water'] - MENU[order]['ingredients']['water']
        if water_level >= 0:
            resources['water'] = water_level
            coffee_level = resources['coffee'] - MENU[order]['ingredients']['coffee']
            if coffee_level > 0:
                resources['coffee'] = coffee_level
                print("bZZzzRRRttZZzz")
                print("Drink Made!")
            else:
                print("Not enough coffee, please check levels")
        else:
            print("Not enough water, please check levels")
    else:
        water_level = resources['water'] - MENU[order]['ingredients']['water']
        if water_level >= 0:
            resources['water'] = water_level
            milk_level = resources['milk'] - MENU[order]['ingredients']['milk']
            if milk_level > 0:
                resources['milk'] = milk_level
                coffee_level = resources['coffee'] - MENU[order]['ingredients']['coffee']
                if coffee_level > 0:
                    resources['coffee'] = coffee_level
                    print("bZZzzRRRttZZzz")
                    print("Drink Made!")
                else:
                    print("Not enough coffee, please check levels")
            else:
                print("Not enough milk, please check levels")
        else:
            print("Not enough water, please check levels")

