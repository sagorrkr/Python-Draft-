#Write a Person class with attributes name, age, and height. 
#Add methods to grow and celebrate a birthday.

class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    
    def growth(self, height_growth):
        if height_growth > 0:
            self.height += height_growth
            print(f"{self.name} grew {height_growth}cm. New Height: {self.height}cm")
        else:
            print("Growth must be more than 0")

    def celebrateBirthday(self):
        self.age += 1
        print(f"Happy Birthday to {self.name}. You're {self.age} years old now. ")

if __name__ == "__main__":
    person = Person(name = "Abir", age = 22, height = 165)

    person.growth(4)
    person.celebrateBirthday()