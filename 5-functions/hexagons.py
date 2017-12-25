import turtle

turtle.speed(0)

def drawHexagon():
    turtle.forward(100)
    turtle.left(60)
    turtle.forward(100)
    turtle.left(60)
    turtle.forward(100)
    turtle.left(60)
    turtle.forward(100)
    turtle.left(60)
    turtle.forward(100)
    turtle.left(60)
    turtle.forward(100)
    turtle.left(60)

for _ in range(3):
    drawHexagon()
    turtle.left(120)

turtle.exitonclick()
