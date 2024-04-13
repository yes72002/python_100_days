inputs = eval(input())
# eval creates list for inputs with format: [1,2,3]

# TODO: Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        output = function(args[0], args[1], args[2])
        # print(f"You called {function.__name__}({args[0]},{args[1]},{args[2]})")
        print(f"You called {function.__name__}{args}")
        print(f"It returned: {output}")
        
    return wrapper

# TODO: Use the decorator 👇
@logging_decorator
def a_function(a, b, c):
    return a * b * c

a_function(inputs[0], inputs[1], inputs[2])