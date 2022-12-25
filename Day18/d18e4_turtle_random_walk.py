from turtle import Turtle, Screen
import random

timmy = Turtle()

timmy.shape("turtle")
timmy.speed('fastest')
timmy.pensize(10)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
angle = [0, 90, 180, 270]

# random walk
for i in range(0,100):
    r = random.random()
    g = random.random()
    b = random.random()
    timmy.pencolor(r, g, b)
    # timmy.pencolor(random.choice(colours))
    timmy.forward(30)
    timmy.setheading(random.choice(angle))

my_sreen = Screen()
my_sreen.exitonclick()
