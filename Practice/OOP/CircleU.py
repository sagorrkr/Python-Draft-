#Write a Circle class with an attribute radius. Add methods to calculate the area and circumference.
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)
    def calculate_circumference(self):
        return 2 * math.pi * self.radius

    def display_details(self):
        print("\nHere's the circle details:")
        print(f"Radius : {self.radius}")
        print(f"Area: {self.calculate_area(): .2f} ")
        print(f"Circumference: {self.calculate_circumference(): .2f} ")

def createCircle():
    print("Enter the below info.")
    radius = float(input("Radius: "))
    return Circle(radius)

if __name__ == "__main__":
    circle = createCircle()
    circle.display_details()