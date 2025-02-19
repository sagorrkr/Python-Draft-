#Write a program to print the multiplication table of a given number.

n = int(input("Enter a number to see multiplication table: "))

for i in range(1,11):
    print(f"{n} x {i} = {n*i}")
    i += 1