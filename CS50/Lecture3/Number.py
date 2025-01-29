try:
    x = int(input("What's X? "))
except ValueError:
    print("X in not an integer!")
else:
    print(f"X is {x}")