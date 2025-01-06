MENU = {
    "espresso": {
        "ingredients": {
            "milk": 0,
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

Turn_off = True
money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}


def check_resources(user_input):
    for item in resources:
        if resources[item] < user_input[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True


def process_coin(quarters_q, dimes_q, nickles_q, pennies_q):
    """returninh total money"""
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01
    total = quarters_q * quarters + dimes_q * dimes + nickles_q * nickles + pennies_q * pennies
    return total


def is_transection(total):
    price = MENU[user_input]['cost']
    if total == price:
        print(f"This is your cofee")
        return True
    elif total > price:
        print(f"Balance ${round(total - price, 2)})")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def report_gen():
    global money
    print(f"The summary report is as following...:")
    print(f"Water: {resources['water']}ml")
    if user_input != "espresso":
        print(f"milk: {resources['milk']}ml")
    print(f"coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def update_resources(cofee_name):
    global money
    for item in resources:
        resources[item] = resources[item] - MENU[cofee_name]['ingredients'][item]
    money = money + MENU[cofee_name]['cost']
    print(f"Here is your {cofee_name} ☕️. Enjoy!")


def bill():
    print(f"The Bill is as following...:")
    print(f"Water: {MENU[user_input]['ingredients']['water']}")
    if user_input != "espresso":
        print(f"milk: {MENU[user_input]['ingredients']['milk']}")
    print(f"coffee: {MENU[user_input]['ingredients']['coffee']}")
    print(f"price: ${MENU[user_input]['cost']}")


while Turn_off:
    user_input = input('What would you like? (espresso/latte/cappuccino):')
    if user_input.lower() == "off":
        print("Turning off machine")
        Turn_off = False
    elif user_input.lower() == "report":
        report_gen()
    else:
        drink = MENU[user_input]
        if check_resources(drink['ingredients']):
            print("please insert coins.")
            quarters_q = int(input("How many quarters? ..:"))
            dimes_q = int(input("How many dimes? ..:"))
            nickles_q = int(input("How many nickles? ..:"))
            pennies_q = int(input("How many pennies?...:"))
            total = process_coin(quarters_q, dimes_q, nickles_q, pennies_q)
            if is_transection(total):
                update_resources(user_input)

    print("\n"*20)