from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 40, "normal")
# FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.setposition(0, 220)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.setposition(0, 220)
        self.clear()
        self.write(f"{self.score}", True, align=ALIGNMENT, font=FONT)

    def score_plus_1(self):
        self.score += 1
        self.update_scoreboard()
