import turtle

side = 100
angle = 120

for _ in range(12):
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)

    turtle.left(angle)

turtle.exitonclick()
