#Write a Rectangle class with attributes length and width. Add methods to calculate the area and perimeter.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def Calculate_area(self):
        return self.length * self.width
    
    def Calculate_perimeter(self):
        return 2 * (self.length + self.width)
    
    def Display_Details(self):
        print("\nRectangle Details: ")
        print(f"Length:  {self.length}")
        print(f"Width: {self.width}")
        print(f"Area: {self.Calculate_area()}")
        print(f"Perimeter: {self.Calculate_perimeter()}")

def create_rectangle():
    print("\nEnter the measurement below: ")
    length = float(input("Length: "))
    width = float(input("Width: "))
    return Rectangle(length, width)

if __name__ == "__main__":
    rectangle = create_rectangle()

    rectangle.Display_Details()