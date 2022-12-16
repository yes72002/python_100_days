def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# conditions
# front_is_clear()
# wall_in_front()
# at_goal()
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()