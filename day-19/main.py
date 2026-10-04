from turtle import Turtle, Screen

purple = Turtle()
screen = Screen()

def move_forward():
    purple.forward(10)

def move_backward():
    purple.backward(10)

def turn_right():
    purple.right(10)

def turn_left():
    new_heading = purple.heading() + 10
    purple.setheading(new_heading)

def clear_screen():
    purple.reset()



screen.listen()
screen.onkey(key="w" , fun=move_forward)
screen.onkey(key="s" , fun=move_backward)
screen.onkey(key="d" , fun=turn_right)
screen.onkey(key="a" , fun=turn_left)
screen.onkey(key="c" , fun=clear_screen)

screen.exitonclick()