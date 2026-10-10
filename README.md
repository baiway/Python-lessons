# Resources for learning Python from scratch
A set of lessons and exercises for learning Python from scratch. They assume no prior programming experience (although if you've used Scratch or written pseudocode before, you'll find the early lessons go quickly!), and cover everything you need for GCSE and IB Computer Science, plus a few extras. This is a work in progress.

## How to use these lessons
Each lesson lives in its own folder inside [`lessons`](lessons) and contains:
- `README.md`: explanations, examples and tasks. This is where you should start. You can read it right here on GitHub.
- `examples/`: the example code from the lesson, so you can run it yourself.
- `exercises/`: starter code for some of the tasks. Replace each `...` with your own code.
- `solutions/`: my model solutions to every task. Try each task yourself before looking at these! There's usually more than one correct way to solve a problem, so don't worry if your solution looks a bit different to mine.

Tasks marked with a ⭐ are challenge tasks. These are a bit harder (or a bit longer) than the others. Have a go at them if you finish early or want to stretch yourself.

You can run any of the programs with `python <script>.py` (or `python3 <script>.py` on macOS/Linux). Some programs in [Lesson 14](lessons/14-packages) use third-party packages (`numpy` and `matplotlib`), which you'll need to install first. That lesson explains how, using either `pip` or [`uv`](https://docs.astral.sh/uv/).

## Contents
### Fundamentals
- [Lesson 0](lessons/00-getting-started): Installing Python and VS Code, writing a "hello world" program, and interactive mode
- [Lesson 1](lessons/01-variables-and-types): Variables, data types, arithmetic, f-strings and user input
- [Lesson 2](lessons/02-conditionals): Conditional logic (`if`, `elif` and `else`)
- [Lesson 3](lessons/03-loops): `for` loops and `while` loops
- [Lesson 4](lessons/04-lists): Lists
- [Lesson 5](lessons/05-2d-lists): 2D lists
- [Lesson 6](lessons/06-functions): Functions
- [Lesson 7](lessons/07-strings): Strings and string formatting
- [Lesson 8](lessons/08-exceptions): Errors and exceptions (`try`, `except`, `else` and `finally`)
- [Lesson 9](lessons/09-files): Reading and writing files
- [Lesson 10](lessons/10-searching-and-sorting): Searching and sorting algorithms
- [Lesson 11](lessons/11-classes-and-objects): Classes and objects
- [Lesson 12](lessons/12-inheritance-and-encapsulation): Inheritance and encapsulation (including a comparison with C++)

### Extras
- [Lesson 13](lessons/13-dictionaries-and-sets): Tuples, dictionaries, sets and comprehensions
- [Lesson 14](lessons/14-packages): Modules and third-party packages (`numpy` and `matplotlib`)
- [Lesson 15](lessons/15-type-hints-and-dataclasses): Type hints and dataclasses
- [Lesson 16](lessons/16-recursion-stacks-and-queues): Recursion, stacks and queues
- [Lesson 17](lessons/17-testing): Testing your code with `pytest`

### Abstract data types
These lessons go beyond GCSE, but are needed for IB Computer Science (HL) and A Level Computer Science.
- [Lesson 18](lessons/18-linked-lists): Linked lists (singly, doubly and circular)
- [Lesson 19](lessons/19-binary-search-trees): Binary search trees
- [Lesson 20](lessons/20-hash-tables-and-sets): Hash tables and sets

### Exam board notes
- [Exam board notes](exam-board-notes): how each GCSE, A Level and IB course assesses programming, how each board's pseudocode compares with Python, and which lessons cover each specification

## For teachers
This repository is a [`uv`](https://docs.astral.sh/uv/) project. To check that all the examples and model solutions run correctly, use:
```sh
uv run --group scientific pytest
```

The `scientific` dependency group contains `numpy` and `matplotlib`, which are only needed for [Lesson 14](lessons/14-packages). If you leave out `--group scientific`, the scripts that need them are skipped.

Scripts that ask for user input are given simulated input, which is defined in [`tests/test_solutions.py`](tests/test_solutions.py). If you add a new interactive script, add some input for it there. Each script is run from a temporary copy of its own folder, so any files it creates don't end up in the repository. The C++ examples in [Lesson 12](lessons/12-inheritance-and-encapsulation) are compiled and run too, if `g++` is installed, the type hints in [Lesson 15](lessons/15-type-hints-and-dataclasses) are checked with `mypy`, and the test files in [Lesson 17](lessons/17-testing) are run with `pytest`.
