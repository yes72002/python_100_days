from turtle import Screen
from cannon import Cannon
from cannonbase import CannonBase
from laser import Laser
from alien import Alien
from scoreboard import Scoreboard
from gameover import GameOver
import time

CANNON_POSITIONS = (0, -250)
BOUNDARY_GAME = 400

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.tracer(0)

cannon = Cannon(CANNON_POSITIONS)
cannonbase = CannonBase(CANNON_POSITIONS)
laser = Laser(CANNON_POSITIONS)
scoreboard = Scoreboard()
gameover = GameOver()
alien_11 = Alien((-300, 160), "blue")
alien_12 = Alien((-200, 160), "red")
alien_13 = Alien((-100, 160), "blue")
alien_14 = Alien((   0, 160), "red")
alien_15 = Alien(( 100, 160), "blue")
alien_16 = Alien(( 200, 160), "red")
alien_17 = Alien(( 300, 160), "blue")
alien_21 = Alien((-300, 130), "red")
alien_22 = Alien((-200, 130), "blue")
alien_23 = Alien((-100, 130), "red")
alien_24 = Alien((   0, 130), "blue")
alien_25 = Alien(( 100, 130), "red")
alien_26 = Alien(( 200, 130), "blue")
alien_27 = Alien(( 300, 130), "red")
alien_31 = Alien((-300, 100), "blue")
alien_32 = Alien((-200, 100), "red")
alien_33 = Alien((-100, 100), "blue")
alien_34 = Alien((   0, 100), "red")
alien_35 = Alien(( 100, 100), "blue")
alien_36 = Alien(( 200, 100), "red")
alien_37 = Alien(( 300, 100), "blue")

alien_set = [
    alien_11, alien_12, alien_13, alien_14, alien_15, alien_16, alien_17,
    alien_21, alien_22, alien_23, alien_24, alien_25, alien_26, alien_27,
    alien_31, alien_32, alien_33, alien_34, alien_35, alien_36, alien_37,
]
laser_set = []

def cannon_go_right():
    cannon.go_right()
    cannonbase.go_right()

def cannon_go_left():
    cannon.go_left()
    cannonbase.go_left()

def gen_laser():
    cannon_pos = cannon.position()
    # print(f"cannon_pos = {cannon_pos}")
    laser = Laser(cannon_pos)
    laser_set.append(laser)

screen.listen()
screen.onkey(key="Right", fun=cannon_go_right)
screen.onkey(key="Left", fun=cannon_go_left)
screen.onkey(key="space", fun=gen_laser)

game_is_on = True
count = 0
count_cannon = 1/laser.move_speed # 1 secs
# print(count_cannon)
count_move = 0
direction = 1

while game_is_on:
    screen.update()
    time.sleep(laser.move_speed)
    laser.move()
    for laserx in laser_set:
        # Detect collision with ceiling
        if (laserx.ycor() >= BOUNDARY_GAME):
            laserx.bounce_ceiling()
        else:
            laserx.move()

    # alien move per 1 secs
    if count == count_cannon:
        # print(f"direction = {direction}")
        # print(f"count_move = {count_move}")
        if abs(count_move) > 3:
            direction *= -1
        for alien in alien_set:
            alien.move_right(direction)

        count_move += direction
        count = 0
    count += 1

    if alien_set == []:
        gameover.show_gameover()
        game_is_on = False
    else:
        # Detect laser touch alien
        for alien in alien_set:
            if laser.distance(alien) < 60:
                scoreboard.score_plus_1()
                alien.touch_delete()
                alien_set.remove(alien)
                laser.bounce_alien()
            for laserx in laser_set:
                if laserx.distance(alien) < 60:
                    scoreboard.score_plus_1()
                    alien.touch_delete()
                    alien_set.remove(alien)
                    laserx.bounce_alien()


screen.exitonclick()