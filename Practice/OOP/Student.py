#Create a Student class with attributes like name, roll_number, and marks. 
#Add a method to calculate the average marks.

class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
    
    def calculate_avg_marks(self):
        if len(self.marks) == 0:
            return 0
        else:
            return sum(self.marks) / len(self.marks)
        
if __name__ == "__main__":
    student1 = Student(
        name = "Roy",
        roll_number = 20240513004,
        marks = [ 97, 86, 91, 90, 97]
    )

print(f"{student1.name}'s average mark : {student1.calculate_avg_marks(): .2f} ")