import turtle


def drawPolygon(sides, length):
    for _ in range(sides):
        turtle.forward(length)
        turtle.left(360 / sides)


def titledPolygon(sides, length, angle, number):
    for _ in range(number):
        drawPolygon(sides, length)
        turtle.right(angle)

turtle.speed(0)
titledPolygon(3, 100, -1, 100)
