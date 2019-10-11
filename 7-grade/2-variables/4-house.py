import turtle, math

cathet = 100
hypo = math.sqrt(cathet*cathet + cathet*cathet)
angle = 180 - (180 - 90) / 2

turtle.forward(cathet)
turtle.left(90)
turtle.forward(cathet)
turtle.left(angle)
turtle.forward(hypo)

turtle.right(angle)
turtle.forward(cathet)
turtle.right(angle)
turtle.forward(hypo)

turtle.left(angle)
turtle.forward(cathet)
turtle.left(90)
turtle.forward(cathet)
turtle.right(120)
turtle.forward(cathet)
turtle.right(120)
turtle.forward(cathet)

turtle.exitonclick()
