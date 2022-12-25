from turtle import Turtle, Screen
import random

timmy = Turtle()

colors = ["light blue", "dark gray", "navy", "cyan", "medium aquamarine", "dark green", "khaki", "burlywood", "firebrick", "orange red", "light pink", "thistle", "light slate blue"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

for shaple_side_n in range(3, 11):
    timmy.color(random.choice(colors))
    draw_shape(shaple_side_n)

my_sreen = Screen()
my_sreen.exitonclick()
