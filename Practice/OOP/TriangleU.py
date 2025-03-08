#Write a Triangle class with attributes side1, side2, and side3. 
#Add methods to calculate the perimeter and check if it’s a valid triangle.

class Triangle:
    def __init__(self, side1, side2, side3):

        self.side1 = side1
        self.side2 = side2
        self.side3 = side3 

    def perimeter(self):
        return self.side1 + self.side2 + self.side3
    
    def is_valid_triangle(self):
        # A triangle is valid if the sum of any two sides is greater than the third side
        return (self.side1 + self.side2 > self.side3) and \
               (self.side2 + self.side3 > self.side1) and \
               (self.side1 + self.side3 > self.side2)
    

    def displayDetails(self):
        print("\nTriangle Details: ")
        print(f"Side 1: {self.side1}")
        print(f"Side 2: {self.side2}")
        print(f"Side 2: {self.side2}")
        if triangle.is_valid_triangle():
            print("The triangle is valid. ")
            print(f"The perimeter of the triangle is {triangle.perimeter()}")
        else:
            print("This isn't a valid triangle")

def createTriangle():
    print("Enter triangle details: ")
    side1 = float(input("Side1: "))
    side2 = float(input("Side2: "))
    side3 = float(input("Side3: "))
    return Triangle(side1, side2, side3)
        
if __name__ == "__main__":

    triangle = createTriangle()
    triangle.displayDetails()
