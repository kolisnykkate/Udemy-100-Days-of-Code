import turtle as t
import random

purple = t.Turtle()
t.colormode(255)
purple.shape("turtle")
# purple.color("purple")
purple.speed(0)

screen = t.Screen()
screen.setup(1200,1000)


# def draw_square():
#     for i in range(4):
#         purple.forward(100)
#         purple.left(90)
#
# draw_square()


# purple.teleport(-600, 0)
# for _ in range(50):
#     purple.forward(10)
#     purple.penup()
#     purple.forward(10)
#     purple.pendown()

# sides = 2
# for shapes in range(8):
#     random_hex = f"#{random.randint(0, 0xFFFFFF):06x}"
#     purple.color(random_hex)
#     for i in range(sides):
#         purple.forward(100)
#         purple.right(360/sides)
#     sides += 1

# purple.pensize(10)
# direction = (0, 90, 180, 270)
# purple.speed(10)
# for _ in range(100):
#
#     random_rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     purple.color(random_rgb)
#     purple.setheading(random.choice(direction))
#     purple.forward(20)

# circles = 50
# for _ in range(circles):
#     random_rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     purple.color(random_rgb)
#     purple.circle(100, 360, 50)
#     # purple.left(360/circles)
#     purple.setheading(purple.heading() + (360/circles))

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        random_rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        purple.color(random_rgb)
        purple.circle(100, 360, 50)
        purple.setheading(purple.heading() + size_of_gap)

draw_spirograph(5)



screen.exitonclick()





