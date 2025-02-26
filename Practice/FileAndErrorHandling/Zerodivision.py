#Write a program to handle a ZeroDivisionError when dividing two numbers.

def divide_number():
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the dinominator: "))

        result = numerator / denominator
        print(f"The result of {numerator} / {denominator} is {result}")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed. ")
    except ValueError:
        print("Error. Please Enter valid numeric value: ")
    

divide_number()