from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.ht()
        self.penup()
        self.goto(-200, 200)
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, "center", ("Arial", 25, "normal"))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Level {self.score}", False, "center", ("Arial", 20, "normal"))
