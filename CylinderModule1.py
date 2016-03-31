'''
Created on Oct 21, 2015

@author: qtipb
this Class file shows that self.radius and self.height are not private
and can be changed
'''
import math
class Cylinder1:
    def __init__(self, r = 1, h = 1):
        self.radius = r
        self.height = h
    
    def getPerimeter(self):
        return self.radius*2*math.pi
    
    def getEndArea(self):
        return self.radius**2*math.pi
    
    def getSideArea(self):
        return self.height*self.getPerimeter()
    
    def getSurfaceArea(self):
        return self.getSideArea() + 2*self.getEndArea()
    
    def getVolume(self):
        return self.getEndArea()*self.height
    
    
