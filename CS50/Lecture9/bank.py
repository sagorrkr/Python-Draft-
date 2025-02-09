balance = 0


def main():
    print("Banalce:", balance)
    deposite(100)
    withdraw(50)
    print("Banalce:", balance)


def deposite(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n
    



if __name__ == "__main__":
    main()
