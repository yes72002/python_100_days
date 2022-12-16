def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for i in range(6): # 0, 1, 2, 3, 4, 5
    move_jump()