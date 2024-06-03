from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# without inheritance
class CarManager():
    def __init__(self):
        self.car_list = []
        for i in range(0, 30):
            self.create_car()

    def create_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.goto(random.randint(250, 850), random.randint(-250, 250))
        # new_car.goto(random.randint(-250, 250), random.randint(-250, 250)) # test
        self.car_list.append(new_car)
    
    def move(self):
        # new_x = self.xcor() + self.x_move
        # new_y = self.ycor() + self.y_move
        # self.goto(new_x, new_y)
        for car in self.car_list:
            new_x = car.xcor() - MOVE_INCREMENT
            if new_x < -350:
                new_x = 350
            car.setx(new_x)