#Create a program that reads a file and handles the FileNotFoundError if the file does not exist.

def readfile():
    filepath = input("Enter a file path: ")

    try:
        with open(filepath, 'r') as file:
            content = file.read()
            print("File content: \n", content)
    except FileNotFoundError:
        print(f"Error: The file {filepath} doesn't exist. check your filepath again. ")

readfile()