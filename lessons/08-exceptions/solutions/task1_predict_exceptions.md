# Task 1 solution
| Code                   | Result                                                                    |
|------------------------|---------------------------------------------------------------------------|
| `int("3.5")`           | `ValueError`: `int` can only convert strings that look like whole numbers |
| `float("3.5")`         | No exception: gives `3.5`                                                 |
| `"5" * 3`              | No exception: gives `'555'` (the string repeated three times)             |
| `"5" + 3`              | `TypeError`: you can't add a string and an integer                        |
| `[10, 20, 30][-1]`     | No exception: gives `30` (negative indexes count from the end)            |
| `[10, 20, 30][-4]`     | `IndexError`: the list only has three items, so `-3` is as far back as it goes |
| `len(42)`              | `TypeError`: integers don't have a length                                 |
| `10 // 0`              | `ZeroDivisionError`                                                       |
| `"hello".uppercase()`  | `AttributeError`: the method is called `.upper()`, not `.uppercase()`     |
