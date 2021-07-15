import turtle
wn = turtle.Screen()
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("yellow")
t.hideturtle()

for i in range(99):
    for colors in ["red", "purple", "blue", "green", "pink", "orange"]:
        t.pencolor(colors)
        t.width(1)
        t.forward(100)
        t.left(59)
    t.right(5)

wn.exitonclick()
