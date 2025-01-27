def main():
    x = int(input("What's X? "))

    if isEven(x):
        print("X is Even")
    else:
        print("X is Odd")

def isEven(x):
    #return x % 2 == 0
    #return True if x % 2 == 0 else False
    if x % 2 == 0:
        return True
    else:
        return False
    
main()