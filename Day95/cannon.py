from turtle import Turtle

MOVE_CANNON = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Cannon(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_cannon(position)

    def create_cannon(self, position):
        # Directly build a long turtle
        # self = Turtle("square")
        self.shape("triangle")
        self.penup()
        self.color("green")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.goto(position)
        self.setheading(UP)

    def go_right(self):
        self.right(90)
        self.forward(MOVE_CANNON)
        self.left(90)

    def go_left(self):
        self.right(90)
        self.backward(MOVE_CANNON)
        self.left(90)
