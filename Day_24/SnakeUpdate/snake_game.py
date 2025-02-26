import time
from turtle import Screen
from score_board import Scoreboard
from snake import Snake
from food import Food
score=0
screen=Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake=Snake()
food=Food()
scoreboard=Scoreboard()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        scoreboard.increment_score()
        print('nom nom nom')
        food.refresh()
        snake.snake_long()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset_score()
        snake.reset_snake()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            scoreboard.reset_score()
            snake.reset_snake()


screen.exitonclick()