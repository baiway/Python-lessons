# Lesson 15: Type hints and dataclasses
Python is a _dynamically typed_ language: variables don't have a fixed type, and Python only checks whether you're using a value sensibly while your program is running. This makes Python quick to write, but it also means that some mistakes (like passing a string to a function that expects a list) only show up when that line of code actually runs, which might be in the middle of an exam, or after your program has been running for an hour!

Many other languages (like C++, which we saw in [Lesson 12](../12-inheritance-and-encapsulation), and Java) are _statically typed_: you have to say what type every variable is, and the compiler checks that everything fits together before your program runs at all. In this lesson, we'll see how to get some of the benefits of static typing in Python, using _type hints_. We'll then see how type hints let us write simple classes much more quickly, using _dataclasses_.

## Type hints
A _type hint_ (or _type annotation_) says what type a variable, parameter or return value should have. We write them after a colon for variables and parameters, and after an arrow `->` for return values:
```python
name: str = "Ada"
age: int = 36

def sphere_surface_area(radius: float) -> float:
    """Calculates the surface area of a sphere with the given radius"""
    return 4 * math.pi * radius**2

def greet(name: str, greeting: str = "Hello") -> None:
    """Prints a greeting"""
    print(f"{greeting}, {name}!")
```

A function that doesn't return anything has a return type of `None`. For collections, put the type of the items inside square brackets:

| Type hint            | Meaning                                                     | Example                      |
|----------------------|-------------------------------------------------------------|------------------------------|
| `list[int]`          | A list of integers                                          | `[1, 2, 3]`                  |
| `list[list[str]]`    | A 2D list of strings                                        | `[["X", "O"], [" ", "X"]]`   |
| `dict[str, float]`   | A dictionary with string keys and float values              | `{"Ada": 72.5}`              |
| `set[str]`           | A set of strings                                            | `{"red", "blue"}`            |
| `tuple[int, int]`    | A tuple containing exactly two integers                     | `(3, 4)`                     |
| `int \| None`        | Either an integer or `None`                                 | `None`                       |
| `int \| float`       | Either an integer or a float                                | `3.14`                       |

Here's the most important thing to understand about type hints: **Python completely ignores them when running your code.** This runs without any complaint:
```python
age: int = "thirty-six"
```

So what's the point? Type hints are for _humans_ and _tools_:
1. They're documentation. When you read `def mean(numbers: list[float]) -> float:`, you know exactly what the function expects, and what it gives back, without having to read the code.
2. VS Code uses them to give you better auto-completion: if it knows that `name` is a `str`, it can suggest string methods when you type `name.`.
3. A _type checker_ can read your type hints and check that your code is consistent, _without running it_. This catches lots of bugs before they happen.

