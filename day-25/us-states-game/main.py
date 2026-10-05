import turtle
import pandas as pd
from PIL import Image

IMAGE = "blank_states_img.gif"

with Image.open(IMAGE) as img:
    width, height = img.size

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=width, height=height)
screen.bgpic(IMAGE)
# turtle.shape(image)



states_data = pd.read_csv("50_states.csv")
guessed_states = []
states_list = states_data.state.to_list()
print(states_list)

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        states_to_learn = [state for state in states_list if state not in guessed_states]
        # pd.Series(states_to_learn).to_csv("states_to_learn.csv", index=False)
        new_data = pd.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states_list:
        # position = (states_data.x[states_data["state"] == answer_state].iloc[0],
        #             states_data.y[states_data["state"] == answer_state].iloc[0])
        state_data = states_data[states_data.state == answer_state]
        guessed_states.append(answer_state)
        turtle.penup()
        turtle.hideturtle()
        # turtle.goto(position)
        turtle.goto(state_data.x.item(), state_data.y.item())
        # turtle.write(answer_state, align="center", font=("Arial", 10, "normal"))
        turtle.write(state_data.state.item())
    else:
        continue






# screen.mainloop()

screen.exitonclick()