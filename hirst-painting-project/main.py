import random
import turtle
from turtle import Turtle, Screen
rgb_colors = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
              (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
              (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
              (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19),
              (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

screen = Screen()
turtle.colormode(255)
screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)
tommy = Turtle()
tommy.penup()
tommy.pensize(15)
tommy.speed(10)
tommy.ht()


def draw_row():
    for i in range(10):
        tommy.dot(20, random.choice(rgb_colors))
        tommy.fd(50)


def draw_paint():
    for i in range(5):
        draw_row()
        tommy.left(90)
        tommy.fd(50)
        tommy.left(90)
        tommy.fd(50)
        draw_row()
        tommy.right(90)
        tommy.fd(50)
        tommy.right(90)
        tommy.fd(50)


draw_paint()
screen.exitonclick()
