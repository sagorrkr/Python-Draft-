#Create an Employee class with attributes name, employee_id, and salary. 
#Add methods to calculate the yearly salary and give a raise.

class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name 
        self.employee_id = employee_id
        self.salary = salary 
    
    def yearly_salary(self):
        return self.salary * 12
    
    def give_raise(self, raiseAmount):
        if raiseAmount >= 0:
            self.salary += raiseAmount
            print(f"Salary raised ${raiseAmount}. New Salary ${self.salary}")
        else:
            print("Invalid raise amount!")

def createEmployee():
    print("\nEnter Employee details: ")
    name = input("Name: ")
    employee_id = input("ID: ")
    salary = int(input("Current Salary: "))
    return Employee(name, employee_id, salary)

if __name__ == "__main__":

    employee = createEmployee()
    print(f"Yearly Salary of {employee.name} is {employee.yearly_salary()}")
    employee.give_raise(2000)


    
            