from operator import truediv
from turtle import Turtle
import random

class snake:
    def __init__(self):
        self.position=[]
        self.T=[]
        self.start_pos()
        self.T[0].shape("triangle")
        self.dir=self.T[0].heading
        self.Score=3
        self.Cpoint=Turtle(shape="circle")
        self.Cpoint.color("royal blue")
        self.Cpoint.penup()
        self.Cpoint.teleport(random.randint(-15,15)*20,random.randint(-15,15)*20)
        self.A=self.Cpoint.pos()


    def start_pos(self):
        for i in range(3):
            t = Turtle(shape= "square")
            t.penup()
            t.teleport(-20 * i, 0)
            self.position.append(t.pos())
            t.color('white')
            self.T.append(t)
    def AddLen(self):
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        t.teleport(self.T[self.Score-1].xcor(), self.T[self.Score-1].ycor())
        self.T.append(t)
        self.position.append(t.pos())
        self.Score+=1


    def MoveUp(self):
        if self.T[0].heading()!=270:
            self.T[0].setheading(90)
    def MoveDown(self):
        if self.T[0].heading()==90:
            pass
        else:
            self.T[0].setheading(270)
    def MoveLeft(self):
        if self.T[0].heading()==0:
            pass
        else:
            self.T[0].setheading(180)
    def MoveRight(self):
        if self.T[0].heading()!=180:
            self.T[0].setheading(0)

    def makeBound(self,x,y):
        self.T[0].teleport(-1*x/2,y/2);
        self.T[0].pendown()
        self.T[0].fd(x)
        self.T[0].right(90)
        self.T[0].fd(y)
        self.T[0].right(90)
        self.T[0].fd(x)
        self.T[0].right(90)
        self.T[0].fd(y)
        self.T[0].penup()
        self.T[0].home()

    def move(self):

        for i in range(self.Score-1, 0, -1):
            x = self.T[i-1].xcor()
            y = self.T[i-1].ycor()
            self.position[i]=self.position[i-1]
            self.T[i].teleport(x, y)
        self.T[0].fd(20)
        self.position[0]=(self.T[0].pos())

        if round(self.T[0].pos()[0]) == round(self.A[0]) and round(self.T[0].pos()[1]) == round(self.A[1]):
            self.AddLen()
            m,n=self.T[0].pos()
            while((m,n) in self.position):
                m=random.randint(-14, 14) * 20
                n=random.randint(-14, 14) * 20

            self.Cpoint.teleport(m,n)
            self.A = self.Cpoint.pos()
    def collide(self):
        point=self.T[0].pos()
        if abs(point[0])>=300 or abs(point[1])>=300:
            return True
        else :
            return False

