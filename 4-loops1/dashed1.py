import turtle

line = 10
space = 5

for _ in range(20):
    turtle.forward(line)
    turtle.penup()
    turtle.forward(space)
    turtle.pendown()

turtle.exitonclick()
