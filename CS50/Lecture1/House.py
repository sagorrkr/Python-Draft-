name = input("What's your name?" )

match name: 
    case "Harry" | "Hermoine" | "Ron":
        print("Grayffindor")
    case "Draco":
        print("Slytherine")
    case _:
        print("Who?")


#below code also does the same job
'''if name == "Harry":
    print("Grayffindor")
elif name == "Hermione":
    print("Grayffindor")
elif name == "Ron":
    print("Grayffindor")
elif name == "Draco":
    print("Slaytherin")
else:
    print("Who?")'''