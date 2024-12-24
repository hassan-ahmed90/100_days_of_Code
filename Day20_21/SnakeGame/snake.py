from turtle import Turtle


STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE=20
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]
        self.direction="right"

    def create_snake(self):
        for turtle in STARTING_POSITION:
            t = Turtle('square')
            t.color('white')
            t.penup()
            t.goto(turtle)
            self.segments.append(t)

    def snake_long(self):
        t = Turtle('square')
        t.color('white')
        t.penup()
        self.segments.append(t)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)


    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[seg - 1].xcor()
            y_cor = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x_cor, y_cor)
        self.segments[0].forward(DISTANCE)








