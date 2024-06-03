from turtle import Screen
# from paddle_myself import Paddle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from brick import Brick
import time
import math

PADDLE_POSITIONS = (0, -250)
BRICK_POSITIONS = (100, 100)
BOUNDARY_CEILING = 280
BOUNDARY_WALL = 380
BOUNDARY_PADDLE = -270
BOUNDARY_FLOOR = -290
BOUNDARY_GAME = 400

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)

paddle = Paddle(PADDLE_POSITIONS)
ball = Ball()
scoreboard = Scoreboard()
brick_11 = Brick((-300, 160), "blue")
brick_12 = Brick((-200, 160), "red")
brick_13 = Brick((-100, 160), "blue")
brick_14 = Brick((   0, 160), "red")
brick_15 = Brick(( 100, 160), "blue")
brick_16 = Brick(( 200, 160), "red")
brick_17 = Brick(( 300, 160), "blue")
brick_21 = Brick((-300, 130), "red")
brick_22 = Brick((-200, 130), "blue")
brick_23 = Brick((-100, 130), "red")
brick_24 = Brick((   0, 130), "blue")
brick_25 = Brick(( 100, 130), "red")
brick_26 = Brick(( 200, 130), "blue")
brick_27 = Brick(( 300, 130), "red")
brick_31 = Brick((-300, 100), "blue")
brick_32 = Brick((-200, 100), "red")
brick_33 = Brick((-100, 100), "blue")
brick_34 = Brick((   0, 100), "red")
brick_35 = Brick(( 100, 100), "blue")
brick_36 = Brick(( 200, 100), "red")
brick_37 = Brick(( 300, 100), "blue")

brick_set = [
    brick_11,
    brick_12,
    brick_13,
    brick_14,
    brick_15,
    brick_16,
    brick_17,
    brick_21,
    brick_22,
    brick_23,
    brick_24,
    brick_25,
    brick_26,
    brick_27,
    brick_31,
    brick_32,
    brick_33,
    brick_34,
    brick_35,
    brick_36,
    brick_37,
]

screen.listen()
screen.onkey(key="Right", fun=paddle.go_right)
screen.onkey(key="Left", fun=paddle.go_left)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # print(f"x = {ball.xcor()}")
    # print(f"y = {ball.ycor()}")

    # Detect collision with ceiling
    if (ball.ycor() >= BOUNDARY_CEILING):
        ball.bounce_ceiling()

    # Detect collision with paddle
    if (int(ball.ycor()) <= int(-BOUNDARY_PADDLE)): # ycor() not correct
        if ball.distance(paddle) < 50:
            ball.bounce_paddle()

    # Detect collision with floor
    if (ball.ycor() <= -BOUNDARY_FLOOR): # ycor() not correct
        # ball.reset_position()
        pass

    # Detect collision with right and left wall
    if (ball.xcor() >= BOUNDARY_WALL) or (ball.xcor() <= -BOUNDARY_WALL):
        ball.bounce_wall()

    for brick in brick_set:
        if ball.distance(brick) < 60:
            scoreboard.score_plus_1()
            brick.touch_delete()
            brick_set.remove(brick)
            ball.bounce_brick()


screen.exitonclick()