students = ["Hermoine", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

Stud_Houses = {
    "Hermoine" : "Gryffindor",
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin"
}

print(Stud_Houses["Hermoine"])
print(Stud_Houses["Draco"])

for stdh in Stud_Houses:
    print(stdh, Stud_Houses[stdh], sep = ",")