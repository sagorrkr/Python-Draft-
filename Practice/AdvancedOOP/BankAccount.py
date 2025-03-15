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
            print(f"Deposited {amount} into {self.account_number}. Current balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be more than 0. ")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount} from {self.account_number}. Current balance: ${self.balance:.2f}")
            else:
                print(f"Insufficient funds in {self.account_number}")
        else:
            print("Withdrawal amount must be bigger than 0. ")

class Bank:
    def __init__(self):
        self.accounts =  {}

    def add_account(self, account):
        self.accounts[account.account_number] = account
        print(f"Added account {account.account_number} for {account.account_holder}")

    def display_all_accounts(self):
        if self.accounts:
            print("\nAll accounts:")
            for account_number, account in self.accounts.items():
                print(f"Account Number {account_number}, Holder: {account.account_holder}")
        else:
            print("No accounts in the bank. ")

    def display_all_balances(self):
        if self.accounts:
            print("\nAll account balances: ")
            for account_number, account in self.accounts.items():
                print(f" Account: {account_number} \nBalance: {account.balance:.2f}")

        else:
            print("No account in the bank. ")

if __name__ == "__main__":
    bank = Bank()

    account1 = BankAccount(account_number = 1234, account_holder = "Roy", balance = 1000)
    account2 = BankAccount(account_number = 4567, account_holder = "Rogas", balance = 3000)
    account3 = BankAccount(account_number = 7890, account_holder = "Ridoy", balance = 6969)

    bank.add_account(account1)
    bank.add_account(account2)
    bank.add_account(account3)

    bank.display_all_accounts()

    account1.deposit(3000)
    account2.withdraw(500)
    account3.withdraw(3969)

    bank.display_all_balances()


        

    