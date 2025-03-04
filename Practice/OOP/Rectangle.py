#Write a Rectangle class with attributes length and width. Add methods to calculate the area and perimeter.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Calculate_area(self):
        return self.length * self.width
    
    def Calculate_perimeter(self):
        return 2 * (self.length + self.width)
    
if __name__ == "__main__":
    ractangle = Rectangle(
        length = float(input("Enter Length: ")),
        width = float(input("Enter Width: "))
    )
print(f"The area of the rectengle is {ractangle.Calculate_area()}")
print(f"The perimeter of the rectengle is {ractangle.Calculate_perimeter()}")
