from turtle import Turtle

STARTING_POSITION = (0, -280)
UP = 90
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_player()
        self.move_speed = 0.1
    
    def create_player(self):
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.goto(STARTING_POSITION)
        self.setheading(UP)
    
    def move(self):
        self.forward(MOVE_DISTANCE)
    
    def reset_player(self,):
        self.move_speed *= 0.9
        self.goto(STARTING_POSITION)

