'''
Created on Oct 22, 2015

@author: qtipb
this program uses CylinderModule2
'''
from CylinderModule2 import *

def main():
    bottle = Cylinder2()
        
    bottle.setRadius(2)   #  Note the value is different from the previous test 
    bottle.setHeight(4)
    print("The radius and height of the bottle are: ", bottle.getRadius(), " and ", bottle.getHeight())
    print("The perimeter of the bottle end circle is", format(bottle.getPerimeter(), '.2f'))
    print("The end circle area of the bottle is ", format(bottle.getEndArea(), '.2f'))
    print("The side area of the bottle is ", format(bottle.getSideArea(), '.2f'))
    print("The total surface of the bottle is ", format(bottle.getSurfaceArea(), '.2f'))
    print("The volume of the bottle is ", format(bottle.getVolume(), '.2f'))

main()
