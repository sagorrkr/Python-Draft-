#Write a program to find common elements between two lists.

def finding_common_element(lst1, lst2):

    common_element = set(lst1).intersection(set(lst2))

    return list(common_element)

#testig the code

list1 = [ 1, 2, 3, 4, 5]
list2 = [ 3, 4, 5, 6, 7]

result = finding_common_element(list1, list2)

print(result)