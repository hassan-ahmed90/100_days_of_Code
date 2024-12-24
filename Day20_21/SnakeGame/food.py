import turtle
from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        x_corrr = random.randint(-280, 300)
        y_corrr = random.randint(-280, 300)
        self.goto(x_corrr, y_corrr)

