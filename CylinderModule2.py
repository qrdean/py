'''
Created on Oct 22, 2015

@author: qtipb
this program shows that self.__radius and self.__height is private
and can't be changed directly. So have to define a set and get function
'''
import math
class Cylinder2:
    def __init__(self, r = 1, h = 1):
        self.__radius = r
        self.__height = h
    
    def getPerimeter(self):
        return self.getRadius()*2*math.pi
    
    def getEndArea(self):
        return self.getRadius()**2*math.pi
    
    def getSideArea(self):
        return self.getHeight()*self.getPerimeter()
    
    def getSurfaceArea(self):
        return self.getSideArea() + 2*self.getEndArea()
    
    def getVolume(self):
        return self.getEndArea()*self.getHeight()
    
    def setRadius(self, r):
        self.__radius = r
    
    def setHeight(self, h):
        self.__height = h
        
    def getRadius(self):
        return self.__radius
    
    def getHeight(self):
        return self.__height
    
    
