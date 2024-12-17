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
money=0
should_con=True

def check_resources(order_ingredients):
    for items in order_ingredients:
        if resources[items]<order_ingredients[items]:
            print("Sorry there is not enough resource you have")
            return False
    return True

def take_coins():
    total=0
    print("Enter the money?\n")
    total+=int(input("Enter the quaters?\n"))*0.25
    total += int(input("Enter the nickles?\n")) * 0.05
    total += int(input("Enter the pennies?\n")) * 0.01
    total += int(input("Enter the dimes?\n")) * 0.10
    return  total

def check_transiction(user_money,coffe_money):
    if user_money>=coffe_money:
        global  money
        money+=coffe_money
        change=round(user_money-coffe_money,2)
        if change>0:
            print(f"Here is your change {change}$")
        return True
    else:
        print("You don't have enough money for this coffe")
        return False

def make_coffe(drink,order_ing):
    for item in order_ing:
        resources[item]-=order_ing[item]

    print(f"Here is your drink {drink}")


while should_con:
    user_choice=input("What would you like? (espresso/latte/cappuccino):?\n")
    if user_choice=="off":
        should_con=False
    elif user_choice=="report":
        print(f"Water = {resources['water']}ml")
        print(f"Milk = {resources['water']}ml")
        print(f"Coffee = {resources['coffee']}")
        print(f"Money {money}$")
    elif user_choice in MENU:
        drink= MENU[user_choice]
        actual_cost=drink['cost']
        if check_resources(drink['ingredients']):
            user_money=take_coins()
            if check_transiction(user_money,actual_cost):
                make_coffe(user_choice,drink['ingredients'])

    else:
        print("Enter Valid Choice")



