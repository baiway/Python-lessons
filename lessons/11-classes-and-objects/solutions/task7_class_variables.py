class BankAccount:
    interest_rate = 0.05  # shared by every account
    num_accounts = 0      # counts how many accounts have been created

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        BankAccount.num_accounts = BankAccount.num_accounts + 1

    def add_interest(self):
        """Adds interest to this account, using the shared interest rate"""
        self.balance = self.balance + self.balance * BankAccount.interest_rate

    def __str__(self):
        return f"{self.owner}'s account: £{self.balance:.2f}"


accounts = [BankAccount("Ada", 100), BankAccount("Alan", 250), BankAccount("Grace")]
print(f"{BankAccount.num_accounts} accounts have been created")

for account in accounts:
    account.add_interest()
    print(account)

# Changing the class variable changes the interest rate for every account
BankAccount.interest_rate = 0.10
print(f"The interest rate is now {BankAccount.interest_rate:.0%}")

for account in accounts:
    account.add_interest()
    print(account)
