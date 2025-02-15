name = input("What's your name? ")

print(f"Hello, {name}")

number = int(input("What's your average mark this semester? "))

if 90 <= number <= 100:
    print("You've got A+")
elif 80 <= number <= 89:
    print("You've got an A")
elif 70 <= number <= 79:
    print("You've got a B")
elif 60 <= number <= 69:
    print("You've got a C")
else:
    print("You have failed. Keep trying!")
