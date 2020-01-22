import turtle


def drawPolygon(sides, length):
    for _ in range(sides):
        turtle.forward(length)
        turtle.left(360 / sides)


drawPolygon(30, 30)

turtle.penup()
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(50)
turtle.pendown()

drawPolygon(4, 30)

turtle.penup()
turtle.left(180)
turtle.forward(120)
turtle.right(90)
turtle.forward(30)
turtle.left(90)
turtle.pendown()

drawPolygon(4, 30)

turtle.exitonclick()
