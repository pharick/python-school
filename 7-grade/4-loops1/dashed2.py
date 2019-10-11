import turtle

line = 10
space = 5

for _ in range(10):
    turtle.forward(line)
    turtle.penup()
    turtle.forward(space)
    turtle.pendown()
    line += 5

turtle.exitonclick()
