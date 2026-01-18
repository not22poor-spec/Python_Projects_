from turtle import Turtle
class ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color('blue')
        self.a=1
        self.b=1
        self.start=False
    def move(self):
        if(self.start):
            self.teleport(self.xcor()+self.a,self.ycor()+self.b)
    def reball(self):
        self.start=False
        self.home()
    def start_stop_game(self):
        if(self.start):
            self.start=False
        else:
            self.start=True
