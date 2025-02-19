#Write a program to reverse a list without using the built-in reverse() method.
#Creating a New Reversed List (Preserves Original)

def reverse_new_list(lst):

    reversed_list = []

    # Iterate backward and append elements to the new list
    for i in range(len(lst)-1,-1,-1):
        reversed_list.append(lst[i])
    return reversed_list

#testing the code

original = [1 ,2, 3, 4, 5]
result = reverse_new_list(original)

print("The original list: ", original)
print("Reversed list: ", result)

