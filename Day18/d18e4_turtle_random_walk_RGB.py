from turtle import Turtle, Screen
# import turtle as turtle
import turtle
import random

timmy = Turtle()
turtle.colormode(255)
timmy.shape("turtle")
timmy.speed('fastest')
timmy.pensize(10)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

angle = [0, 90, 180, 270]

# random walk
for i in range(0,100):
    timmy.pencolor(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(angle))

my_sreen = Screen()
my_sreen.exitonclick()
