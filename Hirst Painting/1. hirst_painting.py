# random color generator, creating polygons, random walks, generating spirograph

import random
import turtle
from turtle import Turtle,Screen

#extracting colors from an image using colorgram.
# import colorgram
# rgb = []
# colors = colorgram.extract('image.jpg',30)
# for color in colors :
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb.append(new_color)
# print (rgb)

colors = [(202, 164, 110),  (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
turtle.colormode(255)

tim = Turtle()
tim.penup()
x = -160
y = -160
tim.setpos(x,y)
tim.pendown()
tim.hideturtle()

def draw(length) :
    for i in range (length) :
        tim.pendown()
        tim.dot(length,random.choice(colors))
        tim.penup()
        tim.forward(50)

def coordinate():
    tim.penup()
    tim.setpos(x,tim.ycor()+50)

def draw_hirst (length,height):
    for i in range (height):
        draw(length)
        coordinate()

tim.speed("fastest")
draw_hirst(10,10)

screen = Screen()
screen.exitonclick()

#easy approach
# def draw () :
#     timmy.dot(20,random.choice(colors))
#     timmy.penup()
#     timmy.forward(35)
#
# def locator() :
#     ypos = timmy.position()[1]
#     timmy.setposition(xpos,ypos+35)
# n = 10
# for i in range (n) :
#     for i in range(n):
#         draw()
#     locator()