from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
# FONT = ("Courier", 24, "normal")

SCOREBOARD_POSITION = (-220, 250)
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(SCOREBOARD_POSITION)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.goto(SCOREBOARD_POSITION)
        self.clear()
        self.write(f"Level: {self.score}", True, align=ALIGNMENT, font=FONT)
    
    def score_plus_1(self):
        self.score += 1
        self.goto(SCOREBOARD_POSITION)
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", True, align=ALIGNMENT, font=FONT)
