import turtle
wn = turtle.Screen()
wn.bgcolor("black")

alex = turtle.Turtle()
alex.pensize(1)
alex.color("yellow")
alex.speed(100)
alex.hideturtle()

for i in range(73):
    alex.left(145)
    alex.forward(180)
    alex.left(72)

wn.exitonclick()
