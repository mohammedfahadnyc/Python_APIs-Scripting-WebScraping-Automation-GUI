import random
from turtle import Turtle,Screen

screen = Screen()
user_bet = screen.textinput(title="Make a Choice",prompt="Choose the color of your turtle")
screen.title("Welcome to the turtle race!")
screen.setup(width=500,height=400)
is_bet_on = False
colors = ["red","green","blue","yellow","orange","purple"]
turtle_list = []

for i in range (0,6) :
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x=-230,y=0+(i*20))
    turtle_list.append(turtle)

if user_bet :
    is_bet_on = True
writer = Turtle()
writer.penup()
writer.hideturtle()
writer.goto(-100,0)
writer.color("Black")


while is_bet_on :
    for turtle in turtle_list :

        if turtle.xcor() > 230 :
            is_bet_on = False
            winner = turtle.pencolor()
            if winner == user_bet :
                writer.write(f"The winner is {winner}, You've Won",font=("aerial",14,"normal"))
            else :
                writer.write(f"The winner is {winner}, You've Lost",font=("aerial",14,"normal"))
        turtle.forward(random.randint(0,10))



screen.exitonclick()