## Type checkers
The most widely used type checker is [mypy](https://mypy-lang.org/). Like `numpy` and `matplotlib`, it's a third-party package, so you'll need to install it using one of the methods from [Lesson 14](../14-packages). For example, with your virtual environment activated:
```sh
pip install mypy
```

or, in a `uv` project:
```sh
uv add --dev mypy
```

`--dev` adds `mypy` to a dependency group called `dev`, which `uv` installs by default. It's for packages that you need while _developing_ your code, but that your program doesn't need in order to run. (If you've cloned this repository, `mypy` is already in its `dev` group, so you don't need to install anything.) You can then check a program by running `mypy my_program.py` (or `uv run mypy my_program.py`).

If you've installed `uv`, you can also skip installing mypy altogether, and use `uvx`, which downloads a tool and runs it in one go:
```sh
uvx mypy my_program.py
```

mypy will print a list of problems, or `Success: no issues found` if it can't find any. For example, running it on [`exercises/find_the_bugs.py`](exercises/find_the_bugs.py) gives:
```
find_the_bugs.py:8: error: Unsupported operand types for + ("str" and "int")  [operator]
...
Found 5 errors in 1 file (checked 1 source file)
```

VS Code can also check your types as you type, using the Pylance extension (which comes with the Python extension we installed in [Lesson 0](../00-getting-started)). To turn this on, open the settings (`Ctrl` + `,` on Windows, `⌘` + `,` on macOS), search for "type checking mode", and change it from "off" to "standard". Type errors will then be underlined in red, just like spelling mistakes.

> [!NOTE]
> Should you use type hints in your own code? For short scripts, they're optional, and many Python programmers don't bother. But for anything bigger, they're very helpful, and most professional Python code uses them. Check what your course expects in exams: most exam boards don't expect type hints in Python answers, but writing them won't lose you marks either.

**Task 1:** Add type hints to every function in [`exercises/add_type_hints.py`](exercises/add_type_hints.py). Then run mypy on your file to check that it's happy. [Solution](solutions/task1_add_type_hints.py)

**Task 2:** [`exercises/find_the_bugs.py`](exercises/find_the_bugs.py) contains four bugs. First, run the program with `python`. How many of the bugs does Python find? Then run mypy on it. How many bugs does mypy find? Fix all the bugs, so that both Python and mypy are happy. [Solution](solutions/task2_find_the_bugs.md)

## Dataclasses
In [Lesson 11](../11-classes-and-objects), we wrote lots of classes that looked like this:
```python
class Student:
    def __init__(self, name, year, scores):
        self.name = name
        self.year = year
        self.scores = scores
```

Notice how repetitive `__init__` is: we have to write out each attribute name three times! And if we want to print a student nicely, or compare two students with `==`, we need to write `__str__` and `__eq__` too. Python can write all of this for us if we use a _dataclass_:
```python
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    year: int
    scores: list[int]

    def mean_score(self) -> float:
        return sum(self.scores) / len(self.scores)
```

The `@dataclass` decorator looks at the attributes listed in the class (which _must_ have type hints) and automatically writes:
- an `__init__` method that takes each attribute as a parameter, in order,
- a `__repr__` method (similar to `__str__`), so that printing a student gives something useful like `Student(name='Ada', year=10, scores=[72, 85, 64])`,
- an `__eq__` method, so that two students with the same attributes are equal.

You can still add your own methods, like `mean_score` above, just as with a normal class.
```python
>>> ada = Student("Ada", 10, [72, 85, 64])
>>> ada
Student(name='Ada', year=10, scores=[72, 85, 64])
>>> ada.mean_score()
73.66666666666667
>>> ada == Student("Ada", 10, [72, 85, 64])
True
```

### Default values
You can give attributes default values, as long as all the attributes with defaults come after all the ones without:
```python
@dataclass
class BankAccount:
    owner: str
    balance: float = 0.0
```

There's one catch: if the default is a mutable value like a list or a dictionary, you have to use `field(default_factory=...)`. This creates a brand new empty list for each object, which avoids the "shared default list" trap from [Lesson 11](../11-classes-and-objects). (If you forget, Python will refuse to create the class, which is helpful!)
```python
from dataclasses import dataclass, field

@dataclass
class Student:
    name: str
    year: int
    scores: list[int] = field(default_factory=list)
```

### Frozen and ordered dataclasses
The `@dataclass` decorator takes some useful options:
- `@dataclass(frozen=True)` makes objects immutable: once created, their attributes can't be changed. Like tuples, frozen dataclasses can be used as dictionary keys and stored in sets.
- `@dataclass(order=True)` adds `<`, `>`, `<=` and `>=`, so objects can be sorted. They're compared attribute by attribute, in the order the attributes are listed (so in the `Student` class above, by `name` first, then `year` if the names are the same, and so on).

You can find all of these examples in [`examples/dataclasses_example.py`](examples/dataclasses_example.py).

**Task 3:** Rewrite your `Student` class from [Lesson 11](../11-classes-and-objects) Task 4 as a dataclass, with type hints on every attribute and method. `scores` should default to an empty list. Use it to find the student with the highest mean score, as before. [Solution](solutions/task3_student_dataclass.py)

**Task 4:** Write a frozen dataclass `Point` with `x` and `y` coordinates (both floats), and a method `distance_to(other: Point) -> float` that returns the distance between two points. What happens if you try to change a point's `x` coordinate after creating it? [Solution](solutions/task4_point.py)

**Task 5:** Write a dataclass `Item` representing an item in a shop, with a `name`, a `price` (in £) and a `quantity` in stock. Create a list of a few items, then print: the total value of all the stock, the items sorted from cheapest to most expensive, and the names of any items that are out of stock. [Solution](solutions/task5_shop.py)

**⭐ Task 6:** Write a small library system. Create a dataclass `Book` with a `title`, an `author`, an `isbn` and an `on_loan` attribute (which should default to `False`). Then write a `Library` class (this can be a normal class or a dataclass, it's up to you) that stores its books in a dictionary, using the ISBN as the key. Give it fully type-hinted methods to `add_book`, `borrow` a book (by ISBN) and `return_book`. `borrow` and `return_book` should raise exceptions if the book doesn't exist, or is already on loan (or isn't on loan). Test your classes, then check them with mypy. [Solution](solutions/task6_library.py)

**⭐ Task 7:** Use `@dataclass(order=True)` to write a `Card` dataclass that can be sorted by its value, so that `sorted(hand)` puts a hand of cards in order. Hint: the attribute you want to sort by needs to come first. Can you also make the cards print nicely (like `7♠`) without changing how they're sorted? [Solution](solutions/task7_sortable_cards.py)

---
[← Previous: Lesson 14](../14-packages) | [Contents](../../README.md) | [Next: Lesson 16 →](../16-recursion-stacks-and-queues)
