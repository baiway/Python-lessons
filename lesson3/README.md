# Conditional logic
To write responsive programs, we need to use conditional logic. The general structure of conditional statements in Python is as follows:
```python
x = 5
y = 3

if x > y:
    print("x is greater than y")
elif x == y:
    print("x equals y")
else:
    print("x is smaller than y")
```

You don't have have to use comparison operators like `>` and `==` though; you can use any statement that evaluates to either `True` or `False`. For example:
```python
plastics = ["Regina", "Gretchen", "Karen"]
name = "Cady"

if name not in plastics:
    print("You can't sit with us")
```

**Task 1:** write some code that plays rock, paper, scissors against the computer. You can use the snippet below to start you off.
```python
import random

computer_choice = random.choice(["rock", "paper", "scissors"])
user_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()
```