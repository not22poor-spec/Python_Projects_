from turtle import Turtle
class player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("lime green")
        self.penup()
        self.setheading(90)
        self.startpos()
        self.m=False
    def jumpfd(self):
        if self.m:
            self.goto(self.xcor(),self.ycor()+50)
    def jumpright(self):
        if self.m:
            self.goto(self.xcor() + 50, self.ycor() )
    def jumpleft(self):
        if self.m:
            self.goto(self.xcor() - 50, self.ycor())
    def startpos(self):
            self.teleport(0, -275)