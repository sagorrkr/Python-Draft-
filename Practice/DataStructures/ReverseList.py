#Write a program to reverse a list without using the built-in reverse() method.

User = list(map(int, input("Enter numbers separated by space: ").split()))
print(User)

print(User[ ::-1])