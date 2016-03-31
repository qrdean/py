'''
Created on Oct 31, 2015

@author: Quinton Dean
FurnitureComponents.py contains the following classes: Room, Table, and Sofa.
'''
from MyTurtle import *
'''
CLASS ROOM CONTAINS PERAMETERS:
x and y which tells the location of turtle
l which is the length of the room
w which is the width of the room
n which is the name of the room 'family room', 'game room', etc.
show() calls the rectangle object from the class MyTurtle and displays the Room or Rooms
'''
class Room():
    def __init__(self,x,y,l,w,n):
        self.__x = x
        self.__y = y
        self.__length = l
        self.__width = w
        self.__name = n
        
    def setX(self,x):
        self.__x = x
    
    def setY(self,y):
        self.__y = y
    
    def setLength(self,l):
        self.__length = l
        
    def setWidth(self,w):
        self.__width = w
        
    def setName(self,n):
        self.__name = n
        
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def getLength(self):
        return self.__length
    
    def getWidth(self):
        return self.__width
    
    def getName(self):
        return self.__name
    
    def show(self):
        r1 = MyTurtle.rectangle(Room.getLength(self),Room.getWidth(self), Room.getX(self), Room.getY(self), 'black', False)
        text1 = MyTurtle.writeText(Room.getX(self), Room.getY(self), Room.getName(self), 'black')
        return r1
        return text1

'''
CLASS TABLE CONTAINS THE FOLLOWING PERAMETERS:
x and y which are tells the location of turtle
s is the shape of the table i.e. 4, 6, etc. can only accept values 4,5,6 and 8
l is the side length of the shape if the shape perameter is not 4. If 4 then it is side1 length
w is not specified and is 0 if the shape perameter is not 4. If 4 then it is side2: width
c is the color of the table
show() calls the rectangle object from the class MyTurtle if shape is 4 if not then
calls the polygon object from the class MyTurtle and displays the Table or Tables
'''
class Table():
    def __init__(self,x,y,s,l,w,c):
        self.__x = x
        self.__y = y
        self.__shape = s
        self.__side1 = l
        self.__side2 = w
        self.__color = c
    
    def setX(self,x):
        self.__x = x
    
    def setY(self,y):
        self.__y = y
    
    def setSide1(self,l):
        self.__side1 = l
        
    def setSide2(self,w):
        self.__side2 = w
        
    def setShape(self,s):
        if s == 0:
            self.__shape = s
            return 1
        if s <= 8:
            if s >= 4:
                if s != 7:
                    self.__shape = s
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    
        
        
    def setColor(self,c):
        self.__color = c
      
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def getSide1(self):
        return self.__side1
    
    def getSide2(self):
        return self.__side2
    
    def getShape(self):
        return self.__shape
    
    def getColor(self):
        return self.__color
    
    def show(self):
        if Table.getShape(self) == 4:
            tb1 = MyTurtle.rectangle(Table.getSide1(self), Table.getSide2(self), Table.getX(self), Table.getY(self), Table.getColor(self), True)
        else:
            tb1 = MyTurtle.polygon(Table.getSide1(self), Table.getShape(self), 0, Table.getX(self), Table.getY(self), Table.getColor(self), True)
        return tb1
'''
CLASS SOFA CONTAINS THE FOLLOWING PERAMETERS:
x and y which are tells the location of turtle
l which is the length of the room
w which is the width of the room
c is the color of the Sofa
show() calls the rectangle object from the class MyTurtle and displays the Sofa or Sofas
'''
class Sofa():
    def __init__(self, x,y,l,w,c):
        self.__x = x
        self.__y = y
        self.__length = l
        self.__width = w
        self.__color = c
    
    def setX(self,x):
        self.__x = x
    
    def setY(self,y):
        self.__y = y
    
    def setLength(self,l):
        self.__length = l
        
    def setWidth(self,w):
        self.__width = w
        
    def setColor(self,c):
        self.__color = c
        
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def getLength(self):
        return self.__length
    
    def getWidth(self):
        return self.__width
    
    def getColor(self):
        return self.__color
    
    def show(self):
        s1 = MyTurtle.rectangle(Sofa.getLength(self), Sofa.getWidth(self), Sofa.getX(self), Sofa.getY(self), Sofa.getColor(self), True)
        return s1
    
