print("Hello, World!")

print("Hello, \"World\"")

Name = input("What's your name? ")


print("Hello", Name)

Age = int(input("How old are you? "))

print("So, you are going to be", str(Age + 1) ,"next year")

friend1 = "Alex"
friend2 = "Dias"

print(friend1, friend2, sep = " and ", end= " ")
print("are good friends")

name = input("Name again? ")

#formating string
print(f"Hello, {name}")


#ask for their name
name2= input("whats your name? ")

#remove whitespace and capitalize the first letter of each word
name2= name2.strip().title()
print(f"Hello, {name2}")


#spllit users name into first name and last name
first, last = name2.split()
print(f"Hello, {first}")