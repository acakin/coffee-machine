MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
espresso, latte, cappuccino, ingredients = "espresso", "latte", "cappuccino", "ingredients"
water, milk, coffee, cost = "water", "milk", "coffee", "cost"
quarter, dimes, nickels, pennies = 0.25, 0.10, 0.05, 0.01
safe_box = 0
MENU[espresso][ingredients][milk] = 0
machine = True
while machine:
    order = input("What would you like? Please type 'e' for espresso, 'l' for latte, 'c' for cappuccino: ").lower()

    if order == "e":
        order = espresso

    elif order == "l":
        order = latte

    elif order == "c":
        order = cappuccino

    elif order == "report":
        print(f"Water: {resources[water]}ml")
        print(f"Milk: {resources[milk]}ml")
        print(f"Coffee: {resources[coffee]}g")
        print(f"Money: ${safe_box}")
        continue

    elif order == "off":
        break

    print(f"Please insert coins. It cost ${MENU[order][cost]}.")
    num_quarters = int(input("How many quarters?: "))
    num_dimes = int(input("How many dimes?: "))
    num_nickels = int(input("How many nickels?: "))
    num_pennies = int(input("How many pennies?: "))

    total = quarter * num_quarters + dimes * num_dimes + nickels * num_nickels + pennies * num_pennies
    change = round(total - MENU[order][cost], 2)
    if change < 0:
        print("Sorry that's not enough money. Money refunded.")
    else:
        safe_box += (MENU[order][cost])
        print(f"Here is ${change} in change.")
        print(f"Here is {order} ☕. Enjoy!")
        resources[water] -= MENU[order][ingredients][water]
        resources[milk] -= MENU[order][ingredients][milk]
        resources[coffee] -= MENU[order][ingredients][coffee]
        if resources[water] < MENU[order][ingredients][water]:
            print("Sorry, there is not enough water.")
        elif resources[milk] < MENU[order][ingredients][milk]:
            print("Sorry, there is not enough milk.")
        elif resources[coffee] < MENU[order][ingredients][coffee]:
            print("Sorry, there is not enough coffee.")