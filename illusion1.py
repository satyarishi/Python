import turtle
wn = turtle.Screen()
wn.bgcolor("black")

alex = turtle.Turtle()
alex.pensize(1)
alex.color("orange")
alex.hideturtle()
alex.speed(0)
c = 0
d = 0


while True:
    for i in range(4):
        alex.forward(80)
        alex.right(90)
    alex.right(5)
    c += 1
    if c >= 390 / 5:
        alex.forward(50)
        c = 0
        d += 1
        if d >= 12:
            break


wn.exitonclick()
