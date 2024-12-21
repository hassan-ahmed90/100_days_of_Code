

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeemaker=CoffeeMaker()
menuu=Menu()
moneymachine=MoneyMachine()

should_con=True
while should_con:
    option=menuu.get_items()
    user_choice=input(f"What coffe would you like to take {option}")
    if user_choice=="off":
        should_con=False
    elif user_choice=="report":
        moneymachine.report()
        coffeemaker.report()
    else:
        drink=menuu.find_drink(user_choice)
        if drink:
            coffeemaker.is_resource_sufficient(drink)
            if moneymachine.make_payment(drink.cost):
                coffeemaker.make_coffee(drink)






