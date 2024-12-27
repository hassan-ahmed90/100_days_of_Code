import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
y_pos=[-100,-40,20,80,140,200]

class CarManager:
    def __init__(self):
        super().__init__()
        self.all_cars=[]
        self.move_distance=STARTING_MOVE_DISTANCE
    def car_create(self):
        if random.randint(1, 6) == 1:
        # for i in range(len(COLORS)):
            car=Turtle('square')
            car.shapesize(stretch_len=2,stretch_wid=1)
            car.penup()
            car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)  # Randomize Y-coordinate
            car.goto(300, random_y)
            # car.goto(300,y_pos[i])
            self.all_cars.append(car)

    def car_moving(self):
        for turtle in self.all_cars:
            turtle.backward(self.move_distance)


    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT