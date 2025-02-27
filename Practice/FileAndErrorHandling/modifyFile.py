#Write a program to append text to an existing file.

def appendTOfile(filepath, text):
    try:
        with open(filepath, 'a') as file:
            file.write(text + "\n")
        print(f"The text is successfully added to '{filepath}")
    except Exception as e:
        print(f"Error: An error occured : {e}")
              
filepath = 'test.txt'
text_to_append = "Let's see if we can append this sentense"

appendTOfile(filepath, text_to_append)