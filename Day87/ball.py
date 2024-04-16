from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1 # fast
        # self.move_speed = 0.5 # fast
        # self.move_speed = 1 # slow

    def create_ball(self):
        self.shape("circle")
        self.penup()
        self.color("white")
        # self.shapesize(stretch_len=1, stretch_wid=1)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce_ceiling(self):
        self.y_move *= -1

    def bounce_wall(self):
        self.x_move *= -1
    
    def bounce_paddle(self):
        self.y_move *= -1
        # self.move_speed *= 0.9
    
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_paddle()

    def bounce_brick(self):
        self.y_move *= -1
