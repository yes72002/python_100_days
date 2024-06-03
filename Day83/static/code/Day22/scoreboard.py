from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 40, "normal")
# FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_right = 0
        self.score_left = 0
        self.penup()
        self.color("white")
        self.setposition(0, 220) # move writting position
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.setposition(0, 220)
        self.clear()
        self.write(f"{self.score_left} : {self.score_right}", True, align=ALIGNMENT, font=FONT)

    def score_right_plus_1(self):
        self.score_right += 1
        self.update_scoreboard()
    
    def score_left_plus_1(self):
        self.score_left += 1
        self.update_scoreboard()


