def main():
    number = int(input("Enter an integer: "))
    isEven(number)

def isEven(number):
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")

if __name__ == "__main__":
    main()



