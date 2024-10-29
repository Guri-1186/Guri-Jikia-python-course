import turtle
screen = turtle.Screen()
screen.setup(600,600)
t = turtle.Turtle()

t.penup()
t.goto(-250, 0)
t.pendown()
t.forward(500)

t.penup()
t.goto(0, -250)
t.setheading(90)
t.pendown()
t.forward(500)

screen.exitonclick()