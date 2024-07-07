from turtle import Turtle


class Timmy(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(0, -200)

    def move(self):
        self.fd(10)

    def crossed_finish_line(self):
        if self.ycor() > 200:
            return True
        else:
            return False
