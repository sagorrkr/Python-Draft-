students = ["Hermoine", "Harry", "Ron"]

print(students[0])
print(students[1]) # 0 indexed 
print(students[2])

for student in students:
    print(student)

for i in range(len(students)):
    print(i + 1, students[i])