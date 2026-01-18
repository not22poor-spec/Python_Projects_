from turtle import Turtle
class Player(Turtle):
    def __init__(self,i=1):
        super().__init__()
        self.shape('square')
        self.color("white")
        self.shapesize(stretch_len= 5,stretch_wid=0.5)
        self.setheading(90)
        self.penup()
        self.tpp(i)
    def tpp(self,n):
        if(n==2):
            self.teleport(380, 0)
        else:
            self.teleport(-380, 0)

    def moveup(self):
        if self.ycor()>245:
            pass
        else:
            self.fd(2)
    def movedn(self):
        if self.ycor() < -245:
            pass
        else:
            self.bk(2)
