import random
from turtle import Turtle,Screen

timmy=Turtle()
timmy.shape('turtle')
def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    timmy.color(R, G, B)

# timmy.color('red')
#
# for i in range(4):
#     timmy.forward(100)
#     timmy.left(90)
# for i in range(10):
#     timmy.forward(10)
#     timmy.color('white')
#     timmy.forward(10)
#     timmy.color("black")
#
# for i in range(15):
#     timmy.forward(10)
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#
#

for i in range(3):
    change_color()
    timmy.forward(100)
    timmy.right(120)

for i in range(4):
    change_color()
    timmy.forward(100)
    timmy.right(90)

for i in range(5):
    change_color()
    timmy.forward(100)
    timmy.right(72)

for i in range(6):
    change_color()
    timmy.forward(100)
    timmy.right(60)

for i in range(7):
    change_color()
    timmy.forward(100)
    timmy.right(51.4)

for i in range(8):
    change_color()
    timmy.forward(100)
    timmy.right(45)

for i in range(9):
    change_color()
    timmy.forward(100)
    timmy.right(40)

for i in range(10):
    change_color()
    timmy.forward(100)
    timmy.right(36)

screen=Screen()
screen.exitonclick()

# import turtle (when we use Class only 1-2 times)
# import turtle from Turtle (when we use class many times)
# import turtle as t (then we can call it t.Turtle())
# import turtle from* (when we import all classes from turtle package)

import heroes