def writeTofile(filepath):
    
    userinput = input("Write something to save in the file: ")

    #writting in the file
    with open(filepath, 'w') as file:
        file.write(userinput)

        print("The file saved successfully!")