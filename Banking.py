class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")


class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest


class CurrentAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")


savings_account = SavingsAccount("SA001", 5000, 0.05)
savings_account.deposit(1000)
savings_account.calculate_interest()
savings_account.display_balance()

current_account = CurrentAccount("CA001", 2000, 5000)
current_account.withdraw(3000)
current_account.display_balance()