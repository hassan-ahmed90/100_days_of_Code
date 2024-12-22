

# W forward
# S backward
# A left Anti-Clockwise
# D Right Clockwise
# C Clear Drawings

from turtle import Turtle,Screen
def move_for():
    t.forward(20)
def lefty():
    t.left(10)
def righty():
    t.right(10)
def back():
    t.backward(10)

def clear_sc():
    t.clear()
    t.penup()
    t.home()
    t.pendown()




t=Turtle()
s=Screen()
s.listen()

s.onkey(key="w",fun=move_for)
s.onkey(key="s",fun=back)
s.onkey(key="a",fun=lefty)
s.onkey(key="d",fun=righty)
s.onkey(key="c",fun=clear_sc)
s.exitonclick()