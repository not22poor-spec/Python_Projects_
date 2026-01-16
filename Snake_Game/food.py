
from turtle import  Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.f = Turtle(shape="circle")
        self.f.color("royal blue")
        self.f.penup()
        self.f.shapesize(0.5,0.5)
        self.f.teleport(random.randint(-29, 29) * 10, random.randint(-29, 29) * 10)
    def refesh(self):
        x=random.randint(-29, 29) * 10
        y=random.randint(-29, 29) * 10
        self.f.teleport(x,y)

    def collide(self,tur):
        if tur.T[0].distance(self.f.pos())<=15:
            return True
        else :
            return False