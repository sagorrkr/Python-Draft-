"""def main():
    x = int(input("what's x? "))
    print("X squared is", square(x))

def square(n):
    return n * n # n**2, pow also works

main()
"""

def main():
    result = gender()
    print(result)

def gender():
    gender = input("gender : ").strip().lower()
    
    if gender == 'male':
        return "It's a boy!"
    elif gender == 'female':
        return "It's a girl!"
    else:
        return "It's a hijra"


main()
