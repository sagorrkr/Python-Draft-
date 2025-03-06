#Create an Employee class with attributes name, employee_id, and salary. 
#Add methods to calculate the yearly salary and give a raise.

class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def yearly_salary(self):
        print(f"{self.name}'s yearly salary is {self.salary * 12}") 
    
    def Raise(self, raiseAmount):
        if raiseAmount >= 0:
            self.salary += raiseAmount
            print(f"Raise of {raiseAmount} is given to {self.name}. New salary {self.salary}")
        else:
            print("Salary raise can not be a negative number.")

    def DisplayDetails(self):
        print("\nHere's  the Employee Details:")
        print(f"Name: {self.name}")
        print(f"ID: {self.employee_id}")
        print(f"Monthly Salary: {self.salary}")

def create_employee():
    print("Enter the below details: ")
    name = input("Name: ")
    employee_id = int(input("ID: "))
    salary = float(input("Current Salary: "))
    return Employee(name, employee_id, salary)

#testing the code

if __name__ == "__main__":
    employee = create_employee()

#displaying employe details
    employee.DisplayDetails()
    employee.Raise(2000)    
    employee.DisplayDetails()
    employee.yearly_salary()


        
        