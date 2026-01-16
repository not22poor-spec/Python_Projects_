
from turtle import Turtle
class score(Turtle):
    def __init__(self):
        super().__init__()
        self.s=Turtle()
        self.s.teleport(0,310)
        self.s.color('white')
        self.s.hideturtle()
    def ChangeScore(self,score):
        self.s.clear()
        self.s.write(arg=f"SCORE : {score}",move=False,align="center",font=("Arial",14,"normal"))
    def gameover(self):
        self.s.teleport(0,0)
        self.s.color=('yellow')
        self.s.write(arg="GAME OVER",move=False,align="center",font=("Arial",28,"normal"))
