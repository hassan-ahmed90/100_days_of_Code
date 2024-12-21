import turtle
from turtle import Turtle,Screen
import random


def chan_color():
    R = random.random()
    B = random.random()
    G = random.random()

    fire=(R,G,B)
    timmy.color(fire)

timmy =Turtle()
timmy.shape('turtle')
timmy.speed(15)
directions=[0,90,180,270]

for i in range(0,20):
    chan_color()
    timmy.width(25)
    timmy.forward(random.randint(30,90))
    timmy.right(random.choice(directions))


screen=Screen()
screen.exitonclick()