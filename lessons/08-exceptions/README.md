# Lesson 8: Errors and exceptions
By now, you'll have seen plenty of error messages! In this lesson, we'll learn how to read them, how to write programs that deal with errors gracefully instead of crashing, and how to track down bugs that don't cause any error messages at all.

## Types of error
There are three main types of error you'll come across:
1. **Syntax errors** happen when your code isn't valid Python, e.g. if you forget a colon, a bracket or a quotation mark. Python spots these _before_ it starts running your program, so nothing runs at all.
2. **Runtime errors** happen while your program is running, when Python is asked to do something impossible, like dividing by zero or converting `"banana"` to an `int`. In Python, these are called _exceptions_. Unless you handle them, they crash your program.
3. **Logic errors** happen when your program runs without crashing, but does the wrong thing, e.g. if you type `+` when you meant `-`. Python can't spot these for you. These are usually the hardest errors to find! We'll look at some ways of finding them [at the end of this lesson](#debugging-finding-logic-errors).

In this lesson, we're interested in the second type: exceptions.

## Reading a traceback
When an exception crashes your program, Python prints a _traceback_. For example, if you run [`examples/traceback_example.py`](examples/traceback_example.py) and enter `banana`, you'll see something like:
```
Traceback (most recent call last):
  File "traceback_example.py", line 5, in <module>
    age = get_age()
  File "traceback_example.py", line 2, in get_age
    return int(input("How old are you? "))
ValueError: invalid literal for int() with base 10: 'banana'
```

It's tempting to panic when you see one of these, but they're actually very helpful. Read them from the **bottom up**:
- The last line tells you the _type_ of exception (`ValueError`) and a message describing what went wrong (Python couldn't turn `'banana'` into an `int`).
- The lines above tell you _where_ it went wrong: line 2, inside the function `get_age`, which was called from line 5.

Here are some of the most common exceptions:

| Exception           | When it happens                                           | Example                      |
|---------------------|-----------------------------------------------------------|------------------------------|
| `ValueError`        | A value has the right type, but an unsuitable value       | `int("banana")`              |
| `TypeError`         | An operation is used on the wrong type                    | `"age: " + 15`               |
| `ZeroDivisionError` | Dividing by zero                                          | `5 / 0`                      |
| `IndexError`        | An index is outside the range of a list or string         | `[1, 2, 3][3]`               |
| `NameError`         | Using a variable that hasn't been defined (often a typo!) | `print(scroe)`               |
| `AttributeError`    | Using a method that doesn't exist (often a typo!)         | `"hi".uppper()`              |
| `FileNotFoundError` | Trying to open a file that doesn't exist                  | `open("missing.txt")`        |
| `KeyError`          | Looking up a key that isn't in a dictionary               | (see [Lesson 13](../13-dictionaries-and-sets)) |

**Task 1:** For each line of code below, predict which exception (if any) it will cause. Then check your predictions using interactive mode. [Solution](solutions/task1_predict_exceptions.md)
```python
int("3.5")
float("3.5")
"5" * 3
"5" + 3
[10, 20, 30][-1]
[10, 20, 30][-4]
len(42)
10 // 0
"hello".uppercase()
```

## Handling exceptions with `try` and `except`
To deal with an exception, put the code that might cause it inside a `try` block, and the code that should run if it happens inside an `except` block:
```python
try:
    age = int(input("How old are you? "))
    print(f"Next year, you will be {age + 1}")
except ValueError:
    print("That's not a whole number!")
```

Python runs the code in the `try` block as normal. If an exception happens, Python immediately jumps to the matching `except` block, skipping the rest of the `try` block. If no exception happens, the `except` block is skipped.

Always say _which_ exception you're expecting (`except ValueError:`) rather than just writing `except:`. Otherwise, you'll also catch exceptions you weren't expecting, which can hide bugs in your code.

You can have several `except` blocks to handle different exceptions in different ways. You can also store the exception in a variable using `as`, which is useful if you want to print its message:
```python
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(f"{a} / {b} = {a / b}")
except ValueError:
    print("Please enter whole numbers only.")
except ZeroDivisionError as error:
    print(f"Something went wrong: {error}")
```

A very common pattern is to combine `try`/`except` with a `while True` loop to keep asking the user for input until they give us something valid:
```python
while True:
    try:
        age = int(input("How old are you? "))
        break  # only reached if the line above didn't cause an exception
    except ValueError:
        print("That's not a whole number! Try again.")
```

**Task 2:** Write a function `get_int(prompt)` that keeps asking the user for a whole number until they enter one, then returns it. Use it to ask the user for two numbers, and print their sum. [Solution](solutions/task2_get_int.py)

**Task 3:** Write a program that asks the user for two numbers and divides the first by the second. Your program should print a different, helpful message if the user enters something that isn't a number, or tries to divide by zero. [Solution](solutions/task3_safe_division.py)

**Task 4:** Improve your `get_int_in_range(prompt, low, high)` function from [Lesson 6](../06-functions) Task 5 so that it also copes with input that isn't a whole number. Use it to make your "guess the number" game from [Lesson 3](../03-loops) Task 6 impossible to crash. [Solution](solutions/task4_guess_the_number.py)

**Task 5:** Write a program that shows the user the menu below, numbered from 1, and asks them to choose an item by its number. Print the item they chose. Your program shouldn't crash if the user enters something that isn't a number, or a number that's too big. Make sure you test what happens if they enter `0` or a negative number -- you might be surprised! [Solution](solutions/task5_menu.py)
```python
menu = ["Pizza", "Burger", "Pasta", "Salad", "Soup"]
```

## `else` and `finally`
A `try` statement can also have an `else` block and a `finally` block:
- The `else` block runs only if the `try` block finished _without_ an exception. It's a good place for code that should only run if everything went well, but which you don't want to protect with the `try` (because you're not expecting it to cause an exception).
- The `finally` block runs _no matter what_: whether the `try` block succeeded, an exception was handled by an `except` block, or even if an exception wasn't handled and is about to crash the program.

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number
except ValueError:
    print("That's not a whole number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print(f"100 / {number} = {result}")
finally:
    print("Thanks for using my program!")
```

You can find this example in [`examples/try_except_else_finally.py`](examples/try_except_else_finally.py).

> [!NOTE]
> In practice, you'll use `finally` very rarely. It's designed for "clean-up" code that _must_ run, like closing a file or a network connection, even if something goes wrong. However, Python has a neater way of doing this for files (the `with` statement, which we'll see in [Lesson 9](../09-files)), and in most of the programs you'll write, there's nothing to clean up. It's worth knowing what `finally` does, though, as it does come up in exam questions! `else` is used a bit more often, but is still optional: you can usually get the same effect by putting the code at the end of the `try` block instead.

**Task 6:** Predict what the program in [`examples/try_except_else_finally.py`](examples/try_except_else_finally.py) prints when the user enters each of the following. Then run it to check. [Solution](solutions/task6_trace_output.md)
1. `4`
2. `0`
3. `four`

## Raising exceptions
You can also cause (or _raise_) exceptions yourself using `raise`. This is useful when writing functions: if your function is given a value it can't sensibly deal with, it's better to raise an exception than to return a wrong answer or carry on silently. Whoever called the function can then decide how to handle it.
```python
def calculate_area(width, height):
    """Calculates the area of a rectangle"""
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive")
    return width * height
```

**Task 7:** Write a function `calculate_bmi(mass, height)` that calculates a person's body mass index using the formula $\text{BMI} = \frac{\text{mass}}{\text{height}^2}$, where mass is in kilograms and height is in metres. Your function should raise a `ValueError` with a helpful message if either input is zero or negative. Write a program that asks the user for their mass and height, and uses `try`/`except` to print either their BMI (to 1 decimal place) or the error message. [Solution](solutions/task7_bmi.py)

## Debugging: finding logic errors
Exceptions are annoying, but at least Python tells you that something has gone wrong, and where. Logic errors are harder: your program runs perfectly happily, but gives the wrong answer. Tracking down and fixing errors like these is called _debugging_. There are several techniques that can help.

### Print statements
The simplest technique is to add some extra `print` statements, to show you the values of your variables as your program runs. The `=` trick from [Lesson 7](../07-strings) is perfect for this: `print(f"{i=}, {total=}")` prints something like `i=2, total=6`. Remember to remove these when you've found the problem!

### Trace tables
A _trace table_ is a way of working through a program by hand, line by line, writing down the value of each variable every time it changes. Each column is a variable (or a condition, or the output), and you add a new row whenever something changes. They're a great way of understanding what a piece of code does, and you'll be asked to complete them in exams. For example, here's a trace table for the program below:
```python
total = 0
for i in range(1, 4):
    total = total + i * 2
print(total)
```

| `i` | `total` | Output |
|-----|---------|--------|
|     | 0       |        |
| 1   | 2       |        |
| 2   | 6       |        |
| 3   | 12      |        |
|     |         | 12     |

### Using a debugger
VS Code (and Thonny) have a built-in _debugger_, which lets you pause your program at any line, look at the values of all your variables, and then run your program one line at a time. It's like an automatic trace table!
1. Click just to the left of a line number to set a _breakpoint_ (a red dot will appear). Your program will pause just _before_ it runs that line.
2. Press `F5` (or click the arrow next to the "Run" button and choose "Python Debugger: Debug Python File"). Your program will run until it reaches the breakpoint.
3. While the program is paused, the "Variables" panel on the left shows the current value of every variable. You can also hover your mouse over a variable in your code to see its value.
4. Use the buttons in the toolbar at the top of the screen to carry on:
    - **Step Over** (`F10`) runs the current line, then pauses again on the next line.
    - **Step Into** (`F11`) is like Step Over, but if the current line calls one of your functions, it goes _into_ the function so that you can step through it too.
    - **Continue** (`F5`) runs until the next breakpoint (or until the program finishes).
    - **Stop** (`Shift` + `F5`) stops the program.

(On a Mac, you may need to hold the `fn` key to use the `F` keys.) In Thonny, click the "Debug current script" button (the bug icon) instead of "Run", then use the "Step over" and "Step into" buttons.

> [!TIP]
> If you're really stuck, try explaining your code out loud, one line at a time, to someone else (or to a rubber duck!). This is called _rubber duck debugging_, and it works surprisingly often: you'll usually spot the problem halfway through explaining it.

**Task 8:** Complete a trace table for the program below, with columns for `n`, `n % 2 == 0`, `steps` and the output. Then check your answer using the debugger. [Solution](solutions/task8_trace_table.md)
```python
n = 6
steps = 0
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    steps = steps + 1
print(steps)
```

**Task 9:** [`exercises/buggy_scores.py`](exercises/buggy_scores.py) is supposed to print the mean score, the number of passes (a score of 50 or more is a pass) and the highest score for the list of scores below. The correct answers are a mean of 60.83 (to 2 decimal places), 5 passes, and a highest score of 91. But the program contains three logic errors! Use print statements, a trace table and/or the debugger to find and fix them. [Solution](solutions/task9_fixed_scores.py)
```python
scores = [72, 50, 38, 91, 50, 64]
```

**⭐ Task 10:** The list below contains some data that was typed in by hand, and some of it is invalid. Write a function `mean_of_valid(entries)` that converts each entry to a `float`, skips any that can't be converted, and returns the mean of the valid ones _and_ the number that were skipped. What should your function do if _none_ of the entries are valid? [Solution](solutions/task10_mean_of_valid.py)
```python
entries = ["12", "7.5", "banana", "3", "", "-4", "1O", "8.25"]
```

**⭐ Task 11:** I said earlier that you should never write `except:` on its own. Run the program in [`examples/bare_except.py`](examples/bare_except.py) and try to stop it by pressing `Ctrl` + `c`. What happens, and why? How would you fix it? [Solution](solutions/task11_bare_except.md)

---
[← Previous: Lesson 7](../07-strings) | [Contents](../../README.md) | [Next: Lesson 9 →](../09-files)
