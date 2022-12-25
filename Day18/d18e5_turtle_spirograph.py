from turtle import Turtle, Screen
# import turtle as turtle
import turtle
import random

timmy = Turtle()
turtle.colormode(255)
timmy.shape("turtle")
timmy.speed('fastest')

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

# Spirograph
gap = 10
for i in range(0, 360, gap):
    timmy.pencolor(random_color())
    timmy.circle(radius=100)
    timmy.setheading(i)

my_sreen = Screen()
my_sreen.exitonclick()

