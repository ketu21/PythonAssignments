#Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.
import math

class Circle():
    def __init__(self,r):
        self.radius = r

    def area(self):
        return(math.pi*self.radius*self.radius)

    def perimeter(self):
        return(2*math.pi*self.radius)

obj1 = Circle(2)
obj2 = Circle(5)

print("Area of circle with radius {0} is {1} and perimeter is {2}".format(obj1.radius,obj1.area(),obj1.perimeter()))
print("Area of circle with radius {0} is {1} and perimeter is {2}".format(obj2.radius,obj2.area(),obj2.perimeter()))

