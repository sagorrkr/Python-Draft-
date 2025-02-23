#Write a program to read a text file and count the number of words in it.

def count_words_f(file_path):
    try:
        with open(file_path, "r") as file:

            content = file. read()
            words = content.split()
            word_count = len(words)

            return word_count
        
    except FileNotFoundError:
        return "File not found, Check the file path."
    
file_path =  "/Users/sagor/Desktop/Python-Draft-/Practice/FileAndErrorHandling/sample.txt"    #"sample.text"   
wc = count_words_f(file_path)

print(wc)