import time
import turtle
from turtle import  Turtle, Screen
import pandas
screen = Screen()
screen.title("US States Game")
screen.setup(height=600, width=800)
screen.bgpic("blank_states_img.gif")
FONT = ("areial",15,"normal")
player = Turtle()
player.hideturtle()
player.penup()
player.color ("Black")

data = pandas.read_csv("50_states.csv")
states = data.state
states_list = states.to_list()

repetetive_list = []

score = 0

def get_location(state):
    state_row =  data[data["state"] == state]
    x_cor = state_row["x"]
    y_cor = state_row.y.item()
    return (int(x_cor),int(y_cor))

is_game_on = True




while is_game_on :
    time.sleep(0.3)
    answer = screen.textinput(title=f"{score}/50 States Correct", prompt=" Enter a State Name!").title()
    if answer not in repetetive_list and answer in states_list :
        player.goto(get_location(answer))
        print(get_location(answer))
        player.write(answer,font=FONT)
        repetetive_list.append(answer)
        score += 1

    if answer.lower() == "exit":
        is_game_on = False
        new_list = []
        for states in states_list:
            if states not in repetetive_list:
                new_list.append(states)
        missed_states_csv = pandas.DataFrame(new_list).to_csv("missed_states")

    screen.update()


# turtle.mainloop()