from turtle import Turtle
class path(Turtle):
    def __init__(self,path_number):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.teleport(-400,-300+path_number*50)
        for i in range(17):
            self.fd(25)
            self.teleport(self.xcor()+25,self.ycor())




