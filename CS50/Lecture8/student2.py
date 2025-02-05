def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] == "Ravenclaw"
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]   #it returns a list
        #returnig a list because it's immutable

if __name__ == "__main__":
    main()