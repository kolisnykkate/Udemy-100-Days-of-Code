from turtle import Screen

import scoreboard
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
left_scoreboard = Scoreboard((-100, 200))
right_scoreboard = Scoreboard((100, 200))


screen.listen()
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")


screen.update()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    left_scoreboard.show_score()
    right_scoreboard.show_score()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320\
        or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    if ball.xcor() > 420:
        left_scoreboard.score += 1
        ball.reset()


    if ball.xcor() < -420:
        right_scoreboard.score += 1
        ball.reset()

    if left_scoreboard.score == 10 or right_scoreboard.score == 10:
        left_scoreboard.game_over()
        game_is_on = False




screen.exitonclick()