#Create a program to count the frequency of each character in a string using a dictionary.

from collections import Counter

def count_char(Input_str):

    return Counter(Input_str)

Input_str = "Hello World"
result = count_char(Input_str)

for char, count in result.items():
    print(f"{char} : {count}")
