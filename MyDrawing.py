'''
file name:MyDrawing.py
Description: This program draws a musical note length of user choice:: quarter, half, eighth, or sixteenth
For best results use a radius smaller than 50.

@author: Quinton Dean
Date due: October 15,2015
'''
import turtle
from GraphicsAndPatternLibrary import *
def main():
    circle(50,-50,50,'blue',True,True)
    turtle.done()
    rectangle(100,60,50,50,'green',False)
    turtle.done()
    polygon(60,5,0,-50,0,'red',True)
    turtle.done()
    chessboard(80,-50,-50)
    turtle.done()
    musicnote(40,'quarter',5,-100,-50, 'orange')
    
main()
    