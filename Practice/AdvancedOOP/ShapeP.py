#Write a program to demonstrate polymorphism by creating a function 
#that takes a Shape object and calls its area() method.
import math
class Shape:
    def __init__(self):
        print("Calculating the area of a generic shape.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        circle = math.pi * (self.radius ** 2)
        print(f"The area of the circle with radius {self.radius} is {circle}")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        rectangle = self.length * self.width
        print(f"The area of a {self.length} by {self.width} rectangle is : {rectangle: .2f}")

def calculateArea(shape):
    return shape.area()
    
if __name__ == "__main__":
    circle = Circle( radius = 5)
    rectangle = Rectangle(length = 5, width = 4)

    calculateArea(circle)
    calculateArea(rectangle)