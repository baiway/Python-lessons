class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Adds `amount` to the balance"""
        self.balance = self.balance + amount

    def withdraw(self, amount):
        """Takes `amount` away from the balance, if there's enough money"""
        if amount > self.balance:
            raise ValueError(f"Insufficient funds: the balance is only £{self.balance:.2f}")
        self.balance = self.balance - amount

    def __str__(self):
        return f"{self.owner}'s account: £{self.balance:.2f}"


account = BankAccount("Ada")
print(account)

account.deposit(150)
account.withdraw(29.50)
print(account)

try:
    account.withdraw(500)
except ValueError as error:
    print(f"Error: {error}")

print(account)  # the balance shouldn't have changed
