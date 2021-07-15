import turtle
import random

wn = turtle.Screen()
wn.bgcolor("white")
wn.colormode(255)

alex = turtle.Turtle()
alex.pensize(2)
alex.hideturtle()

alex.speed(0)
c = 0

while True:
    for i in range(3):
        for colors in ["red", "yellow", "green"]:
            alex.pencolor(colors)
            alex.forward(180)
            alex.left(120)
            alex.circle(80)
    alex.right(10)
    c += 1
    if c >= 36:
        break
wn.exitonclick()
