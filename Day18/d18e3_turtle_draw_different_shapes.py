from turtle import Turtle, Screen
import random

timmy = Turtle()

timmy.shape("turtle")
timmy.color("coral")

# draw different shapes
for i in range(0,20):
    angle_sum = 0
    # timmy.color("coral")
    r = random.random()
    g = random.random()
    b = random.random()
    timmy.pencolor(r, g, b)
    while angle_sum < 360:
        timmy.forward(100)
        angle = 360 / (4 + i)
        timmy.right(angle)
        angle_sum += angle

my_sreen = Screen()
my_sreen.exitonclick()
