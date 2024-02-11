class BankAccount:
    def __init__(self, account_number, account_holder, account_balance):
        self.account_number = account_number
        self.holder = account_holder
        self.balance = account_balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"deposit of {amount} successfully processed. ")
            self.display_balance()
        else:
            print('invalid')

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} successfully processed.")
            self.display_balance()
        else:
            print('not enough money to withdraw')
    def display_balance(self):
        print(f"current balance is: {self.balance}")

account1 = BankAccount('5532', 'Kote', 100000)
account2 = BankAccount('5533', 'luka', 120000)

account1.deposit(500)
account1.withdraw(200)
account2.deposit(1000)
account2.withdraw(800)
