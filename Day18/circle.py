from random import randint
from turtle import Turtle,Screen
import random

t = Turtle()
t.shape('turtle')

def circle_color():
    R = random.random()
    B = random.random()
    G = random.random()
    t.color(R, G, B)

t.speed(10000)
def draw_spiro(size):
    for i in range(int(360/size)):
        t.circle(100)
        t.setheading(t.heading()+size)
        circle_color()

draw_spiro(5)



screen=Screen()
screen.exitonclick()