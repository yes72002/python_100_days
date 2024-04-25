from turtle import Turtle

MOVE_PADDLE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class CannonBase(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_cannonbase(position)

    def create_cannonbase(self, position):
        # Directly build a long turtle
        self.shape("square")
        self.penup()
        self.color("green")
        self.shapesize(stretch_len=3, stretch_wid=0.9)
        position = (position[0], position[1] - 15)
        self.goto(position)
        self.setheading(RIGHT)

    def go_right(self):
        self.forward(MOVE_PADDLE)

    def go_left(self):
        self.backward(MOVE_PADDLE)
