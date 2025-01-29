try:
    x = int(input("What's X? "))
    print(f"x is {x}")
except ValueError:
    print("X in not an integer!")