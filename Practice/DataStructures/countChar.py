#Create a program to count the frequency of each character in a string using a dictionary.
def find_char_frequency(input_str):
    frequency_dict = {}

    for char in input_str:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1

    return frequency_dict

input_str = "Hello World"

result = find_char_frequency(input_str)

print(result)