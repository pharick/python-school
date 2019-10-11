import turtle
turtle.shape('turtle')

side = 300
angle = 180 - (180 / 3)

turtle.forward(side)
turtle.left(angle)
turtle.forward(side)
turtle.left(angle)
turtle.forward(side)

turtle.exitonclick()
