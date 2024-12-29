from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        try:
            with open('data.txt', mode='r') as score_file:
                self.high_score = int(score_file.read())
        except FileNotFoundError:
            self.high_score = 0
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
        self.write(f"Score : {self.score} High Score = {self.high_score} ", align="center",
                   font=("candara", 24, "bold"))
        with open('data.txt', mode='w') as score:
            score.write(str(self.high_score))
    def game_over(self):
        self.goto(0,0)
        self.write(" Game Over ", align="center",
                   font=("candara", 24, "bold"))

    def reset_score(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open('data.txt', mode='w') as score_file:
                score_file.write(str(self.high_score))
        self.score=0
        self.update_scoreboard()

    def increment_score(self):
        """Increments the score and updates the display."""
        self.score += 1
        self.update_scoreboard()

