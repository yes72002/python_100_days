# import turtle
# timmy = turtle.Turtle() # we've save it into an object called Timmy.

from turtle import Turtle, Screen
timmy = Turtle()
print(timmy) # <turtle.Turtle object at 0x00000222C141E3E0>

# change speed
# timmy.speed('normal') # normal = '6'
timmy.speed('slowest')# slowest = '1'

# move forward for 100 distance
timmy.forward(100)

# change shape
# before this line, the shape is a arrow.
timmy.shape("turtle") # change to actual turtle, the other method
timmy.shape("square")

# change color
# timmy.color("blue")
timmy.color("coral")
# timmy.color("darkolivegreen2")
# timmy.color("gold1")

# move forward for 100 distance
timmy.forward(100)

# show screen
my_sreen = Screen()
# object attribute
print(my_sreen.canvheight)
# the screen is the object and that height is an attribute

# object method
my_sreen.exitonclick() # click the screen and dispear


