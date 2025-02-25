#Writing on a local file

def writingOnfile(filepath):
    userInput = input("Enter some text to save in the file: ")

    with open(filepath, 'a') as file:
        file.write(userInput + '\n')

    print("Text saved successfully!")
filepath = "user_input.txt"
content = writingOnfile(filepath)


