# Functions can be returned from other function
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function

inner_function = outer_function()
inner_function()