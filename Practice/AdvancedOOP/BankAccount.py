#Create a Bank class that manages multiple BankAccount objects. 
#Add methods to display all accounts and their balances.

class BankAccount:
    def __init__(self, account_number, account_holder, balance = 0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into {self.account_number}. Current balance: ${self.balance: .2f}")
        else:
            print("Deposit amount must be more than 0. ")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal {amount} from {self.account_number}. Current balance: ${self.balance: .2f}")
            else:
                print(f"Insufficient funds in {self.account_number}")
        else:
            print("Withdrawal amount must be bigger than 0. ")

class Bank:
    def __init__(self):
        self.accounts =  {}

    def add_accounts(self, account):
        self.accounts[account.account.account_number] = account
        print(f"Added account {account.account_number} for {account.account_holder}")

    def display_all_accounts(self):
        if self.accounts:
            print("\nAll accounts:")
            for account_number, account in self.accounts.items():
                print(f"Account Number {account_number}, Holder: {account.account_holder}")
        else:
            print("No accounts in bank. ")

        

    