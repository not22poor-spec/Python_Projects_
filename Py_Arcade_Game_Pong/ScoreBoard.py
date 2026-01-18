from turtle import Turtle
class score(Turtle):
    def __init__(self,n=1):
        super().__init__()
        self.s=Turtle()
        self.s.color("white")
        self.points=0
        self.position=self.setplayer(n)
        self.s.hideturtle()

        self.showpoint()

    def setplayer(self,n):
        if(n==1):
            self.s.teleport(-40,190)

            return n
        elif(n==2):
            self.s.teleport(40,190)

            return n
        else:
            pass
    def showpoint(self):
        self.s.clear()
        if self.position==1:
            self.s.write(self.points,False,"right",("Arial",70,"bold"))

        elif self.position==2:
            self.s.write(self.points,False,"left",("Arial",70,"bold"))

    def inc_point(self):
        self.points+=1
        self.showpoint()
