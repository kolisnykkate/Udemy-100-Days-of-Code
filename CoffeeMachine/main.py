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

COINS = {"quarters": 0.25,
         "dimes": 0.1,
         "nickels": 0.05,
         "pennies": 0.01,
         }

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def insert_coins():
    print("Please insert coins.")
    total = 0
    for key, value in COINS.items():
        inserted_coin = int(input(f"How many {key}? "))
        total += inserted_coin * value
    return total


def is_resources_sufficient(coffee, resources):
    for ingredient, amount in coffee["ingredients"].items():
        if resources[ingredient] < amount:
            print(f"Sorry, there's not enough {ingredient}.")
            return False
    return True


def reduce_resources(coffee, resources):
    for ingredient, amount in coffee["ingredients"].items():
        resources[ingredient] -= amount
    return resources


def is_enough_money(coffee, payment):
    return (payment >= coffee["cost"],
            payment - coffee["cost"])


def machine_on():
    money = 0

    while True:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()

        if order == "off":
            return

        elif order == "report":
            for ingredient, amount in resources.items():
                print(f"{ingredient.title()}: {amount} ml(g)")
            print(f"Money: ${money}")
        else:
            try:
                coffee = MENU[order]
            except KeyError:
                print(f"Sorry, {order} is not a valid coffee.")
                continue

            if is_resources_sufficient(coffee, resources):
                total = insert_coins()
                is_enough, change = is_enough_money(coffee, total)
                if is_enough:
                    money += coffee["cost"]
                    reduce_resources(coffee, resources)
                    print(f"Here is ${round(change, 2)} in change.\n"
                          f"Here is your {order} ☕️. Enjoy!")
                else:
                    print("Sorry, that's not enough money. Money refunded.")


machine_on()




