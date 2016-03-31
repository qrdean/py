'''
file name:GraphicsAndPatternLibrary.py
description: This is a graphics library that includes:: circle, rectangle, polygon, and chessboard

@author: Quinton Dean
Date due: October 15,2015
'''
def circle(radius, cx = 0, cy = 0, color = 'black', fill = False, move = True):
    import turtle
    
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
    turtle.hideturtle()
    
    
def rectangle(length, width, x = 0, y = 0, color = 'black', fill = False):
    import turtle
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
    turtle.hideturtle()
    
def polygon(side, numberSides, angle = 0, xstart = 0, ystart = 0, color = 'black', fill = False):
    import turtle
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
    turtle.hideturtle()
    

def chessboard(side, xstart = 0, ystart = 0, color = 'black', background = 'white'):
    import turtle
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

def musicnote(radius, notevalue = 'quarter', size = 5, xstart = 0, ystart =0, color = 'black'):
    import turtle
    turtle.color(color)
    if notevalue == 'quarter':
        turtle.pensize(size)
        circle(radius, xstart, ystart, color, fill = True, move =  True)
        turtle.circle(radius,90)
        turtle.end_fill()
        turtle.forward(radius*5)
        turtle.hideturtle()
        turtle.done()

    if notevalue == 'half':
        turtle.pensize(size)
        circle(radius, xstart, ystart, color, fill = True, move = True)
        turtle.circle(radius,90)
        turtle.forward(radius*5)
        turtle.hideturtle()
        turtle.done()
   
    
    if notevalue == 'eighth':
        turtle.pensize(size)
        circle(radius, xstart, ystart, color, fill = True, move =  True)
        turtle.circle(radius,90)
        turtle.forward(radius*5)
        turtle.penup()
        turtle.goto(xstart,ystart)
        turtle.right(90)
        turtle.forward(radius*5)
        turtle.pendown()
        circle(radius, color, fill = True, move = False)
        turtle.circle(radius,90)
        turtle.end_fill()
        turtle.forward(radius*5)
        turtle.left(90)
        turtle.forward(radius*5)
        turtle.hideturtle()
        turtle.done()
    
    if notevalue == 'sixteenth':
        turtle.pensize(size)
        circle(radius, xstart, ystart, color, fill = True, move = True)
        turtle.circle(radius,90)
        turtle.end_fill()
        turtle.forward(radius*5)
    
        turtle.penup()
        turtle.goto(xstart,ystart)
        turtle.right(90)
        turtle.forward(radius*5)
        turtle.pendown()
        circle(radius, color, fill = True, move = False)
        turtle.circle(radius,90)
        turtle.forward(radius*5)
        turtle.left(90)
        turtle.forward(radius*5)
        turtle.penup()
        turtle.goto(xstart+radius*5,ystart)
        turtle.right(180)
    
        turtle.forward(radius*5)
        turtle.pendown()
        circle(radius, color, fill = True, move = False)
        turtle.circle(radius,90)
        turtle.forward(radius*5)
        turtle.left(90)
        turtle.forward(radius*5)
        turtle.penup()

        turtle.goto(xstart+radius*10,ystart)
        turtle.right(180)
        turtle.forward(radius*5)
        turtle.pendown()
        circle(radius, color, fill = True, move = False)
        turtle.circle(radius,90)
        turtle.forward(radius*5)
        turtle.left(90)
        turtle.forward(radius*5)
        turtle.hideturtle()
        turtle.done()
            
        
        
        
            
    
    
    
    
    
    
    
    
    
    
    
    