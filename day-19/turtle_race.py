from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)

def create_turtle(turtle_color):
    """Create an instance of the Turtle class, set its color."""
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(turtle_color)
    return turtle

def random_speed(racer):
    """Randomly change the distance the turtle moves forward."""
    racer.forward(random.randint(0, 50))

def check_bet(user_bet, finishers):
    """ Check if the user's bet is the winner of the race. """
    if user_bet.lower() == finishers[0].color()[0]:
        print("You win!")
    else:
        print(f"You lose! The {finishers[0].color()[0]} turtle won the race! ")

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
x = -230
y = -100
turtles = []
for color in colors:
    turtle = create_turtle(color)
    turtles.append(turtle)
    turtle.goto(x, y)
    y += 40

finishers = []
while len(turtles) > 0:
    for turtle in turtles.copy():
        random_speed(turtle)
        if turtle.xcor() > 240:
            finishers.append(turtle)
            turtles.remove(turtle)


check_bet(user_bet, finishers)


screen.exitonclick()