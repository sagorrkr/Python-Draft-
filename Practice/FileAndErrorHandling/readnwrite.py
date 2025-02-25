#Create a program that writes user input to a file and then reads the file to display the content.

def writeTofile(filepath):
    
    userinput = input("Write something to save in the file: ")

    #writting in the file
    with open(filepath, 'w') as file:
        file.write(userinput)

        print("The file saved successfully!")
def readFromfile(filepath):

    with open(filepath, 'r') as file:
        try:
            content = file.read()
            print(f"content of the file {content}")

        except FileNotFoundError:
            print("File not found, Check the filepath again!")

filepath = "user_input.txt"

writeTofile(filepath)
readFromfile(filepath)