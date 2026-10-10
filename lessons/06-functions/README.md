# Lesson 6: Functions
Back in [Lesson 1](../01-variables-and-types), you calculated the surface areas of several octahedra by writing out the same formula again and again. That works, but it's tedious, and if you make a mistake in the formula you have to fix it in lots of places. Functions solve this problem: they let us write a piece of code _once_, give it a name, and then use (or _call_) it as many times as we like.

You've already been using functions written by other people: `print`, `input`, `len`, `range` and `random.randint` are all functions. In this lesson, we'll learn how to write our own.

## Defining and calling functions
As an example, the code below calculates the surface area of a sphere using the formula $S = 4 \pi r^2$. We simply need to define the function `sphere_surface_area` once, then we can call it as many times as we want with different inputs.
```python
import math

def sphere_surface_area(radius):
    area = 4 * math.pi * radius**2
    return area

r = 1
s = sphere_surface_area(r)
print(f"The surface area of a sphere of radius {r} cm is {s:.2f} cm^2")

R = 4
S = sphere_surface_area(R)
print(f"The surface area of a sphere of radius {R} cm is {S:.2f} cm^2")
```

Let's break this down:
1. `def` tells Python that we're defining a function, and `sphere_surface_area` is the name of the function. Function names follow the same rules as variable names (so use `snake_case`!).
2. `radius` is a _parameter_. It's a variable that only exists inside the function, and it takes whatever value we pass in when we call the function. When we call `sphere_surface_area(r)`, `radius` takes the value of `r`. The value we pass in is called an _argument_.
3. The indented lines are the _body_ of the function. They don't run when Python reads the `def` line; they only run when the function is called.
4. `return` sends a value back to wherever the function was called from. When Python reaches a `return`, the function stops immediately.

Combined with a loop, this gets even neater:
```python
radii = [1, 2, 3, 4, 5, 6, 7, 8]
for radius in radii:
    surface_area = sphere_surface_area(radius)
    print(f"The surface area of a sphere of radius {radius} cm is {surface_area:.2f} cm^2")
```

You can find this example in [`examples/sphere.py`](examples/sphere.py).

