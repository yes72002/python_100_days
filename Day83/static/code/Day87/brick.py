from turtle import Turtle
import random

MOVE_PADDLE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Brick(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.create_brick(position, color)

    def create_brick(self, position, color):
        # Directly build a long turtle
        # self = Turtle("square")
        self.shape("square")
        self.penup()
        self.color(color)
        # self.shapesize(stretch_len=1, stretch_wid=5)
        self.shapesize(stretch_len=4, stretch_wid=1)
        self.goto(position)
        self.setheading(RIGHT)

    def touch_delete(self):
        # self.clear()
        self.goto(-1000, -1000)
