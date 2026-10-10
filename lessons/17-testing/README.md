# Lesson 17: Testing your code with `pytest`
How do you know that your code works? So far, we've tested our programs by running them, typing in some input, and checking the output by eye. That's fine for small programs, but it gets tedious (and easy to get wrong) as programs get bigger. Worse, every time you change something, you have to test _everything_ again, in case you've broken something that used to work.

The solution is to write _automated tests_: small pieces of code that check that your code gives the right answers. Once you've written them, you can run all of them in a fraction of a second, as often as you like. Professional programmers write lots of tests, and in this lesson, we'll learn how to write them using the most popular testing tool for Python, `pytest`.

## `assert`
Before we get to `pytest`, let's look at Python's built-in `assert` statement. `assert` checks that something is `True`. If it is, nothing happens; if it isn't, Python raises an `AssertionError`:
```python
>>> assert 1 + 1 == 2
>>> assert 1 + 1 == 3
AssertionError
```

This gives us a simple way of checking our functions:
```python
assert celsius_to_fahrenheit(0) == 32
assert celsius_to_fahrenheit(100) == 212
```

If these lines run without an error, the function gave the right answers. But if one of them fails, the program stops straight away, so we don't find out whether any of the other checks would have passed. And it doesn't tell us much about what went wrong. This is where `pytest` comes in.

## Installing `pytest`
`pytest` is a third-party package, so you'll need to install it first, using any of the methods from [Lesson 14](../14-packages). For example, with your virtual environment activated:
```sh
pip install pytest
```

or, in a `uv` project:
```sh
uv add --dev pytest
```

As we saw in [Lesson 15](../15-type-hints-and-dataclasses), `--dev` adds `pytest` to the `dev` dependency group, for packages that you need while _developing_ your code. (If you've cloned this repository, `pytest` is already in its `dev` group, so you don't need to install anything.)

## Writing tests with `pytest`
`pytest` looks for tests in files whose names start with `test_`, and in functions whose names start with `test_`. Each test function should check one thing using `assert`. Usually, the code being tested lives in one file (a module, as in [Lesson 14](../14-packages)), and its tests live in another. For example, [`examples/temperature.py`](examples/temperature.py) contains:
```python
def celsius_to_fahrenheit(c):
    """Converts a temperature from degrees Celsius to degrees Fahrenheit"""
    return 9/5 * c + 32


def fahrenheit_to_celsius(f):
    """Converts a temperature from degrees Fahrenheit to degrees Celsius"""
    return 5/9 * (f - 32)
```

and [`examples/test_temperature.py`](examples/test_temperature.py) tests it:
```python
from temperature import celsius_to_fahrenheit, fahrenheit_to_celsius


def test_freezing_point():
    assert celsius_to_fahrenheit(0) == 32


def test_boiling_point():
    assert celsius_to_fahrenheit(100) == 212


def test_minus_forty():
    # -40 is the same in both scales!
    assert celsius_to_fahrenheit(-40) == -40
    assert fahrenheit_to_celsius(-40) == -40


def test_round_trip():
    assert fahrenheit_to_celsius(celsius_to_fahrenheit(37)) == 37
```

To run the tests, open a terminal in the folder containing both files and run `pytest` (or `uv run pytest`). `pytest` finds all the test files and test functions by itself, runs them, and gives you a report:
```
============================= test session starts ==============================
collected 4 items

test_temperature.py ...F                                                 [100%]

=================================== FAILURES ===================================
_______________________________ test_round_trip ________________________________

    def test_round_trip():
>       assert fahrenheit_to_celsius(celsius_to_fahrenheit(37)) == 37
E       assert 37.00000000000001 == 37
E        +  where 37.00000000000001 = fahrenheit_to_celsius(98.60000000000001)
E        +    where 98.60000000000001 = celsius_to_fahrenheit(37)

test_temperature.py:19: AssertionError
=========================== short test summary info ============================
FAILED test_temperature.py::test_round_trip - assert 37.00000000000001 == 37
========================= 1 failed, 3 passed in 0.01s ==========================
```

Each `.` is a test that passed, and each `F` is a test that failed. For each failure, `pytest` shows you exactly which `assert` failed, and the values involved. Here, the problem is that converting 37 °C to Fahrenheit and back again gives `37.00000000000001`, not `37`!

