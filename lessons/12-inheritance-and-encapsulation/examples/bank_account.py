class BankAccount:
    def __init__(self, owner, balance, pin):
        self.owner = owner       # public
        self._balance = balance  # "protected" (by convention only!)
        self.__pin = pin         # "private" (name mangled, but still accessible)

    def deposit(self, amount):
        if amount <= 0:
            print("Deposits must be positive!")
            return
        self._balance = self._balance + amount

    def get_balance(self):
        return self._balance

    def check_pin(self, attempt):
        return attempt == self.__pin


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, pin, interest_rate):
        super().__init__(owner, balance, pin)
        self._interest_rate = interest_rate

    def add_interest(self):
        self._balance = self._balance + self._balance * self._interest_rate


account = SavingsAccount("Ada", 100.0, 1234, 0.05)
account.deposit(50.0)
account.add_interest()

print(f"{account.owner}'s balance is £{account.get_balance()}")
print(f"Is the PIN 1234? {account.check_pin(1234)}")

# None of these cause an error in Python! The underscores are just a polite
# request not to touch, which Python doesn't enforce.
account._balance = 1_000_000.0
print(f"{account.owner}'s balance is now £{account.get_balance()}")

# `account.__pin` doesn't work, because Python has renamed (or "mangled") the
# attribute to `_BankAccount__pin`. But we can still get at it if we really try!
print(f"The PIN is {account._BankAccount__pin}")
