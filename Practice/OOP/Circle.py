#Write a Circle class with an attribute radius. Add methods to calculate the area and circumference.
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14159 * (self.radius ** 2)
    
    def calculate_circumference(self):
        return 2 * 3.14159 * self.radius
if __name__ == "__main__":
    circle = Circle(radius =5)

    print(f"The area of the circle is : {circle.calculate_area(): .2f}")
    print(f"The circumference of the circle is: {circle.calculate_circumference(): .2f}")