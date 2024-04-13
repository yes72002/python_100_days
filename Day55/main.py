from flask import Flask



class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False
        

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("Jim")
new_user.is_logged_in = True
create_blog_post(new_user)



# def make_bold(function):
#     def wrapper_function():
#         text = function()
#         return f"<b>{text}</b>"
#     return wrapper_function

# def make_emphasis(function):
#     def wrapper_function():
#         text = function()
#         return f"<em>{text}</em>"
#     return wrapper_function

# def make_underlined(function):
#     def wrapper_function():
#         text = function()
#         return f"<u>{text}</u>"
#     return wrapper_function


# if __name__ == "__main__":
#     app.run(debug=True)


