from turtle import Turtle

class Laser(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_laser(position)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1 # fast
        # self.move_speed = 0.5 # middle
        # self.move_speed = 1 # slow

    def create_laser(self, position):
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=0.5, stretch_wid=1)
        self.goto(position)

    def move(self):
        new_x = self.xcor() + 0
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_ceiling(self):
        new_x = self.xcor()
        new_y = self.ycor()
        self.goto(new_x, new_y)
        # self.goto(-1000, -1000)

    def bounce_alien(self):
        # self.y_move *= -1
        self.goto(1000, 1000)
