'''
Created on Oct 30, 2015

@author: Quinton Dean
MyTurtle.py contains the class MyTurtle with the following methods: circle, rectangle, polygon, chessboard
and writeText. The methods are taken directly from the functions in GraphicsAndPatternLibrary and assigned as
methods to class MyTurtle. The turtle method .setheading(0) was added to the end of each method to correct angle
problems from Assignment 2 so no longer use turtle.done() in main() as a work around.
The functions writeText was added and musicnote was removed. 
'''
import turtle
class MyTurtle():

    def circle(radius, cx = 0, cy = 0, color = 'black', fill = False, move = True):    
        turtle.showturtle()
        if move == True:
            turtle.penup()
            turtle.goto(cx,cy)
            turtle.pendown()
            turtle.color(color)
            if fill == True:
                turtle.begin_fill()
                turtle.circle(radius)
                turtle.end_fill()
            else:
                turtle.circle(radius)
        turtle.setheading(0)
        turtle.hideturtle()
    
    
    def rectangle(length, width, x = 0, y = 0, color = 'black', fill = False):
        turtle.showturtle()
        turtle.penup()
        turtle.goto(x,y)
        turtle.color(color)
        turtle.pendown()
        if fill == True:
            turtle.begin_fill()
            turtle.forward(length)
            turtle.left(90)
            turtle.forward(width)
            turtle.left(90)
            turtle.forward(length)
            turtle.left(90)
            turtle.forward(width)
            turtle.end_fill()
        else:
            turtle.forward(length)
            turtle.left(90)
            turtle.forward(width)
            turtle.left(90)
            turtle.forward(length)
            turtle.left(90)
            turtle.forward(width)
        turtle.setheading(0)
        turtle.hideturtle()
    
    def polygon(side, numberSides, angle = 0, xstart = 0, ystart = 0, color = 'black', fill = False):
        totDegree = (numberSides - 2) * 180
        new = totDegree / numberSides
        degree = 180-new
        turtle.showturtle()
        turtle.penup()
        turtle.goto(xstart, ystart)
        turtle.color(color)
        turtle.pendown()
        turtle.right(angle)
        turtle.forward(side)
        if fill == True:
            turtle.begin_fill()
            for i in range(1,numberSides):
                turtle.left(degree)
                turtle.forward(side)
            turtle.end_fill()
        else:
            for i in range(1,numberSides):
                turtle.left(degree)
                turtle.forward(side)
        turtle.setheading(0)
        turtle.hideturtle()
    

    def chessboard(side, xstart = 0, ystart = 0, color = 'black', background = 'white'):
        turtle.speed(50)
        turtle.showturtle()
        turtle.penup()
        turtle.goto(xstart, ystart)
        turtle.right(45)
        squareSize = side/8
        for i in range(1,9):
            oddoreven = i % 2
            if oddoreven == 1:
                for k in range(0,4):
                
                    turtle.color(color)
                    turtle.begin_fill()
                    turtle.circle(squareSize, steps = 4)
                    turtle.end_fill()
                    turtle.left(45)
                    turtle.forward(squareSize*1.45)
                    turtle.color(background)
                    turtle.begin_fill()
                    turtle.right(45)
                    turtle.circle(squareSize, steps = 4)
                    turtle.end_fill()
                    turtle.left(45)
                    turtle.forward(squareSize*1.45)
                    turtle.right(45)
            else:
                for k in range(0,4):
                
                    turtle.color(background)
                    turtle.begin_fill()
                    turtle.circle(squareSize, steps = 4)
                    turtle.end_fill()
                    turtle.left(45)
                    turtle.forward(squareSize*1.45)
                    turtle.color(color)
                    turtle.begin_fill()
                    turtle.right(45)
                    turtle.circle(squareSize, steps = 4)
                    turtle.end_fill()
                    turtle.left(45)
                    turtle.forward(squareSize*1.45)
                    turtle.right(45)
            turtle.penup()
            turtle.goto(xstart, ystart+squareSize*1.45*i)
            turtle.pendown()
        turtle.penup()
        turtle.goto(xstart,ystart)
        turtle.color('black')
        turtle.pensize(5)
        turtle.pendown()
        turtle.circle(side*1.01, steps = 4)
        turtle.setheading(0)
        
    def writeText(x, y, text, color ='black'):
        turtle.showturtle()
        turtle.color(color)
        turtle.penup()
        turtle.goto(x + .05*abs(x),y + .05*abs(y))
        turtle.pendown()
        turtle.write(text)
        turtle.setheading(0)
        
        
        