## Comparing floats
This isn't really a bug in our code. Computers store floats in binary, and most decimal numbers can't be stored exactly in binary (in the same way that $\frac{1}{3}$ can't be written exactly as a decimal), so calculations with floats often have tiny rounding errors. Try `0.1 + 0.2 == 0.3` in interactive mode!

This means that you should almost never use `==` to compare floats. Instead, check whether they're _approximately_ equal. `pytest` has a helper for this, called `pytest.approx`:
```python
import pytest

def test_round_trip():
    assert fahrenheit_to_celsius(celsius_to_fahrenheit(37)) == pytest.approx(37)
```

With this change, all four tests pass:
```
test_temperature.py ....                                                 [100%]
============================== 4 passed in 0.01s ===============================
```

(This is the version you'll find in [`examples/test_temperature.py`](examples/test_temperature.py).)

**Task 1:** [`examples/leap_year.py`](examples/leap_year.py) contains a function that's supposed to check whether a year is a leap year (see [Lesson 2](../02-conditionals) Task 5), and [`examples/test_leap_year.py`](examples/test_leap_year.py) contains some tests for it. Run the tests. Which test fails, and why? Fix the bug, and run the tests again to check that they all pass. [Solution](solutions/leap_year.py)

## Choosing good tests
A good set of tests checks more than just one or two "normal" inputs. When choosing test data, it's useful to think about three kinds of data:
- **Normal data:** typical inputs that the code should handle without any problems. For example, a score of `65` for a function that turns test scores out of 100 into grades.
- **Boundary data** (or _extreme_ data): inputs at the edges of what's allowed, or on either side of a boundary where the behaviour changes. For example, scores of `0` and `100`, and `69` and `70` if 70 is the boundary between two grades. Lots of bugs (like using `>` instead of `>=`) only show up at the boundaries!
- **Erroneous data** (or _invalid_ data): inputs that shouldn't be accepted, like a score of `-5` or `"banana"`. The code should deal with these sensibly, e.g. by raising an exception.

Remember to think about empty lists, empty strings, zero and negative numbers too: these are very common sources of bugs.

**Task 2:** [`exercises/functions.py`](exercises/functions.py) contains three functions from [Lesson 6](../06-functions): `is_even`, `max_of_three` and `mean`. Create a file called `test_functions.py`, and write tests for each function, using normal and boundary data. What _should_ happen if you call `mean` with an empty list? [Solution](solutions/test_functions.py)

## Testing exceptions
If a function is supposed to raise an exception for erroneous data, we should test that too. `pytest.raises` checks that the code inside a `with` block raises a particular exception (and the test fails if it _doesn't_):
```python
import pytest

def test_mean_of_empty_list():
    with pytest.raises(ZeroDivisionError):
        mean([])
```

You can also check the exception's message, using `match`:
```python
def test_negative_mass():
    with pytest.raises(ValueError, match="Mass must be greater than zero"):
        calculate_bmi(-70, 1.75)
```

**Task 3:** [`exercises/bmi.py`](exercises/bmi.py) contains the `calculate_bmi` function from [Lesson 8](../08-exceptions) Task 7. Write tests that check it gives the right answer for some normal data (use `pytest.approx`!), and that it raises a `ValueError` with the right message for zero and negative masses and heights. [Solution](solutions/test_bmi.py)

## Running the same test with different data
It's common to want to run the same test with lots of different inputs. Rather than writing lots of almost identical test functions, you can use `@pytest.mark.parametrize`. You give it the names of the parameters, and a list of values for them, and `pytest` runs the test once for each set of values:
```python
@pytest.mark.parametrize("score, grade", [
    (100, "A"),
    (80, "A"),
    (79, "B"),
    (50, "D"),
    (49, "U"),
    (0, "U"),
])
def test_grade(score, grade):
    assert get_grade(score) == grade
```

Each set of values counts as a separate test, so if one fails, you can see exactly which one it was.

**Task 4:** [`exercises/caesar.py`](exercises/caesar.py) contains the Caesar cipher functions from [Lesson 7](../07-strings) Task 6. Use `@pytest.mark.parametrize` to test `caesar_encrypt` on at least five different messages and shifts. Make sure you include some boundary data (what happens at the end of the alphabet?), and messages with capital letters, spaces and punctuation. Then write a parametrised test that checks that decrypting an encrypted message always gives back the original message. [Solution](solutions/test_caesar.py)

## Test-driven development
Some programmers write their tests _before_ they write their code! This is called _test-driven development_ (TDD), and it works in a cycle:
1. **Red:** write a test for something your code doesn't do yet. Run it, and check that it fails.
2. **Green:** write the simplest code that makes the test pass.
3. **Refactor:** tidy up your code, running the tests again to make sure you haven't broken anything.

Then repeat, one small piece at a time. Writing the tests first forces you to think carefully about exactly what your code should do (including the boundary and erroneous cases) before you start, and means you always have a full set of tests when you've finished.

**Task 5:** Use test-driven development to write a function `fizzbuzz(n)`, which returns the string that should be printed for the number `n` in the game of FizzBuzz (see [Lesson 3](../03-loops) Task 7). For example, `fizzbuzz(3)` should return `"Fizz"`, and `fizzbuzz(7)` should return `"7"`. Start with an empty `fizzbuzz.py` file, and a `test_fizzbuzz.py` file containing a single test, and follow the red, green, refactor cycle. What should `fizzbuzz(0)` or `fizzbuzz(-3)` do? [Solution (tests)](solutions/test_fizzbuzz.py) | [Solution (code)](solutions/fizzbuzz.py)

**⭐ Task 6:** [`exercises/stack.py`](exercises/stack.py) contains the `Stack` class from [Lesson 16](../16-recursion-stacks-and-queues) Task 5. Write tests for it. Think about everything that could go wrong: does `pop` return items in the right order? Does `peek` leave the item on the stack? Does `len` stay correct as items are pushed and popped? What happens when the stack is empty? [Solution](solutions/test_stack.py)

**⭐ Task 7:** [`exercises/sorting.py`](exercises/sorting.py) contains a version of bubble sort with a bug in it. Without looking for the bug first, write some tests that find it. Can you find a list that it _does_ sort correctly? (This is why it's important to test with lots of different data!) Once your tests have found the bug, fix it. [Solution (tests)](solutions/test_sorting.py) | [Solution (code)](solutions/sorting.py)

> [!NOTE]
> This repository uses `pytest` to check that all of the examples and model solutions in these lessons work correctly. Have a look at [`tests/test_solutions.py`](../../tests/test_solutions.py) to see how it's done!

---
[← Previous: Lesson 16](../16-recursion-stacks-and-queues) | [Contents](../../README.md) | [Next: Lesson 18 →](../18-linked-lists)
