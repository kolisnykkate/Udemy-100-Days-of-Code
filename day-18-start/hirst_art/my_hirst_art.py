import random
from screen import my_screen
import screen
import colors
import my_turtle
from dot import Dot



dot = Dot(20, 50, 50 )

dot_in_row = dot.dot_num(screen.screen_width)
dot_in_column = dot.dot_num(screen.screen_height)


x_pos = -(screen.screen_width / 2 - dot.wall_distance)
y_pos = -(screen.screen_height / 2 - dot.wall_distance)

for _ in range(dot_in_column):
    my_turtle.start(x_pos, y_pos)

    for _ in range(dot_in_row):
        my_turtle.purple.color(random.choice(colors.rgb_list))
        my_turtle.purple.up()
        my_turtle.purple.dot(dot.radius)
        my_turtle.purple.forward(dot.distance)

    y_pos += dot.distance


my_screen.exitonclick()