# import colorgram
# # Extract 6 colors from an image.
# colors = colorgram.extract('image.jpg', 30)
# rgb=[]
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb.append(new_color)
# print(rgb)
import random

hist_color=[(245, 243, 238), (246, 242, 244), (202, 164, 110),
            (240, 245, 241), (236, 239, 243), (149, 75, 50),
            (222, 201, 136), (53, 93, 123), (170, 154, 41),
            (138, 31, 20),(134, 163, 184), (197, 92, 73),
            (47, 121, 86), (73, 43, 35),  (145, 178, 149),
            (14, 98, 70), (232, 176, 165),
            (160, 142, 158), (54, 45, 50), (101, 75, 77),
            (183, 205, 171), (36, 60, 74), (19, 86, 89),
            (82, 148, 129), (147, 17, 19), (27, 68, 102),
            (12, 70, 64), (107, 127, 153), (176, 192, 208),
            (168, 99, 102)]

hello
normalized_colors = [(r / 255, g / 255, b / 255) for r, g, b in hist_color]
# 10 rows 10 col spots
# Dot size 20 and space is 50
from turtle import Turtle,Screen
t=Turtle()

# t.penup()
t.speed('fastest')
t.setheading(225)
t.forward(300)
t.setheading(0)

no_of_dots=100

for i in range(1,no_of_dots+1):
    t.dot(20,random.choice(normalized_colors))
    t.forward(50)
    if i%10==0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


screen=Screen()
screen.exitonclick()