import random
from turtle import Turtle
COLORS = ["red", "black", "yellow", "blue", "green", "cyan", "lightgreen", "turquoise", "skyblue"]
STARTING_MOVE_DISTANCE = 5
INCREMENT = 10


class Car:
    def __init__(self):
        self.all_cars = []

    def make_car(self):
        rand_num = random.randint(1, 10)
        if rand_num == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.goto(280, random.randint(-180, 190))
            new_car.color(random.choice(COLORS))
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.fd(STARTING_MOVE_DISTANCE)


