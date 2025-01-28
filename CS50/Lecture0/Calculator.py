def main():
    x = int(input("what's x? "))
    print("X squared is", square(x))

def square(n):
    return n * n # n**2, pow also works

main()