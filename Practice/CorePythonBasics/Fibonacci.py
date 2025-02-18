#Write a program to print the Fibonacci sequence up to a given number.

n = int(input("Enter the range of number: "))

a, b = 0, 1

for _ in range(n):
    print(a)
    a, b = b , a+b 