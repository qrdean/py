'''
Created on Oct 21, 2015

@author: qtipb
this program uses the class CylinderModule1
'''
from CylinderModule1 import *

def main():
    bottle = Cylinder1()
        
    bottle.radius = 4
    bottle.height = 8
    print("The radius and height of the bottle are: ", bottle.radius, " and ", bottle.height)
    print("The perimeter of the bottle end circle is", format(bottle.getPerimeter(), '.2f'))
    print("The end circle area of the bottle is ", format(bottle.getEndArea(),'.2f'))
    print("The side area of the bottle is ", format(bottle.getSideArea(), '.2f'))
    print("The total surface of the bottle is ", format(bottle.getSurfaceArea(), '.2f'))
    print("The volume of the bottle is ", format(bottle.getVolume(), '.2f'))

main()   
