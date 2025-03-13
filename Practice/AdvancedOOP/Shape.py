#Write a program to demonstrate method overriding by creating a Shape class with a method area(). 
#Override this method in Circle and Rectangle classes

import math
class Shape():
    def area(self):
        print("Calculating area of a generic shape.")
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        area = math.pi * (self.radius ** 2)
        print(f"The area of a circle with radius {self.radius} is : {area: .2f}")
        return area

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width 
        print(f"The area of a {self.length} by {self.width} rectangle; {area: .2f}")
        return area

if __name__ == "__main__":
    shape = Shape()
    shape.area()

    rectangle = Rectangle( length = 5, width = 4)
    rectangle.area()
    circle = Circle(radius = 5)
    circle.area()
