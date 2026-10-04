import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.bgcolor()
screen.tracer(0)


player = Player()
car = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move, "Up")
screen.onkey(player.move, "space")

cycle = 0
game_is_on = True
while game_is_on:

    time.sleep(car.speed)
    screen.update()
    scoreboard.show_level()

    if cycle%6==0:
        car.create_car()
    car.car_move()
    cycle += 1

    if player.ycor() > FINISH_LINE_Y:
        scoreboard.level += 1
        player.reset_player()
        car.reset_cars()

    for c in car.all_cars:
        if c.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False





screen.exitonclick()