import turtle
wn = turtle.Screen()
wn.bgcolor("black")

alex = turtle.Turtle()
alex.pensize(5)
alex.color("yellow")
alex.shape("turtle")
alex.stamp()
alex.speed(0)
alex.hideturtle()

for i in range(4):
    alex.forward(220)
    alex.right(90)


trex = turtle.Turtle()
trex.pensize(2)
trex.color("blue")
trex.speed(0)
trex.hideturtle()


trex.left(60)
trex.left(120)
trex.forward(260)
trex.left(120)
trex.forward(260)
trex.left(120)
trex.forward(260)
trex.left(120)

fex = turtle.Turtle()
fex.pensize(6)
fex.color("green")
fex.speed(0)
fex.hideturtle()


fex.left(145)
fex.left(72)
fex.backward(180)
fex.left(72)
fex.backward(180)
fex.left(72)
fex.backward(180)
fex.left(72)
fex.backward(180)
fex.left(72)
fex.backward(180)


tips = turtle.Turtle()
tips.pensize(2)
tips.color("orange")
tips.speed(100)

for _ in range(36):
    for colors in ["red", "purple", "green", "orange"]:
        tips.pencolor(colors)
        tips.forward(100)
        tips.right(90)
        tips.forward(100)
        tips.right(90)
        tips.forward(100)
        tips.right(90)
        tips.forward(100)
        tips.right(90)

        tips.left(10)

        tips.left(90)
        tips.forward(50)
        tips.left(90)
        tips.forward(50)
        tips.left(90)
        tips.forward(50)
        tips.left(90)
        tips.forward(50)


scir = turtle.Turtle()
scir.color("white")
scir.pensize(1)
scir.speed(100)
scir.hideturtle()

for _ in range(24):
    scir.right(90)
    scir.forward(120)
    scir.right(90)
    scir.forward(120)
    scir.right(90)
    scir.forward(120)
    scir.right(90)
    scir.forward(120)

    scir.left(15)


'''elan = turtle.Turtle()
elan.color("green")
elan.pensize(3)

distance = 100
for _ in range(18):
    elan.forward(distance)
    elan.right(100)'''


wn.exitonclick()
