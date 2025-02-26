#Write a program to handle a ZeroDivisionError when dividing two numbers.

def divide_number():
    try:
        nemerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the dinominator: "))

        result = nemerator / denominator
        print(f"The result of {nemerator} / {denominator} is {result}")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed. ")

divide_number()