user_input = input("Enter numbers separated by spaces: ")

number_strings = user_input.split()

numbers = []

for num_str in number_strings:
    num = int(num_str)  
    numbers.append(num)  

total = sum(numbers)

print(f"The sum of the numbers is: {total}")
