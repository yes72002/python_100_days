from MENU import MENU
import random

machine_water = random.randint(0, 500)
machine_milk = random.randint(0, 300)
machine_coffee = random.randint(0, 100)
machine_money = 0
# print(machine_money)

resources = {
    "water": machine_water,
    "milk": machine_milk,
    "coffee": machine_coffee,
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            return True

want = input("What would you like? (espresso/latte/cappuccino): ")

while want != "off":
    # want = "report"
    # want = "espresso"

    if want == "report":
        print(f"Water: {resources['water']}g")
        print(f"Milk: {resources['milk']}g")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${machine_money}")
    else:
        # check resources sufficient
        order_ingredients = MENU[want]["ingredients"]
        enough = is_resource_sufficient(order_ingredients)
        # insert money
        if enough == True:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: ")) * 0.25
            dimes = int(input("How many dimes?: ")) * 0.1
            nickles = int(input("How many nickles?: ")) * 0.05
            pennies = int(input("How many pennies?: ")) * 0.01
            insert_money = quarters + dimes + nickles + pennies
            print(f"insert money = {insert_money}")
            needed_cost = MENU[want]["cost"]
            # check money
            if insert_money < needed_cost:
                print("Sorry that's not enough money. Money refunded.")
            else:
                machine_money += insert_money
                # print(f"Money: ${machine_money}")
                change = round(insert_money - needed_cost, 2)
                print(f"Here is ${change} dollars in change.")
                for item in order_ingredients:
                    resources[item] -= order_ingredients[item]
                print(f"Here is your {want}. Enjoy!")

    want = input("What would you like? (espresso/latte/cappuccino): ")




