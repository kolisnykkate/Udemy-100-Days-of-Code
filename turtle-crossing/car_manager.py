from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager:

    def __init__(self):
        self.all_cars = []
        self.speed = 0.1

    def create_car(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.goto(300, random.randint(-250, 220))
        new_car.speed = self.speed
        self.all_cars.append(new_car)


    def car_move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def reset_cars(self):
        self.speed *= 0.6





