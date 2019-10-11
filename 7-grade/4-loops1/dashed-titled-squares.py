import turtle


def draw_line():
  for _ in range(5):
    turtle.pendown()
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)

def draw_square():
  for _ in range(4):
    draw_line()
    turtle.left(90)


draw_square()
turtle.exitonclick()
