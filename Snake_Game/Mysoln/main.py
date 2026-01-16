from Snake import snake
import time
from turtle import Turtle, Screen

S=Screen()
S.title("SNAKE GAME")
S.setup(width=600,height=600)
S.bgcolor("black")
S.tracer(0)
icon=snake()
run_game=True
S.listen()
S.onkey(key='Left', fun=icon.MoveLeft)
S.onkey(key='Right', fun=icon.MoveRight)
S.onkey(key='Down', fun=icon.MoveDown)
S.onkey(key='Up', fun=icon.MoveUp)
icon.makeBound(600,600)
tex=''
while run_game:
    S.update()
    time.sleep(0.1)
    icon.move()
    if icon.collide():
        S.textinput(f" SCORE = {icon.Score-3}",tex)
        break
S.exitonclick()
