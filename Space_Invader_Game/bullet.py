from turtle import Turtle,Screen
from Players import Player
import time
class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.bulletstate="ready"





    def bullet(self):

        if self.bulletstate=="ready":
            self.bulletstate="fire"
            self.penup()
            self.speed()
            self.color("white")
            self.shape("square")
            print(Player().x_cor())
            self.shapesize(stretch_wid=0.5, stretch_len=0.1)

            # while(self.ycor()<310):
            #
            #     time.sleep(0.001)
            #     Screen().tracer(0)
            #     self.goto(self.xcor(),self.ycor()+10)
            #     Screen().update()
            # self.bulletstate = "ready"


