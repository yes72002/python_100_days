from turtle import Turtle, Screen

timmy = Turtle()

timmy.shape("turtle")
timmy.color("coral")

# draw a square
for _ in range(4):
    timmy.forward(100)
    timmy.right(90)

my_sreen = Screen()
my_sreen.exitonclick()
