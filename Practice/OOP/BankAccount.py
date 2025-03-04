#Create a BankAccount class with attributes account_number and balance. 
#Add methods to deposit and withdraw money.

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New Balance ${self.balance}")
        else:
            print("Invalid Deposite amount.Deposite amount must be grreater than 0")
    
    def withdraw(self, amount):
        if  0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New Balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insuffecient balance.")
if __name__ == "__main__":
    account = BankAccount(account_number = 6969, 
                          balance =69000)

#test
    account.deposit(5000)
    account.withdraw(4000)
