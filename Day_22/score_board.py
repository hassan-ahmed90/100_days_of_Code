from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.l_score=0
        self.r_score=0
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.goto(-200, 100)
        self.write(self.l_score, align='center', font=("Courier", 80, 'normal'))
        self.goto(200, 100)
        self.write(self.r_score, align='center', font=("Courier", 80, 'normal'))

    def updateScoreLeft(self):
        self.l_score+=1
        self.update()

    def updateScoreRight(self):
        self.r_score+=1
        self.update()
