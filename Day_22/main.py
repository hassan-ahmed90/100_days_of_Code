#Game Setup (ScreenSize)
#Draw Game Elements (2 Paddles and 1 one Ball)
#Player Input (Moving Paddles up and down)
#Ball Movement (Update the ball movement Continiously)
#Ball Paddle Collision
#Scoring System
from score_board import Scoreboard
import time

from Day02.bmi_calculator import score
from paddles import Paddle
from turtle import Screen
from ball import Ball
screen = Screen()
screen.title("Pong Game")
screen.bgcolor('black')
screen.setup(height=600,width=800)
screen.tracer(0)


paddle1=Paddle((350,0))
paddle2=Paddle((-350,0))
ball=Ball()
score=Scoreboard()

screen.listen()
screen.onkey(paddle1.go_up,"Up")
screen.onkey(paddle1.go_down,"Down")

screen.onkey(paddle2.go_up,"w")
screen.onkey(paddle2.go_down,"s")

while True:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.paddle_bounce()

    if ball.distance(paddle1)<50 and ball.xcor()>340 or ball.distance(paddle2)<50 and ball.xcor()<-340:
        ball.bounce_x()

    if ball.xcor()>380:
        ball.reset_ball()
        score.updateScoreLeft()

    if ball.xcor()<-380:
        ball.reset_ball()
        score.updateScoreRight()





screen.exitonclick()

