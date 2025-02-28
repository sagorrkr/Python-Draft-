#Write a program to append text to an existing file.
def append_str(filepath):
    try:
        with open (filepath, 'a') as file:
            print("Enter text to append(type'exit' to finish)")
            while True:
                line = input()
                if line.lower() == "exit":
                    break
                file.write(line + '\n')
        print(f"Text appended to {filepath} succesfully!")

    except Exception as e:
        print(f"Error: An error occured: {e}")
#testing the code

filepath = "test2.txt"
append_str(filepath)