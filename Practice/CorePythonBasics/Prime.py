#Write a program to check if a number is prime.

def isprime(n):

    if n <= 1:
        return False
    if n in (2,3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    for i in range(5, int(n**.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        
    return True

if __name__ == "__main__":
    try:
        num = int(input("Enter a number to check if it's a prime number: "))
        print(f"{num} is {'a prime' if isprime(num) else 'not a prime'} number")

    except ValueError:
        print("Enter an integer: ")

