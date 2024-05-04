def add(*arg):
    print(arg[0])
    sum = 0
    for n in arg:
        sum += n
    return sum
# print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

def calculate(n, **kwargs):
    # print(type(kwargs)) # dictionary
    # for key, value in kwargs.items():
        # print(key)
        # print(values)
    n += kwargs["add"] # 5 = 2 + 3
    n *= kwargs["multiply"] # 10 = 2 * 5
    # print(n) # 25
calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        # self.make = kw["make"]
        self.make = kw.get("make") # if it doesn't exist, return None
        # self.model = kw["model"]
        self.model = kw.get("model") # if it doesn't exist, return None
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

# my_car = Car(make="Nissan", model="GT-R")
my_car = Car(make="Nissan")
# print(my_car.model) # error, use bracket["model"]
print(my_car.model) # return None

