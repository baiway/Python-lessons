# Lesson 2: Conditional logic
To write responsive programs, we need to use conditional logic: "_if_ this is true, do this, _otherwise_ do that". In Python, we do this with the keywords `if`, `elif` (short for "else if") and `else`. See the example below.
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

There are a few important things to notice here:
1. Each line beginning with `if`, `elif` or `else` ends with a colon `:`.
2. The code that runs when a condition is true is _indented_ (moved to the right) by four spaces. Python uses indentation to work out which lines belong to which condition, so it really matters! If you've used Scratch, you can think of indented code as the blocks that sit _inside_ an "if" block.
3. Python checks each condition in order, from top to bottom, and only runs the code for the _first_ one that's true. The `else` block runs only if none of the conditions above it were true.
4. You can have as many `elif` blocks as you like (including none at all), and the `else` block is optional.

## Comparison operators
The conditions above use _comparison operators_. These compare two values and give back either `True` or `False` (a `bool`).

| Operator | Meaning                  | Example  | Result  |
|----------|--------------------------|----------|---------|
| `==`     | Equal to                 | `3 == 3` | `True`  |
| `!=`     | Not equal to             | `3 != 3` | `False` |
| `>`      | Greater than             | `5 > 3`  | `True`  |
| `<`      | Less than                | `5 < 3`  | `False` |
| `>=`     | Greater than or equal to | `3 >= 3` | `True`  |
| `<=`     | Less than or equal to    | `4 <= 3` | `False` |

> [!WARNING]
> Be careful not to mix up `=` and `==`. A single `=` _stores_ a value in a variable. A double `==` _compares_ two values.

You don't have to use comparison operators though; you can use any statement that evaluates to either `True` or `False`. For example, you can use the `in` keyword to check whether something appears in a list (we'll learn all about lists in [Lesson 4](../04-lists)):
```python
plastics = ["Regina", "Gretchen", "Karen"]
name = "Cady"

if name not in plastics:
    print("You can't sit with us")
```

**Task 1:** Write a program that asks the user for a whole number, then prints whether that number is odd or even. Hint: what is the remainder (`%`) when you divide an even number by 2? [Solution](solutions/task1_odd_or_even.py)

**Task 2:** Write a program that asks the user for a test score out of 100 and prints their grade using the boundaries below. [Solution](solutions/task2_grades.py)

| Score    | Grade |
|----------|-------|
| 80 -- 100 | A    |
| 70 -- 79  | B    |
| 60 -- 69  | C    |
| 50 -- 59  | D    |
| 0 -- 49   | U    |

## Combining conditions with `and`, `or` and `not`
We can combine several conditions into one using the _logical operators_ `and`, `or` and `not`:
- `a and b` is `True` only if _both_ `a` and `b` are `True`.
- `a or b` is `True` if _at least one_ of `a` and `b` is `True`.
- `not a` is `True` if `a` is `False` (and vice versa).

For example:
```python
age = int(input("How old are you? "))
has_ticket = input("Do you have a ticket? (yes/no) ") == "yes"

if age >= 12 and has_ticket:
    print("Enjoy the film!")
elif not has_ticket:
    print("You need to buy a ticket first.")
else:
    print("Sorry, this film is rated 12.")
```

**Task 3:** A cinema charges £5 for children (under 12) and pensioners (65 or over), and £9 for everyone else. Write a program that asks the user for their age and prints the price of their ticket. Try to use `or` so that you only need one `if` and one `else`. [Solution](solutions/task3_cinema_tickets.py)

**Task 4:** Write a simple Python program that generates two random numbers `num1` and `num2`, asks the user to do something with them (e.g. add them together, or multiply them -- you decide), then checks whether the user got the answer right. Use the starter code in [`exercises/maths_quiz.py`](exercises/maths_quiz.py) (shown below) to start you off -- you need to replace each `...` with some code. [Solution](solutions/task4_maths_quiz.py)
```python
import random

# Get limits from user
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

**Task 5:** A year is a leap year if it is divisible by 4, _except_ for years that are divisible by 100, which are only leap years if they are also divisible by 400. So 2024 and 2000 were leap years, but 1900 was not. Write a program that asks the user for a year and prints whether or not it is a leap year. [Solution](solutions/task5_leap_year.py)

**Task 6:** Write a program that plays rock, paper, scissors against the computer. You can use the snippet below to start you off. If the user types something other than 'rock', 'paper', or 'scissors', your program should tell them off rather than playing the game. [Solution](solutions/task6_rock_paper_scissors.py)
```python
import random

computer_choice = random.choice(["rock", "paper", "scissors"])
user_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()
```

**⭐ Task 7:** Your solution to Task 6 probably has a lot of repeated code (mine certainly does!). Re-write it so that it only has _three_ `print` statements for the result: one for a draw, one for a user win and one for a computer win. Hint: there are only three ways the user can win -- can you combine them into one condition using `and` and `or`? [Solution](solutions/task7_rock_paper_scissors_short.py)

---
[← Previous: Lesson 1](../01-variables-and-types) | [Contents](../../README.md) | [Next: Lesson 3 →](../03-loops)
