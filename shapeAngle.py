#Quinton Dean
#This program prints how many sides are in a shape using a function

for i in range(0,8):
    sides = eval(input("How many sides is the shape "))

    def interiorAngleOfPolygon(sides):
        totDegree = (sides - 2) * 180
        degree = totDegree / sides
        return degree

    print("The angle of this shape is ", interiorAngleOfPolygon(sides))
