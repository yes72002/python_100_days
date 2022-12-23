from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# MenuItem has already been built, so you don't have to declare it again
# espresso = MenuItem
# espresso.name = "espresso"
# espresso.cost = 1.5
# espresso.ingredients = {"water": 50, "coffee": 18}
# # print(espresso.name)
# # print(espresso.cost)
# # print(espresso.ingredients)
# latte = MenuItem
# latte.name = "latte"
# latte.cost = 2.5
# latte.ingredients = {"water": 200, "milk": 150, "coffee": 24}
# cappuccino = MenuItem
# cappuccino.name = "latte"
# cappuccino.cost = 3.0
# cappuccino.ingredients = {"water": 250, "milk": 100, "coffee": 24}

money = MoneyMachine()
# money.report() # call report method
machine = CoffeeMaker()
my_menu = Menu()
# print(my_menu.get_items()) # latte/espresso/cappuccino/

want = input(f"What would you like? ({my_menu.get_items()}): ")

while want != "off":
    if want == "report":
        machine.report()
        money.report()
    else:
        order = my_menu.find_drink(want)    
        enough = machine.is_resource_sufficient(order)
        # insert money
        if enough == True:
            needed_cost = order.cost
            # check money
            payment_accepted = money.make_payment(needed_cost)
            if payment_accepted == True:
                machine.make_coffee(order)

    want = input("What would you like? (latte/espresso/cappuccino): ")