from turtle import Turtle, Screen

timmy = Turtle()

timmy.shape("turtle")
timmy.color("coral")

# draw a dashed line
for _ in range(50):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

my_sreen = Screen()
my_sreen.exitonclick()
