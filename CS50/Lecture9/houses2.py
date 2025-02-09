students =  [
    {"name" : "Hermoine", "house": "Gryffinfor"},
    {"name" : "Harry", "house": "Gryffinfor"},
    {"name" : "Ron", "house": "Gryffinfor"},
    {"name" : "Draco", "house": "Slytherine"},
    {"name" : "Padma", "house": "Ravenclaw"},
]

houses = set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)