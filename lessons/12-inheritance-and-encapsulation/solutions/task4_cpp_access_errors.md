# Task 4 solution
When the program compiles and runs, it prints:
```
Ada's balance is £157.5
Is the PIN 1234? true
```

Uncommenting each line marked `error` gives the errors below. (These are the messages from `clang`, which is the compiler on macOS. Other compilers, like `g++` on Linux or Windows, word their messages differently, e.g. `'double BankAccount::balance' is protected within this context`, but they mean the same thing.)

1. `pin = 0;` inside `SavingsAccount::add_interest`:
   ```
   bank_account.cpp:44:9: error: 'pin' is a private member of 'BankAccount'
   ```
   `pin` is private, so only `BankAccount` itself can use it. Even though `SavingsAccount` is a subclass of `BankAccount`, it isn't allowed to touch it. (Compare this with `balance`, which is protected, so `add_interest` _can_ use it.)

2. `account.balance = 1000000.0;` inside `main`:
   ```
   bank_account.cpp:59:13: error: 'balance' is a protected member of 'BankAccount'
   ```
   `balance` is protected, so only `BankAccount` and its subclasses can use it. `main` isn't part of either class, so it isn't allowed to.

3. `std::cout << account.pin;` inside `main`:
   ```
   bank_account.cpp:60:26: error: 'pin' is a private member of 'BankAccount'
   ```
   `pin` is private, so `main` certainly isn't allowed to use it!

In each case, the program doesn't compile at all, so it can't run. Compare this with Python, where the equivalent code runs without complaint (see [`examples/bank_account.py`](../examples/bank_account.py)).
