#Generating random password by taking the number of digit from user
import random
import string

def RandomPass(length, use_letters = True, use_digits = True, use_punctuation = True):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation
    if not characters:
        print("Error: No characters set is selected")
    password = ''.join(random.choices(characters, k = length))
    return password
    
try:
    length = int(input("Enter the length of the password: "))
    if length <= 0:
        print("Passeord length must be a positive integer.")

    else:
        use_letters = input("Include letters(y/n)").lower() == 'y'
        use_digits = input("Include digits(y/n)").lower() == 'y'
        use_punctuation = input("Include punctuations(y/n)").lower() == 'y'

        password = RandomPass(length, use_letters, use_digits, use_punctuation)
        print(f"Generated Password: {password}")

except ValueError:
    print("Invalid input. Please enter a valid integer.")


