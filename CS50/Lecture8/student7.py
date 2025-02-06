class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuf", "Ravenclaw", "Slytherine"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student

if __name__ == "__main__":
    main()