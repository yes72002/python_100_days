from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 40, "normal")
# FONT = ("Courier", 24, "normal")

class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()

    def show_gameover(self):
        self.setposition(0, 0)
        self.clear()
        self.write(f"GAME OVER", True, align=ALIGNMENT, font=FONT)