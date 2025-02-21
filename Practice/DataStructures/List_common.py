#Write a program to find common elements between two lists.

def common_elem(lst1, lst2):
    return[element for element in lst1 if element in lst2]

list1 = [ 1, 2, 3, 4, 5]
list2 = [ 3, 4, 5, 6, 7]


result = common_elem(list1, list2)

print(result)
