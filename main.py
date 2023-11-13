"""This bank account class allows users to do a few commands"""

class bank_account:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account = account_number
        self.bal = balance

    """User deposit"""
    def deposit(self, amount):
        self.bal = self.bal + amount
        return self.bal
    
    """User withdrawal"""
    def withdrawal(self, amount):
        self.bal = self.bal - amount

    """Print how much a user has"""
    def display(self):
        print(f"Your account balance is: {self.bal:02}.")

account = bank_account("Spiderman", "0001", 1000 )
account.deposit(100)
account.withdrawal(200)
account.display()

account2 = bank_account("Gina", "0002", 10)
account2.deposit(3000)