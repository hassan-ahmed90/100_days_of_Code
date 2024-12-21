from turtle import Turtle,Screen
import random
timmy=Turtle()
timmy.shape('turtle')

num_side=3
side=num_side/360

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    timmy.color(R, G, B)

def draw_shapes(numside):
    side =  360/numside
    for i in range(numside):
        timmy.forward(100)
        timmy.right(side)

for i in range(3,11):
    draw_shapes(i)
    change_color()

screen=Screen()
screen.exitonclick()