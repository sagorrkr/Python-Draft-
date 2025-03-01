#Generating random password by taking the number of digit from user
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password  = ''.join(random.choices(characters, k = length))
    return password

try:
    length = int(input("Enter the length of the password: "))
    if length <= 0:
        print("Password length must be a positive integer.")
    else:
        password = generate_password(length)
        print(f"Generated password: {password}")

except ValueError:
    print("Error: Please enter a valid integer.")

