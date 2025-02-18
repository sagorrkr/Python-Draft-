#Create a function that takes a list of numbers and returns the largest number.

number = input("Enter numbers separated by space: ").split()

numbers = []

for i in number:
    i = int(i)
    numbers.append(i)

print(max(numbers))