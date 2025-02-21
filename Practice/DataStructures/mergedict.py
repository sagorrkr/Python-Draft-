#Create a program that merges two dictionaries into one.

def merge_dict(dict1,dict2):
    return{**dict1 , **dict2}

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"d": 4, "e": 5, "f": 6}

result = merge_dict(dict1, dict2)

print(result)
