import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(player.move_speed)
    screen.update()
    carmanager.move()
    
    # Detect collision with car.
    for car in carmanager.car_list:
        if player.distance(car) < 20:
            game_is_on = False
            print("crush")
            scoreboard.game_over()

    # Detect collision with finish line Y.
    if player.ycor() > 280:
        player.reset_player()
        scoreboard.score_plus_1()

screen.exitonclick()