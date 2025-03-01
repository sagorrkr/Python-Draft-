#Create a program to calculate the area of a circle using the math module.
import math

def AreaCircle(radius):
    area = math.pi * (radius ** 2)
    return area

try: 
    radius = int(input("Enter the radius of the circle: "))
    if radius <= 0:
        print("Radius can't be negative.")
    else:
        circle = AreaCircle(radius)
        print(f"The are of the circle is {circle}")
except ValueError:
    print("Error: Valid valie: int Only")