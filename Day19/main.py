from turtle import Turtle,Screen

timmy=Turtle()
screen=Screen()

def move():
    timmy.forward(15)



screen.listen()
screen.onkey(key='w',fun=move)
screen.exitonclick()