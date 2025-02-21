#Write a program to remove duplicates from a list using sets.

def remove_duplicates(lst):

    unique_set = set(lst)

    unique_lst = list(unique_set)

    return unique_lst

lst = [1, 2, 4, 5, 2, 4, 5, 6, 7, 1]

result = remove_duplicates(lst)

print(result)