import turtle
from turtle import Turtle,Screen
import random
colors=["red","orange","yellow","green","blue","purple"]
y_pos=[-100,-60,-20,20,60,100]
all_turtle=[]
is_race_on=False
for turtle_index in range(0,6):
    t1=Turtle()
    t1.penup()
    t1.shape('turtle')
    t1.color(colors[turtle_index])
    t1.goto(x=-230,y=y_pos[turtle_index])
    all_turtle.append(t1)


screen=Screen()
screen.setup(height=400,width=500)

user_bet=screen.textinput("Turtle Race","Which turtle will win? ")
if user_bet:
    is_race_on=True
while is_race_on:
    for turtle in all_turtle:
        turtle.forward(random.randint(0,30))
        if turtle.xcor()>230:
            is_race_on=False
            win_col=turtle.pencolor()
            if win_col==user_bet:
                print(f"You won The {win_col} is the winning color.")
                is_race_on=False
            else:
                print(f"You have lost The {win_col} is the winning color")


#
#
# t2=Turtle()
# t2.penup()
# t2.shape('turtle')
# t2.color(colors[1])
# t2.goto(-230,-60)
#
#
# t3=Turtle()
# t3.penup()
# t3.shape('turtle')
# t3.color(colors[2])
# t3.goto(-230,-20)
#
#
# t4=Turtle()
# t4.penup()
# t4.shape('turtle')
# t4.color(colors[3])
# t4.goto(-230,20)
#
#
# t5=Turtle()
# t5.penup()
# t5.shape('turtle')
# t5.color(colors[4])
# t5.goto(-230,60)
#
#
# t6=Turtle()
# t6.penup()
# t6.shape('turtle')
# t6.color(colors[5])
# t6.goto(-230,100)

screen.exitonclick()