#pip install mypy

def meow(n: int):
    for _ in range(n):
        print("meow")

number: int = int(input("Number: "))
meow(number)


#mypy meows2.py