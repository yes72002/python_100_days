# method 1
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
    else:
        while wall_in_front():
            turn_left()
    move()
