class BankAccount:
    all_accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(self.balance)
        return self
    def yield_interest(self):
        self.balance *= self.int_rate
        return self
    @classmethod
    def displayAllBalances(cls):
        for account in cls.all_accounts:
            print(account.balance)

account1 = BankAccount(1.05, 0)
account2 = BankAccount(1.02, 100)

account1.deposit(50).deposit(70).deposit(15).withdraw(12).yield_interest().display_account_info()
account2.deposit(700).deposit(50).withdraw(87.5).withdraw(99).withdraw(140).withdraw(4.5).yield_interest().display_account_info()

BankAccount.displayAllBalances()