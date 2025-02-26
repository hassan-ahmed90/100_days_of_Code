import random as r
import time
from distutils.util import byte_compile
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move=10
        self.y_move=10
        self.ball_speed=0.1

    def move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)

    def paddle_bounce(self):
        self.y_move*= -1

    def bounce_x(self):
        self.x_move*=-1
        self.ball_speed*=0.9
        # self.setx(self.xcor() + self.x_move)
        # self.sety(self.ycor() + self.y_move)

    def reset_ball(self):
        self.goto(0,0)
        self.ball_speed=0.1
        self.bounce_x()

    #
    # def wall_bounce(self):
    #     self.y_move *= -1
    #
    #
    # def paddle_bounce(self):
    #     self.x_move *= -1
    #
    #
    # def reset(self):
    #     self.goto(0, 0)
    #     self.rand_pos()