#Create a BankAccount class with attributes account_number and balance. 
#Add methods to deposit and withdraw money.

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New Balance: ${self.balance}")
        else:
            print("The deposite amount invalid!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New Balance: ${self.balance}")
        else: 
            print("Invalid amount or insuffecient balance. ")
    def Display_Details(self):
        print("\nAccount Details: ")
        print(f"Account No: {self.account_number}")
        print(f"Balance: {self.balance}")

    
def create_bankAccount():
    print("Enter account details: ")
    account_number = int(input("Account Number: "))
    balance = float(input("Initial Balance: $"))
    return BankAccount(account_number, balance)

if __name__ == "__main__":

    account = create_bankAccount()
    account.Display_Details()

#testing the code
    account.deposit(5000)
    account.withdraw(4000)

    