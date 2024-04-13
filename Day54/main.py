# Functions with inputs/functionality/output
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def devide(n1, n2):
    return n1 / n2


# First-class objects, can be passed around as arguments e.g. int/string/float etc.
# pass function as a argument
def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)

result = calculate(add, 2, 3)
print(result)

result = calculate(multiply, 2, 3)
print(result)

# Nested Functions
# outside the function
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

# nested_function()
# ERROR
# nested_function()
#     ^^^^^^^^^^^^^^^
# NameError: name 'nested_function' is not defined. 
# Did you mean: 'outer_function'?

# inside the function
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    nested_function()

outer_function()