import turtle
wn = turtle.Screen()
wn.bgcolor("red")

elan = turtle.Turtle()
elan.color("green")
elan.pensize(3)
elan.shape("turtle")


elan.forward(10+10)

'''distance = 300
elan.up()
for _ in range(18):
    elan.stamp()
    elan.forward(distance)
    elan.right(100)'''


wn.exitonclick()
