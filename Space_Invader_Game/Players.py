from turtle import Turtle,Screen
import time
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.y=0



    def create_player(self):
        screen=Screen()
        screen.addshape('player.gif')
        screen.tracer(0)
        self.shape('player.gif')
        self.penup()
        self.goto(0, -240)
    def left(self):
        if self.xcor()>-260:
            self.setheading(180)
            self.forward(20)



    def right(self):
        if self.xcor()<260:
            self.setheading(0)
            self.forward(20)


    def x_cor(self):
        self.x=self.xcor()
        return self.x
    # def bullet(self):
    #     if self.bulletstate=="ready":
    #         self.bulletstate="fire"
    #         bullet=Turtle()
    #         bullet.color("white")
    #         bullet.shape("square")
    #         bullet.penup()
    #         bullet.shapesize(stretch_wid=0.5, stretch_len=0.1)
    #         bullet.goto(self.x,-230)



