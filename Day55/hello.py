from flask import Flask

app = Flask(__name__)

# print(__name__)


def make_bold(function):
    def wrapper_function():
        text = function()
        return f"<b>{text}</b>"
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        text = function()
        return f"<em>{text}</em>"
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        text = function()
        return f"<u>{text}</u>"
    return wrapper_function


@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
            '<p>This is a paragraph.</p>' \
            '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaW02NzhjeWUwd3IxNWE0d3BiOXlnbDB0ZGx2MW5lZGFzeXZvem0yaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/EXEEJHIPpT4ZO/giphy.gif" width=200>'


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye"

# name
# @app.route("/username/<name>")
# @app.route("/<name>/jim")
# @app.route("/username/<path:name>")
# def greet(name):
    # return f"Hello {name}"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)


