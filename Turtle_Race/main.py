from random import choice
from turtle import Turtle, Screen
S=Screen()
S.setup(width=1000,height=600)
color=["red","yellow","blue","green","orange"]
t= []
for i in color:
    x=Turtle()
    x.color(i)
    x.shape("turtle")
    x.speed(1)
    t.append(x)

t[0].teleport(-400,300)
t[0].right(90)
t[0].color("black")
t[0].fd(600)
t[0].teleport(400,300)
t[0].fd(600)
t[0].teleport(0,0)
t[0].color(color[0])
t[0].setheading(0)

for i in range(5):
    t[i].penup()
    t[i].goto(-400,-200+i*100)

guess=S.textinput("WINNER",f"Guess The Winner : {color}")
def movefd(x):
    x.fd(choice([10,20,30]))
while 100 :
    x=choice(t)
    movefd(x)
    if x.xcor()>=400:
        print(guess.lower(),color[t.index(x)])
        if guess.lower()==color[t.index(x)]:
            S.textinput("YOU WIN","enter to continue")
        else :
            S.textinput("YOU lose","enter to continue")

        break

