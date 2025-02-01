students = []

with open("students.csv") as file:
    for line in file:
        name , house = line.rstrip().split(",")
#        student = {}
#        student["name"] = name
#        student["house"] = house
        student = {"name" :  name , "house" : house}
        students.append(student)

#to sort according to different keys, we can create functions as below
def get_name(students):
    return students["name"]       

for student in sorted(students , key = get_name):
    print(f"{student['name']} is in{student['house']}")