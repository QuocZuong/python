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
    "value": 0
}


def orderCoffee(name_of_drink):
    if name_of_drink != 'cappuccino' and name_of_drink != 'latte' and name_of_drink != 'espresso':
        print("Please try another drink!")
        return
    elif resources["water"] < MENU[name_of_drink]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        return
    elif resources["milk"] < MENU[name_of_drink]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
        return
    elif resources["coffee"] < MENU[name_of_drink]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        return
    print("Please insert coins.")

    quarters = float(input("How many quarters?:"))
    dimes = float(input("How many dimes?:"))
    nickles = float(input("How many nickles?:"))
    pennies = float(input("How many pennies?:"))
    totalMoney = float((quarters * 0.25) + (dimes * 0.1) +
                       (nickles * 0.05) + (pennies * 0.01))
    print(f"Here is {totalMoney} in change.")

    if totalMoney < float(MENU[name_of_drink]["cost"]):
        print("You don't have enough money")

    else:
        print("Here is your latte!")
        resources["water"] -= MENU[name_of_drink]["ingredients"]["water"]
        resources["milk"] -= MENU[name_of_drink]["ingredients"]["milk"]
        resources["coffee"] -= MENU[name_of_drink]["ingredients"]["coffee"]
        resources["value"] += totalMoney


def report(resources):
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {resources['value']}")


should_continue = True
value = 0

while should_continue:
    order = input("What would you like? ")
    if order == 'off':
        break
    elif order == "report":
        report(resources)
    else:
        orderCoffee(order)
