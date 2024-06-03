from turtle import Turtle

MOVE_PADDLE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Alien(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.create_brick(position, color)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1 # fast
        # self.move_speed = 1 # slow

    def create_brick(self, position, color):
        # Directly build a long turtle
        # self = Turtle("square")
        self.shape("turtle")
        self.penup()
        self.color(color)
        self.shapesize(stretch_len=1, stretch_wid=1)
        # self.shapesize(stretch_len=2, stretch_wid=2) # bigger turtle
        self.goto(position)
        self.setheading(DOWN)

    def touch_delete(self):
        # self.clear()
        self.goto(-1000, -1000)

    def move_right(self, direction):
        new_x = self.xcor() + (self.x_move * direction)
        new_y = self.ycor() + 0
        self.goto(new_x, new_y)
