# Python Decorator Function
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        # Or run it twice
        # Do something after
    return wrapper_function

# We can call the delay_decorator in fron of the method which we want to delay
@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

@delay_decorator
def say_greeting():
    print("How are you?")


say_hello()

decorated_function = delay_decorator(say_greeting)

