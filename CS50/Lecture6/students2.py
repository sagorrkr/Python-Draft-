with open("students.csv") as file:
    for line in file:
        name , house = line.rstrip().split(",")
        print(f"{name} is in{house}")



#for sorting them alphabetically
students = []

with open("students.csv") as file:
    for line in file:
        name , house = line.rstrip().split(",")
        students.append(f"{name} is in{house}")

for student in sorted(students):
    print(student)