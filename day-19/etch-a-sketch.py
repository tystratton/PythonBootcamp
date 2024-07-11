from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def forward():
    turtle.forward(10)

def backward():
    turtle.forward(-10)

def clockwise():
    turtle.right(10)

def counterclockwise():
    turtle.left(10)

def clear():
    turtle.penup()
    turtle.clear()
    turtle.home()
    turtle.pendown()

screen.listen()
screen.onkey(key="w", fun=forward) 
screen.onkey(key="s", fun=backward) 
screen.onkey(key="a", fun=counterclockwise) 
screen.onkey(key="d", fun=clockwise) 
screen.onkey(key="c", fun=clear)

screen.exitonclick()