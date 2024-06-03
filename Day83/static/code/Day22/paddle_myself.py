from turtle import Turtle
import random

STARTING_POSITIONS = [(350, 40), (350, 20), (350, 0), (350, -20), (350, -40)]
MOVE_PADDLE = 20
UP = 90
DOWN = 270

class Paddle:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    def move_up(self):
        for seg_num in range(len(self.segments)-1, 0, -1): 
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_PADDLE)

    def move_down(self):
        for seg_num in range(0, len(self.segments)-1, 1):
            new_x = self.segments[seg_num + 1].xcor()
            new_y = self.segments[seg_num + 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.tail.forward(MOVE_PADDLE)

    def up(self):
        self.head.setheading(UP)
        self.move_up()
    
    def down(self):
        self.tail.setheading(DOWN)
        self.move_down()
