#Quinton Dean
#This program prints the olympic rings using Turtle

import turtle

r = int(input("enter radius for circle "))
print(r);
xSpace = r*.25
ySpace = r*1.2

turtle.showturtle()
turtle.pensize(6)

turtle.color("blue")
turtle.penup()
turtle.goto(-2*r-xSpace, -r)
x = -2*r-xSpace
y = -.5*r
print(x, y)
turtle.pendown()
turtle.circle(r)

turtle.color("black")
turtle.penup()
turtle.goto(0,-r)
x = 0
y = -.5*r
print(x, y)
turtle.pendown()
turtle.circle(r)

turtle.color("red")
turtle.penup()
turtle.goto(2*r+xSpace, -r)
x = 2*r+xSpace
y = -.5*r
print(x,y)
turtle.pendown()
turtle.circle(r)

turtle.color("yellow")
turtle.penup()
turtle.goto(-r-xSpace, -r-ySpace)
x = -r-xSpace
y = -.5*r-ySpace
print(x,y)
turtle.pendown()
turtle.circle(r)

turtle.color("green")
turtle.penup()
turtle.goto(r+xSpace, -r-ySpace)
x = r+xSpace
y = (-.5*r-ySpace)
print(x,y)
turtle.pendown()
turtle.circle(r)

turtle.hideturtle()
turtle.done()


