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
        return sum(self.marks) / len(self.marks)

    def diaplay_studenetDetails(self):
        print("\n Students details below: \n")
        print(f"Name : {self.name}")
        print(f"Roll: {self.roll_number}")
        print(f"Marks: {self.marks}")
        print(f"Average Marks: {self.calculate_avg_marks(): .2f}")

def create_student():
    print("\nEnter Student Details:")
    name = input("Name: ")
    roll_number = int(input("Roll: "))
    marks = list(map(int, input("Enter marks(Comma separated): ").split(",")))
    return Student(name, roll_number, marks)

if __name__ == "__main__":
    student = create_student()

    student.diaplay_studenetDetails()