> [!NOTE]
> You may hear functions called _subroutines_, _procedures_ or _methods_. A _subroutine_ is a general name for a named block of code that can be called. Some people use _function_ to mean a subroutine that returns a value, and _procedure_ to mean one that doesn't. In Python, they're all just called functions. (_Methods_ are functions that belong to an object, like `.append`; we'll learn more about these in [Lesson 11](../11-classes-and-objects).)

**Task 1:** Define a function that calculates the surface area of an octahedron with a given side length (as in [Lesson 1](../01-variables-and-types), the formula is $s = 2a^2 \sqrt{3}$). Then use a loop to calculate the surface area of octahedra with side lengths of 1 cm, 2 cm, 3 cm and 4 cm. You should obtain the same answers as in Lesson 1 Task 6. [Solution](solutions/task1_octahedra.py)

## `return` vs `print`
Beginners often mix up `return` and `print`, because both seem to "give you an answer". They are very different though:
- `print` displays a value on the screen. The rest of your program can't use it.
- `return` gives a value back to the code that called the function, which can then store it in a variable, use it in a calculation, pass it to another function, etc.

As a rule of thumb, functions that calculate something should `return` the answer rather than `print` it. That way, whoever calls the function can decide what to do with it. A function that doesn't have a `return` statement gives back the special value `None`.

## Multiple parameters, default values and keyword arguments
Functions can have as many parameters as you like, separated by commas. You can also give parameters a _default value_, which is used if the caller doesn't provide one:
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Ada"))             # prints "Hello, Ada!"
print(greet("Ada", "Welcome"))  # prints "Welcome, Ada!"
```

When you call a function, you can also name the arguments explicitly. These are called _keyword arguments_, and they make it clearer what each argument means. You've already used one of these: `print(item, end=" ")`.
```python
print(greet(greeting="Good morning", name="Alan"))
```

Functions can also return more than one value, separated by commas. You can then store each value in its own variable:
```python
def min_and_max(numbers):
    return min(numbers), max(numbers)

lowest, highest = min_and_max([4, 8, 1, 9])
```

**Task 2:** Write a function `is_even(n)` that _returns_ `True` if `n` is even and `False` otherwise. Use it to print all the even numbers from 1 to 20. [Solution](solutions/task2_is_even.py)

**Task 3:** Write a function `max_of_three(a, b, c)` that returns the largest of three numbers, without using `max`. Test it with a few different inputs, including some where two of the numbers are the same. [Solution](solutions/task3_max_of_three.py)

**Task 4:** Write two functions: `celsius_to_fahrenheit(c)` and `fahrenheit_to_celsius(f)`. Then write a program that asks the user which conversion they'd like to do and which temperature to convert, and prints the answer to 1 decimal place. [Solution](solutions/task4_temperature_converter.py)

## Scope
Variables created inside a function (including its parameters) are _local_ to that function: they only exist while the function is running, and the rest of your program can't see them.
```python
def double(x):
    result = 2 * x
    return result

print(double(5))  # prints 10
print(result)     # NameError: name 'result' is not defined
```

Functions _can_ read variables defined outside of them (called _global_ variables), but it's usually a bad idea to rely on this. A function is much easier to understand, test and re-use if everything it needs is passed in as a parameter, and everything it produces is returned.

## Docstrings
It's good practice to describe what a function does using a _docstring_: a string in triple quotes on the first line of the function. VS Code will show this when you hover over the function's name.
```python
def sphere_surface_area(radius):
    """Calculates the surface area of a sphere with the given radius"""
    return 4 * math.pi * radius**2
```

> [!NOTE]
> You may also see functions written like `def sphere_surface_area(radius: float) -> float:`. The `: float` and `-> float` parts are called _type hints_. They tell the reader (and VS Code) that `radius` should be a `float`, and that the function returns a `float`. Python itself ignores them when running your code. We'll learn more about them in [Lesson 15](../15-type-hints-and-dataclasses).

**Task 5:** Write a function `get_int_in_range(prompt, low, high)` that keeps asking the user to enter a whole number (using `prompt` as the message) until they enter one between `low` and `high` (inclusive), then returns it. Use your function to ask the user for their age (between 0 and 120) and their favourite number (between 1 and 10). [Solution](solutions/task5_get_int_in_range.py)

**Task 6:** Write the following functions, each of which takes a list as a parameter. Test each of them with a few different lists. [Solution](solutions/task6_list_functions.py)
1. `mean(numbers)`: returns the mean of a list of numbers.
2. `linear_search(items, target)`: returns the index of `target` in `items`, or `-1` if it isn't there. (Look back at [Lesson 4](../04-lists) Task 4 if you need a reminder.)
3. `count_above(numbers, threshold)`: returns how many numbers in the list are greater than `threshold`.

**Task 7:** Functions are great for breaking big programs up into small, understandable pieces. Re-write your noughts and crosses game from [Lesson 5](../05-2d-lists) so that it uses the functions below. The main part of your program should then be quite short! The starter code in [`exercises/noughts_and_crosses.py`](exercises/noughts_and_crosses.py) will get you started. [Solution](solutions/task7_noughts_and_crosses.py)
- `print_board(board)`: prints the board.
- `get_move(board, player)`: asks the player for a row and column until they choose an empty square, then returns the row and column.
- `has_won(board, player)`: returns `True` if `player` has three in a row, and `False` otherwise.

**⭐ Task 8:** Write a function `is_prime(n)` that returns `True` if `n` is prime and `False` otherwise. Use it to print the first 20 prime numbers. Can you make your function faster by only checking divisors up to $\sqrt{n}$? Why does this work? [Solution](solutions/task8_is_prime.py)

**⭐ Task 9:** Write a function `roll_dice(num_dice, sides=6)` that simulates rolling `num_dice` dice, each with `sides` sides, and returns the total. Use it to simulate rolling two six-sided dice 10,000 times, and count how many times each total (2 to 12) comes up. Print the results as a simple bar chart, like the one below. Which total is most common, and why? [Solution](solutions/task9_dice_simulation.py)
```
 2:  279 ##
 3:  541 #####
 4:  845 ########
...
```

---
[← Previous: Lesson 5](../05-2d-lists) | [Contents](../../README.md) | [Next: Lesson 7 →](../07-strings)
