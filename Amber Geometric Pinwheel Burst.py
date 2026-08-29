from turtle import *

speed(0)
bgcolor("black")
color("yellow")
width(1)
tracer(12,0)
hideturtle()

for i in range (720):
    forward(450)
    left(92)
    forward(40)
    left(88)
    forward(150)

    up()
    goto(0, 0)
    left(0.5)
    down()