students =  [
    {"name" : "Hermoine", "house": "Gryffinfor"},
    {"name" : "Harry", "house": "Gryffinfor"},
    {"name" : "Ron", "house": "Gryffinfor"},
    {"name" : "Draco", "house": "Slytherine"},
    {"name" : "Padma", "house": "Ravenclaw"},
]

houses =[]
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])

for house in sorted(houses):
    print(house)