import time
from turtle import Screen
from scoreboard import ScoreBoard
from timmy import Timmy
from cars import Car

my_screen = Screen()
my_screen.tracer(0)
scoreboard = ScoreBoard()
timmy = Timmy()
car = Car()
my_screen.screensize(400, 400)
my_screen.title("Turtle Crossing")
my_screen.listen()
my_screen.onkey(timmy.move, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    my_screen.update()
    car.make_car()
    car.move_car()
    for i in car.all_cars:
        if i.distance(timmy) < 25:
            game_is_on = False
            scoreboard.game_over()
        if timmy.crossed_finish_line():
            scoreboard.update_score()
            timmy.goto(0, -220)


my_screen.exitonclick()
