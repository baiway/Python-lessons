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

**Task 1:** write a simple Python program that generates two random numbers `num1` and `num2`, asks the user to do something with them (e.g. add them together, or multiply them), then checks whether the user got the answer right. Use the code below to start you off.
```python
import random

# Get get limits from user
print("Please enter the lower and upper limit.")
lower_lim = int(input("Lower limit: "))
upper_lim = ...

# Generate `num1` and `num2`
num1 = random.randint(lower_lim, upper_lim)
num2 = ...

answer = num1 * num2  # feel free to change this to anything you like
user_ans = int(input(f"What is {num1} * {num2}? "))

# Check whether user is correct
if ...:
    print(f"You are correct! The answer is: {answer}")
else:
    print(f"WRONG! The answer is: {answer}")
```

**Task 2:** write some code that plays rock, paper, scissors against the computer. You can use the snippet below to start you off.
```python
import random

computer_choice = random.choice(["rock", "paper", "scissors"])
user_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()
```
