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
        
if __name__ == "__main__":

    triangle = Triangle(side1 = 3, side2 = 4, side3 = 5)

    if triangle.is_valid_triangle():
        print("The triangle is valid. ")
        print(f"The perimeter of the triangle is {triangle.perimeter()}")
    else:
        print("This isn't a valid triangle")