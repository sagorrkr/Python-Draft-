#Write a program to remove duplicates from a list using sets.

def removedup(inputlist):

    seen = set()
    uniqueList = []

    for item in inputlist:
        if item not in seen:
            uniqueList.append(item)
            seen.add(item)

    return uniqueList

#testing the code
inputlist = [1, 2, 3, 5, 6, 5, 4, 2, 7, 5, 9]
result = removedup(inputlist)
print(result)