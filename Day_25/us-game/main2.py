import turtle
from turtle import Turtle

import pandas as pd


screen=turtle.Screen()
screen.title("US State Game")
image='blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

df =pd.read_csv('50_states.csv')
all_state=df.state.to_list()
guess_state=[]
while len(guess_state)<50:
    answer_state = screen.textinput(f"Guess the State ({len(guess_state)}/50)", prompt="Enter the another state name").title()
    if answer_state == "Exit":
        missing_state=[state for state in all_state if state not in guess_state]
        # for state in all_state:
        #     if state not in guess_state:
        #         missing_state.append(state)
        new_data=pd.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_state:
        guess_state.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=df[df.state==answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)

screen.exitonclick()
