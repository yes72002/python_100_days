from turtle import Turtle
import random

RANGE_X_POSI = 80
RANGE_y_POSI = 80

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # 10 = 20 * 0.5
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-RANGE_X_POSI, RANGE_X_POSI)
        random_y = random.randint(-RANGE_y_POSI, RANGE_y_POSI)
        self.goto(random_x, random_y)
