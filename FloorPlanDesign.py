'''
Created on Oct 31, 2015

@author: Quinton Dean
FloorPlanDesign.py contains and runs the main function. Main sets and calls each Class and method from
FurnitureComponents.py to create a model of a room.
'''
import turtle
from FurnitureComponents import *
def main():
    space = Room(-150,-150,300,260, "")
    room1 = Room(-150, 10, 100,100, "bed room")
    room2 = Room(70, -150, 80,80, "game room")
    room3 = Room(80,60, 70,50,"bath room")
    
    table1 = Table(-80, -100, 4, 60, 50, 'red')
    table2 = Table(-90, -40, 6, 25, 0, 'blue')
    
    sofa1 = Sofa(50, 0, 30, 40, 'yellow')
    sofa2 = Sofa(0,-70, 30, 80, 'green')
    
    turtle.showturtle()
    space.show()
    room1.show()
    room2.show()
    room3.show()
    
    table1.show()
    table2.show()
    sofa1.show()
    sofa2.show()
    turtle.done()

    
main()
