import turtle

def drawPolygon(sides, length):
    for _ in range(sides):
        turtle.forward(length)
        turtle.left(360 / sides)

drawPolygon(50, 1)
