from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def is_machine_on():
    menu = Menu()
    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker()
    while True:
        order_name = input(f"What would you like? ({menu.get_items()}) ")
        if order_name == "off":
            return

        elif order_name == "report":
            coffee_maker.report()
            money_machine.report()
            continue

        else:
            drink = menu.find_drink(order_name)
            if drink is None:
                continue
            elif coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)

is_machine_on()