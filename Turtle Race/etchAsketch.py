from turtle import Turtle,Screen
tim = Turtle()
screen = Screen()

def front () :
    tim.forward(10)
def right () :
    tim.right(10)
def left () :
    tim.left(10)
def back () :
    tim.backward(10)
def clear () :
    tim.reset()

def penup () :
    tim.penup()
def pendown() :
    tim.pendown()

screen.listen()
screen.onkey(key="w",fun=front)
screen.onkey(key="a",fun=right)
screen.onkey(key="d",fun=left)
screen.onkey(key="s",fun=back)
screen.onkey(key="c",fun=clear)
screen.onkey(key="q",fun=penup)
screen.onkey(key="e",fun=pendown)

screen.exitonclick()
