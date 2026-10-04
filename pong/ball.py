from turtle import Turtle
from random import randint

MOVE_DISTANCE = 20

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.set_heading()
        self.move_speed = 0.1

    def set_heading(self):
        self.setheading(randint(0, 360))
        if self.heading() % 90 == 0:
            self.set_heading()

    def reset(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.set_heading()


    def move(self):
        self.forward(MOVE_DISTANCE)

    def wall_bounce(self):
        self.setheading(- self.heading())

    def paddle_bounce(self):
        self.setheading(180 - self.heading())
        self.move_speed *= 0.9


