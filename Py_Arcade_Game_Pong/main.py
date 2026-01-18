from turtle import Turtle, Screen
from ScoreBoard import score
from Player import Player
from Ball   import ball
import Keys_press as k
import time
#START/PAUSE/--------p
#STOP/---------------f
Sc=Screen()
game=True
Sc.bgcolor("black")
Sc.screensize(canvwidth=800,canvheight=600)
Sc.tracer(0)
player1=Player(1)
player2=Player(2)
b=ball()
boundry=Turtle()
boundry.color("white")
boundry.hideturtle()
boundry.teleport(-400,300)
boundry.fd(800)
boundry.right(90)
boundry.fd(600)
boundry.right(90)
boundry.fd(800)
boundry.right(90)
boundry.fd(600)
boundry.teleport(0,300)
boundry.setheading(270)
Sc.listen()

def move():
    if k.keys["w"]:
        player1.moveup()
    if k.keys["s"]:
        player1.movedn()
    if k.keys["Up"]:
        player2.moveup()
    if k.keys["Down"]:
        player2.movedn()
def gameoff():
    global game
    game=False

Sc.onkeypress(k.press_w, "w")
Sc.onkeyrelease(k.release_w, "w")

Sc.onkeypress(k.press_s, "s")
Sc.onkeyrelease(k.release_s, "s")

Sc.onkeypress(k.press_up, "Up")
Sc.onkeyrelease(k.release_up, "Up")

Sc.onkeypress(k.press_down, "Down")
Sc.onkeyrelease(k.release_down, "Down")
Sc.onkeypress(gameoff, "f")
Sc.onkeypress(b.start_stop_game, "p")
Sc.update()
for i in range(int(600/26+3)):
    boundry.fd(600/52)
    boundry.penup()
    boundry.fd(600/52)
    boundry.pendown()
Sc.update()
p1_score=score(1)
p2_score=score(2)
speed=1
while game:
    Sc.update()
    time.sleep(0.005/speed)
    if b.xcor()>370 and b.distance(player2)<60:
        b.a=-1
        speed+=1
    if b.xcor() < -370 and b.distance(player1) < 60:
        b.a = +1
        speed+=1
    if(b.xcor()>390):
        b.reball()
        p1_score.inc_point()
        speed=1
    if(b.xcor()<-390):
        b.reball()
        p2_score.inc_point()
        speed=1
    if (b.ycor() > 290):
        b.b = -1
    if (b.ycor() < -290):
        b.b = 1

    b.move()
    move()
Sc.update()


Sc.exitonclick()