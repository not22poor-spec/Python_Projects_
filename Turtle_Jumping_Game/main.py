from turtle import Turtle,Screen
from fish_path import path
from fish import fish,move
from player import player
from ScoreBoard import level
import random
import time
import gc
p1=player()
lvl=level()
game_on=True
pau=False
def gameoff():
    global game_on
    game_on=False
def pause(player=None):
    global pau
    if pau:
        pau=False
        p1.m=False
    else:
        pau=True
        p1.m=True
Sc=Screen()
Sc.tracer(0)
Sc.bgcolor("navy blue")
paths=[]
for i in range(10):
    p=path(i+1)
    paths.append(p)
flist=[]
Sc.update()

Sc.listen()
Sc.onkeypress(p1.jumpfd,"w")
Sc.onkeypress(p1.jumpright,"d")
Sc.onkeypress(p1.jumpleft,"a")
Sc.onkeypress(pause,"p")
Sc.onkeypress(gameoff,"e")
nlist= [4]
speed=1
while game_on:
    time.sleep(0.06/speed)
    Sc.update()
    if p1.ycor()>200:
        pause(p1)
        if(len(nlist)<=5 and lvl.level==len(nlist)*5):
            speed-=2
            x=random.randint(1,10)
            while x in nlist:
                x=random.randint(1,10)
            nlist.append(x)

        if speed*2==lvl.level:
            speed+=1
        lvl.levelpass()
        p1.startpos()
    if pau:
        if move(p1):
            lvl.gameover()
            gameoff()
        sp=random.randint(1,10)
        if(sp in nlist):
            fish()
            gc.collect()

Sc.exitonclick()