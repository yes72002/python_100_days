# import colorgram

# rgb_colors = []
# colors = colorgram.extract('hirst_paint.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)
# delete top 3 color, because it's background's color

from turtle import Turtle, Screen
# import turtle as turtle
import turtle
import random

timmy = Turtle()
turtle.colormode(255)
timmy.shape("turtle")
timmy.speed('fastest')

color_list = [(108, 173, 204), (204, 168, 10), (32, 122, 154), (234, 142, 73), (204, 134, 175), (175, 9, 71), (207, 78, 115), (221, 235, 243), (231, 207, 115), (155, 60, 117), (119, 196, 175), (232, 165, 188), (160, 97, 24), (51, 171, 106), (23, 149, 90), (76, 17, 10), (1, 89, 114), (32, 156, 194), (96, 120, 182), (179, 8, 3), (7, 56, 134), (151, 211, 181), (230, 81, 70), (62, 10, 59), (7, 25, 94), (249, 159, 142), (3, 50, 29)]

timmy.hideturtle()
timmy.penup()
timmy.setposition(-200, -200)

# hirst painting
for i in range(0, 10):
    for _ in range(0, 10):
        color = random.choice(color_list)
        timmy.dot(20, color)
        timmy.forward(50)
    timmy.setposition(timmy.position() + (-500, 50))

my_sreen = Screen()
my_sreen.exitonclick()

