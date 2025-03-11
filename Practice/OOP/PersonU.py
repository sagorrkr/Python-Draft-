#Write a Person class with attributes name, age, and height. 
#Add methods to grow and celebrate a birthday.

class Person:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def HeightGrow(self, height_):
        if height_ > 0:
            self.height += height_
            print(f"New Height: {self.height}")
        else:
            print("Growth can't be zero or negative.")

    def birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}. You are {self.age} years old now.")

    def display(self):
        print("\nPersons details: ")
        print(f"Name : {self.name}")
        print(f"Age: {self.age}")
        print(f"Current Height: {self.height}")

def createPerson():
    name = input("Name: ")
    age = int(input("age: "))
    height = float(input("Height: "))
    return Person(name, age, height)

if __name__ == "__main__":

    person = createPerson()

    person.HeightGrow(5)
    person.birthday()
    person.display()

