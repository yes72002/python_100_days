from turtle import Screen
# from paddle_myself import Paddle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

PADDLE_R_POSITIONS = (350, 0)
PADDLE_L_POSITIONS = (-350, 0)
BOUNDARY_WALL = 280
BOUNDARY_PADDLE = 320
BOUNDARY_GAME = 400

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

r_paddle = Paddle(PADDLE_R_POSITIONS)
l_paddle = Paddle(PADDLE_L_POSITIONS)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall
    if (ball.ycor() >= BOUNDARY_WALL) or (ball.ycor() <= -BOUNDARY_WALL):
        ball.bounce_wall()

    # Detect collision with paddle
    if (ball.xcor() >= BOUNDARY_PADDLE) or (ball.xcor() <= -BOUNDARY_PADDLE):
        if ball.distance(r_paddle) < 50:
            ball.bounce_paddle()
        elif ball.distance(l_paddle) < 50:
            ball.bounce_paddle()
                
    if (ball.xcor() >= BOUNDARY_GAME):
        scoreboard.score_left_plus_1()
        ball.reset_position()

    if (ball.xcor() <= -BOUNDARY_GAME):
        scoreboard.score_right_plus_1()
        ball.reset_position()

screen.exitonclick()