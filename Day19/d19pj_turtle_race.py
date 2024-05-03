from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [125, 75, 25, -25, -75, -125]

turtle_list = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    # new_turtle.speed("fastest")
    # new_turtle.speed("slowest")
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    turtle_list.append(new_turtle) # Put object into a list
    # even though the objects are the same name, it's available

is_going = False
if user_bet: # exist
    is_going = True

while is_going:
    for turtle in turtle_list: # useful
        # print(turtle.xcor()) # remember the parentheses
        if (turtle.xcor() > 230) and (is_going == True):
            is_going = False
            # turtle.color() # return (pencolor, fillcolor)
            if turtle.pencolor() == user_bet:
                print(f"You've won! The {turtle.pencolor()} turtle is the winner.")
            else:
                print(f"You've lost! The {turtle.pencolor()} turtle is the winner.")
        # turtle.forward(random.randint(0, 10)) # keep running even if the winner exists
        if is_going == True:
            turtle.forward(random.randint(0, 10))

screen.exitonclick()

