from turtle import Turtle

FONT = ("Courier", 24, "normal")
POSITION = (-270, 250)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(POSITION)
        self.level = 1

    def show_level(self):
        self.clear()
        text = f"Level: {self.level}"
        self.write(text, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        text = f"Game Over!"
        self.write(text, align = "center", font=FONT)


