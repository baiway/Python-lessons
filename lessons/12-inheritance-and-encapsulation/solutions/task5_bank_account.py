class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        """The current balance (read-only: use `deposit` and `withdraw` to change it)"""
        return self._balance

    def deposit(self, amount):
        """Adds `amount` to the balance"""
        if amount <= 0:
            raise ValueError("Deposits must be positive")
        self._balance = self._balance + amount

    def withdraw(self, amount):
        """Takes `amount` away from the balance, if there's enough money"""
        if amount <= 0:
            raise ValueError("Withdrawals must be positive")
        if amount > self._balance:
            raise ValueError(f"Insufficient funds: the balance is only £{self._balance:.2f}")
        self._balance = self._balance - amount

    def __str__(self):
        return f"{self.owner}'s account: £{self._balance:.2f}"


account = BankAccount("Ada")
account.deposit(150)
account.withdraw(29.50)
print(account)
print(f"The balance is £{account.balance:.2f}")

try:
    account.deposit(-10)
except ValueError as error:
    print(f"Error: {error}")

try:
    account.balance = 1_000_000
except AttributeError as error:
    print(f"Error: {error}")

print(account)  # the balance shouldn't have changed
