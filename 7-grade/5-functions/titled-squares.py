import turtle

turtle.speed(0)

def drawSquare():
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)

for _ in range(36):
    drawSquare()
    turtle.left(10)

turtle.exitonclick()
