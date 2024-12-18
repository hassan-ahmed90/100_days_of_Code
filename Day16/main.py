import turtle
from turtle import Turtle, Screen

timmy=Turtle()
print(timmy)
timmy.shape('turtle')
timmy.color('red')
timmy.fillcolor('yellow')
turtle.forward(100)
timmy.position()
timmy.fd(100)
# turtle.goto(100,100)

turtle_screen= Screen()
print(turtle_screen.canvheight)
turtle_screen.exitonclick()