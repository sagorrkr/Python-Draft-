class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}" 
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name
            
    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuf", "Ravenclaw", "Slytherine"]:
            raise ValueError("Invalid House")
        self._house = house

def main():
    student = get_student()
    #studenr._house = "Number Four, Privet Drive"    this will break the purpose of the code
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student

if __name__ == "__main__":
    main()
    
    