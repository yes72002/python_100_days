from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")
# FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.setposition(0, 260) # move writting position
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", True, align=ALIGNMENT, font=FONT)
        # self.write((0, 280), True) # write (0, 280)

    def score_plus_1(self):
        self.score += 1
        self.setposition(0, 260)
        self.clear()
        self.update_scoreboard()

    # def write(self): # don't declare write(self) again
        # super().write()
        # arg, move, align, font
        # arg="Score: "
        # self.move = False
        # self.align = "center"
        # self.font = 
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", True, align=ALIGNMENT, font=FONT)

