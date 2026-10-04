from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")

class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(position)
        self.hideturtle()

    def show_score(self):
        self.clear()
        self.write(self.score, align = ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align = ALIGNMENT, font=FONT)