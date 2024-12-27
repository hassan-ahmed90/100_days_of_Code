import time
from turtle import Screen

from Day_23.CapstoneProject.score_board import ScoreBoard
from car_manage import CarManager
from player import Player
screen=Screen()
screen.setup(600,600)
screen.bgcolor('white')
screen.tracer(0)

player=Player()
car =CarManager()
score = ScoreBoard()

screen.listen()
screen.onkey(player.on_up,"Up")
game_off=True
while game_off:
    time.sleep(0.1)
    car.car_create()
    car.car_moving()
    score.game_level()
    for cars in car.all_cars:
        if player.distance(cars)<20:
            game_off=False
            score.game_over()

    if player.ycor()>290:
        player.level_up()
        car.increase_speed()
        score.update_level()


    screen.update()
screen.mainloop()