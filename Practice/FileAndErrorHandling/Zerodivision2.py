#Write a program to handle a ZeroDivisionError when dividing two numbers.

def divide_numbers():
    while True:
        try:
            numerator = float(input("Enter the Numerator: "))
            denominator = float(input("Enter the Denominator: "))
            result = numerator / denominator
            print(f"The result of {numerator} / {denominator} is {result}")
            break
        except ZeroDivisionError:
            print("Error: Diving by Zero is not allowed")
        except ValueError:
            print("Error: Enter a valid numeric value. ")