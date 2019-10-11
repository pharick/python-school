import turtle, math

side = 80
side2 = math.sqrt(side*side / 2)

turtle.forward(side)
turtle.left(90)
turtle.forward(side)
turtle.left(90)
turtle.forward(side)
turtle.left(90)
turtle.forward(side)

turtle.left(45)

turtle.forward(side2)
turtle.left(90)
turtle.forward(side2*2)
turtle.left(90)
turtle.forward(side2*2)
turtle.left(90)
turtle.forward(side2*2)
turtle.left(90)
turtle.forward(side2)

turtle.exitonclick()
