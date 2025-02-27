#Create a program that reads a file and handles the FileNotFoundError if the file does not exist.

def readFile(Filepath):
    try:
        with open(Filepath, 'r') as file:
            content = file.read()
            print("File content: \n", content)

    except FileNotFoundError:
        print(f"Error: the file {Filepath} doesn't exist. Please check the file path")

Filepath = "Example.txt"

readFile(Filepath)