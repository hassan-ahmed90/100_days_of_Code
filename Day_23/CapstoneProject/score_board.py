from turtle import Turtle

FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1


    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 20)
        self.write("Game Over", align='center', font=("Arial", 20, 'normal'))

    def game_level(self):
        self.hideturtle()
        self.penup()
        self.goto(-230, 250)
        self.write(f"Level {self.level}", align='center', font=("Arial", 20, 'normal'))

    def update_level(self):
        self.clear()
        self.level+=1

