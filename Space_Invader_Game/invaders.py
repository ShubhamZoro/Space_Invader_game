from turtle import Turtle,Screen
class Invader():
    def __init__(self):
        super().__init__()
        self.invaders=[]
        self.create_invader()


    def create_invader(self):


        y = 220
        for i in range(3):
            x=-180

            for j in range(6):
                invader = Turtle()
                invader.penup()

                screen=Screen()
                screen.addshape('invader.gif')
                screen.tracer(0)
                invader.shape('invader.gif')
                invader.penup()
                invader.goto(x + 60 * j+j*2,y)
                self.invaders.append(invader)
            y=y-40

