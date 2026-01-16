
from Snake import snake
import time
from turtle import Turtle, Screen
from food import Food
import scoreboard

S=Screen()
S.title("SNAKE GAME")
S.setup(width=700,height=700)
S.bgcolor("black")
f=Food()
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
score=scoreboard.score()
score.ChangeScore(icon.Score-3)
while run_game:
    S.update()
    time.sleep(0.1)
    icon.move()
    if f.collide(icon):
        icon.AddLen()
        score.ChangeScore(icon.Score - 3)
        f.refesh()

    if(icon.T[0].xcor()>290 or icon.T[0].xcor()<-290 or icon.T[0].ycor()>290 or icon.T[0].ycor()<- 290):
        run_game=False
    for i in range(1,icon.Score):
        if(icon.T[0].distance(icon.T[i])==0):
            run_game=False
score.gameover()
S.exitonclick()
