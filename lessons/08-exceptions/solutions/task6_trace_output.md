# Task 6 solution
1. Entering `4`: no exception happens, so the `else` block runs, followed by the `finally` block.
   ```
   100 / 4 = 25.0
   Thanks for using my program!
   ```
2. Entering `0`: `100 / 0` raises a `ZeroDivisionError`, so the matching `except` block runs, followed by the `finally` block. The `else` block is skipped.
   ```
   You can't divide by zero!
   Thanks for using my program!
   ```
3. Entering `four`: `int("four")` raises a `ValueError`, so the matching `except` block runs, followed by the `finally` block. The `else` block is skipped.
   ```
   That's not a whole number!
   Thanks for using my program!
   ```

Notice that the `finally` block runs every time. In this example, we'd get exactly the same output if we just put `print("Thanks for using my program!")` after the `try` statement, without `finally`. The difference only shows up when an exception _isn't_ handled: try changing `except ZeroDivisionError:` to `except TypeError:` and entering `0`. The program will crash, but it still prints "Thanks for using my program!" first.
