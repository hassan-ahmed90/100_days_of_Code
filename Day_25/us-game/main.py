import turtle
from turtle import Turtle

import pandas as pd


screen=turtle.Screen()
screen.title("US State")
image='blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

df =pd.read_csv('50_states.csv')
x_list=df['x'].tolist()
y_list=df['y'].tolist()
state_name=df['state'].tolist()
size_of_data=df.shape[0]
print(size_of_data)
count=[]
while size_of_data+1>len(count):
    answer_state=screen.textinput(f"Guess the State ({len(count)}/50)",prompt="Enter the another state name").title()
    if answer_state=='Exit':
        with open('entered_states.csv',mode='w') as entered_csv:
            for state in state_name:
                if state not in count:
                    entered_csv.write(state+"\n")
        break
    if answer_state in state_name:
        answer_row=df.loc[df['state']==answer_state]
        print(answer_row)
        x_cor=answer_row['x'].iloc[0]
        y_cor=answer_row['y'].iloc[0]
        print(x_cor,y_cor)
        t1=Turtle()
        t1.hideturtle()
        t1.penup()
        t1.goto(float(x_cor),float(y_cor))
        t1.write(answer_state,align='center',font=("Arial",10,"normal"))
        count.append(answer_state)


