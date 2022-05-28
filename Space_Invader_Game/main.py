from turtle import Screen,Turtle
from Players import Player
from invaders import Invader
from scoreboard import Scoreboard
import winsound
score=Scoreboard()
import time
count=30
screen= Screen()
screen.title("SPACE INVADERS")
screen.setup(width=600,height=600)
screen.bgpic("space_invaders_background.gif")
move=0.3
# Player----------
# player=Turtle()
# screen.addshape('player.gif')
# screen.tracer(0)
# player.shape('player.gif')
# player.penup()
# player.goto(0,-240)
#--------------bullet--------------------------
bulletstate="ready"
jimmy=Turtle()
jimmy.penup()
jimmy.speed()
jimmy.color("white")
jimmy.shape("square")
jimmy.shapesize(stretch_wid=0.5, stretch_len=0.1)
jimmy.hideturtle()
#------------------------
#----------bullet left-------------
chances=Turtle()
chances.color("white")
chances.penup()
chances.hideturtle()
chances.goto(-240,260)
chances.write(f"Bullet_left: {count}")

#--------------------
player=Player()
def bullet():
    global bulletstate
    global count
    if bulletstate == "ready":
        count=count-1
        winsound.PlaySound("Space Invaders_laser.wav",winsound.SND_ASYNC)
        chances.clear()
        chances.write(f"Bullet_left: {count}")
        bulletstate = "fire"
        jimmy.goto(player.xcor(), player.ycor())
        jimmy.penup()
        jimmy.showturtle()



player.create_player()
invader=Invader()

screen.listen()
screen.onkeypress(player.left,"a")
screen.onkeypress(player.right,"d")
screen.onkeypress(bullet,"space")
is_on=True

while(is_on):

    screen.update()
    for invade in invader.invaders:
        invade.goto(invade.xcor()+move,invade.ycor())
        if invade.xcor()>240:
            move=-0.3

        if invade.xcor()<-240:
            move=0.3
        if jimmy.distance(invade)<10:
            winsound.PlaySound("Space Invaders_explosion.wav", winsound.SND_ASYNC)
            jimmy.goto(1000,1000)
            invader.invaders.remove(invade)
            invade.hideturtle()
            score.increase_score()

    jimmy.goto(jimmy.xcor(), jimmy.ycor() +1)
    if jimmy.ycor()>290:
        jimmy.hideturtle()
        bulletstate="ready"
    playe = player.x_cor()
    if score.score==360 :
        score.win()
        is_on=False
    elif count==0:
        score.lose()
        is_on=False
    # print(playe)






screen.mainloop()