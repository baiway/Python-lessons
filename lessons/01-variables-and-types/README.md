# Lesson 1: Variables, data types and user input
In this lesson we'll learn how to store values in variables, do arithmetic, print nicely-formatted output using f-strings, and get input from the user.

## Variables
We can use the assignment operator `=` to store values in variables. For example:
```python
>>> x = 3
>>> y = x**2 + 3*x - 9
>>> print(x)
3
>>> print(y)
9
```

Note that `=` in Python does _not_ mean "equals" in the maths sense. It means "store the value on the right in the variable on the left". This means the following is perfectly valid Python, even though it's nonsense in maths:
```python
>>> x = 3
>>> x = x + 1
>>> print(x)
4
```

Variable names can contain letters, numbers and underscores, but they can't start with a number and they can't contain spaces. By convention, we write Python variable names in `snake_case` (all lowercase, with underscores between words), e.g. `side_length` rather than `SideLength` or `sidelength`. Choose names that describe what the variable stores -- `area` is much better than `a`!

## Arithmetic
Python supports all the arithmetic operators you'd expect, plus a couple you might not have seen before.

| Operator | Meaning                              | Example  | Result |
|----------|--------------------------------------|----------|--------|
| `+`      | Addition                             | `7 + 2`  | `9`    |
| `-`      | Subtraction                          | `7 - 2`  | `5`    |
| `*`      | Multiplication                       | `7 * 2`  | `14`   |
| `/`      | Division                             | `7 / 2`  | `3.5`  |
| `//`     | Integer division (rounds down)       | `7 // 2` | `3`    |
| `%`      | Modulo (remainder after division)    | `7 % 2`  | `1`    |
| `**`     | Exponentiation (powers)              | `7 ** 2` | `49`   |

Python follows the same order of operations (BIDMAS) as you'd use in maths. If in doubt, use brackets!

**Task 1:** Determine the area of a triangle with a base length of 6 cm and a height of 9 cm. Store the lengths as variables `base` and `height` then use the formula `area = 0.5 * base * height` to calculate the area. Print the result to the screen using `print(area)`. [Solution](solutions/task1_triangle_area.py)

**Task 2:** The surface area $s$ of an octahedron with side length $a$ is $s = 2a^2 \sqrt{3}$. Use this formula to determine the surface area of an octahedron with side length 8 cm. Hint: you can use the `math` library to do square roots. To do this, put `import math` at the top of your program, then you can write (for example) `math.sqrt(64)` to calculate $\sqrt{64}$. [Solution](solutions/task2_octahedron.py)

## Data types
Some of the basic data types in Python are listed below. There are more types (for a complete list, click [here](https://docs.python.org/3/library/stdtypes.html)), and it's even possible to define your own (we'll do this in [Lesson 11](../11-classes-and-objects)), but these will be enough for our purposes for some time.

|   Class  |        Basic type      |   Example  |
|----------|------------------------|------------|
| `int`    | Integer numbers        | `42`       |
| `float`  | Floating point numbers | `3.14`     |
| `str`    | Strings and characters | `"cheese"` |
| `bool`   | Boolean values         | `True`     |

It's possible to determine the type of a Python variable using the built-in `type` function. For example,
```python
>>> x = 5
>>> type(x)
<class 'int'>
```

**Task 3:** Use interactive mode to determine the type of each variable below using the `type` function. Before you check each one, try to predict what the answer will be. [Solution](solutions/task3_types.md)
```python
a = 9001
b = "3"
c = False
d = 2.718281828
e = "apple"
f = 10 / 2
```

## Printing with f-strings
We often want to print variables alongside some text. The neatest way to do this in Python is with an _f-string_ (short for "formatted string"). To make an f-string, put the letter `f` just before the opening quotation mark. You can then put any variable (or any Python expression!) inside curly brackets `{}`, and Python will replace it with its value. For example:
```python
name = "Ada"
age = 36
print(f"{name} is {age} years old.")
print(f"Next year, {name} will be {age + 1}.")
```

which prints:
```
Ada is 36 years old.
Next year, Ada will be 37.
```

You can also control how numbers are displayed by adding a _format specifier_ after a colon. The most useful one is `:.Nf`, which rounds a number to `N` decimal places:
```python
>>> import math
>>> print(f"pi is roughly {math.pi:.2f}")
pi is roughly 3.14
>>> print(f"pi is roughly {math.pi:.5f}")
pi is roughly 3.14159
```

We'll learn more format specifiers in [Lesson 7](../07-strings).

> [!NOTE]
> You may see older code that uses `print("Area =", area)` or `print("Area = " + str(area))`. These work, but f-strings are easier to read and harder to get wrong, so I recommend using them wherever you can.

## Getting user input
We can use the `input` function to make our programs interactive. `input` displays a message, waits for the user to type something and press `Enter`, then gives back whatever they typed.

**Task 4:** Save the following code as `fav_fruit.py` then try running it. [Example](examples/fav_fruit.py)
```python
fav_fruit = input("What is your favourite fruit? ")

print(f"The user's favourite fruit is: {fav_fruit}")
```

**Task 5:** Write a program that asks the user to enter the height and base of a triangle, then calculates the area. You will likely run into a `TypeError`. This happens because `input` _always_ gives back a string (`str`), even if the user types a number, and Python doesn't know how to multiply a string by a number. To fix this, you need to explicitly *cast* (convert) the user input to the desired type; for example: [Solution](solutions/task5_triangle_area_input.py)
```python
base = float(input("Enter the base in centimetres: "))
```

> [!NOTE]
> What happens if the user types something that isn't a number, like `banana`? Try it! Python will crash with a `ValueError`. We'll learn how to handle errors like this gracefully in [Lesson 8](../08-exceptions).

**Task 6:** Write a program that calculates the surface areas of octahedra with side lengths of 1 cm, 2 cm, 3 cm and 4 cm. Print each answer to 2 decimal places using an f-string. [Solution](solutions/task6_octahedra.py)

You probably found Task 6 a bit repetitive. Programmers _hate_ repeating themselves, and we'll learn two much better ways of doing this soon: loops (in [Lesson 3](../03-loops)) and functions (in [Lesson 6](../06-functions)).

**Task 7:** Write a program that asks the user for a temperature in degrees Celsius and converts it to degrees Fahrenheit using the formula $F = \frac{9}{5}C + 32$. Print the answer to 1 decimal place. [Solution](solutions/task7_temperature.py)

**Task 8:** Write a program that asks the user for a number of seconds and converts it into minutes and seconds. For example, if the user enters `200`, your program should print `200 seconds is 3 minutes and 20 seconds`. Hint: use `//` and `%`. [Solution](solutions/task8_minutes_and_seconds.py)

**⭐ Task 9:** Write a program that asks the user for an amount of money in pence (e.g. `388`) and works out the smallest number of coins needed to make that amount, using £2, £1, 50p, 20p, 10p, 5p, 2p and 1p coins. For example, 388p is 1 × £2, 1 × £1, 1 × 50p, 1 × 20p, 1 × 10p, 1 × 5p, 1 × 2p and 1 × 1p. Hint: start with the biggest coin and work your way down, using `//` to work out how many of each coin you need and `%` to work out how much is left over. [Solution](solutions/task9_coins.py)

---
[← Previous: Lesson 0](../00-getting-started) | [Contents](../../README.md) | [Next: Lesson 2 →](../02-conditionals)
