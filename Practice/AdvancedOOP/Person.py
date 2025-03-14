#Create a Person class with private attributes name and age. 
#Use getter and setter methods to access and modify these attributes.

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def getName(self):
        return self.__name
    def setName(self, name):
        if isinstance(name, str) and name.strip():
            self.__name = name
        else:
            print("Invalid, Name must be a valid string. ")
    def getAge(self):
        return self.__age
    def setAge(self, age):
        if isinstance(age, int) and age > 0:
            self.__age = age
        else:
            print("Invalid, Age should be a positive int. ")
    def displayDetails(self):
        print(f"Name: {self.__name}, age: {self.__age}")

if __name__ == "__main__":
    person = Person(name = "Tylor", age = 25)
    person.displayDetails()

    print(f"Name: {person.getName()}")
    print(f"Age: {person.getAge()}")

    person.setName("Mike")
    person.setAge(69)
    person.displayDetails()