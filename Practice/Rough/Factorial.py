number = int(input("Enter an integer: "))

fact = 1

for i in range(1, number + 1):
    fact *= i

print(fact)