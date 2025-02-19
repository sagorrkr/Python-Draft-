#Write a program to reverse a list without using the built-in reverse() method.

def reverse_list_in_place(lst):
    start = 0
    end = len(lst) - 1

    while start < end:
        # Swap elements at start and end indices
        lst[start] , lst[end] = lst[end], lst[start]
        start += 1
        end -= 1

#testing the code
original = [1, 2, 3, 4, 5]
reverse_list_in_place(original)

print(original)