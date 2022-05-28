from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score=0
        self.penup()
        self.color("white")
        self.hideturtle()

        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(240, 260)
        self.write(f"score:{self.score}")
    def increase_score(self):
        self.score=self.score+20
        self.update_scoreboard()
    def win(self):
        self.goto(0, 0)
        self.write(f"You WIN")

    def lose(self):
        self.goto(0, 0)
        self.write(f"You Lose")

