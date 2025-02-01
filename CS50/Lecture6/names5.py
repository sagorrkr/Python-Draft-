with open("names.txt", "r") as file:
    for line in file:
        print("Hello", line.rstrip())


names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):   # to reverse, for name in sorted(names, reverse = True):
    print(f"Hello, {name}")
