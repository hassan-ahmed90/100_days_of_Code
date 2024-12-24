import turtle
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} ", align="center",
                   font=("candara", 24, "bold"))
    def game_over(self):
        self.goto(0,0)
        self.write(" Game Over ", align="center",
                   font=("candara", 24, "bold"))

    def increment_score(self):
        """Increments the score and updates the display."""
        self.score += 1
        self.update_scoreboard()

# import turtle
# from turtle import Turtle
# class Scoreborad(Turtle):
#     super().__init__()
#     score=0
#     turtle.speed(0)
#     turtle.shape("square")
#     turtle.color("white")
#     turtle.penup()
#     turtle.hideturtle()
#     turtle.goto(0, 250)
#     turtle.write("Score : 0  High Score : 0", align="center",
#               font=("candara", 24, "bold"))