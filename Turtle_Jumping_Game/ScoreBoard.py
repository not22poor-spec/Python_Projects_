from turtle import Turtle
class level(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.teleport(0,300)
        self.level=1
        self.color("white")
        self.showlevel()
        self.penup()
    def showlevel(self):
        self.clear()
        self.write(f"level : {self.level}",False,"center",("Arial",35,"normal"))
    def levelpass(self):
        self.level+=1
        self.showlevel()
    def gameover(self):
        self.clear()
        self.home()
        self.color("black")
        self.write(f"___GAME OVER___ Level : {self.level}", False, "center", ("Arial", 35, "normal"))
