from turtle import Turtle
import random

import gc
flist=[]
color=["red","yellow","orange","green","purple","pink","magenta","brown",]
class fish(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=2)
        self.color(random.choice(color))
        self.teleport(400,-275+50*random.randrange(1,10))
        flist.append(self)

    def __del__(self):
        self.clear()
        self.hideturtle()
        gc.collect()


def move(player):
    for i in flist:
        i.bk(10)
        if(i.distance(player)<=13):
            return True
        if i.xcor()<-390:
            i.hideturtle()
            del flist[flist.index(i)]
            del i
            gc.collect()
    return False