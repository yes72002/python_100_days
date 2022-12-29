from turtle import Turtle
import random

# PADDLE_POSITIONS = (350, 0)
MOVE_PADDLE = 20
UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        # Directly build a long turtle
        # self = Turtle("square")
        self.shape("square")
        self.penup()
        self.color("white")
        # self.shapesize(stretch_len=1, stretch_wid=5)
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.goto(position)
        self.setheading(UP)

    def go_up(self):
        self.setheading(UP)
        self.forward(MOVE_PADDLE)
    
    def go_down(self):
        # self.head.setheading(UP)
        # self.forward(MOVE_PADDLE)
        self.backward(MOVE_PADDLE)
