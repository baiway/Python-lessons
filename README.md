# Resources for learning Python from scratch
A set of lessons and exercises for learning Python from scratch. They assume no prior programming experience (although if you've used Scratch or written pseudocode before, you'll find the early lessons go quickly!), and cover everything you need for GCSE and IB Computer Science, plus a few extras. This is a work in progress.

## How to use these lessons
Each lesson lives in its own folder inside [`lessons`](lessons) and contains:
- `README.md`: explanations, examples and tasks. This is where you should start. You can read it right here on GitHub.
- `examples/`: the example code from the lesson, so you can run it yourself.
- `exercises/`: starter code for some of the tasks. Replace each `...` with your own code.
- `solutions/`: my model solutions to every task. Try each task yourself before looking at these! There's usually more than one correct way to solve a problem, so don't worry if your solution looks a bit different to mine.

Tasks marked with a ⭐ are challenge tasks. These are a bit harder (or a bit longer) than the others. Have a go at them if you finish early or want to stretch yourself.

You can run any of the programs with `python <script>.py` (or `python3 <script>.py` on macOS/Linux). From [Lesson 15](lessons/15-packages) onwards, we use third-party packages, and you'll need [`uv`](https://docs.astral.sh/uv/) to run some programs (see [Lesson 0](lessons/00-getting-started) for how to install it).

## Contents
### Fundamentals
- [Lesson 0](lessons/00-getting-started): Installing Python and VS Code, writing a "hello world" program, and interactive mode
- [Lesson 1](lessons/01-variables-and-types): Variables, data types, arithmetic, f-strings and user input
- [Lesson 2](lessons/02-conditionals): Conditional logic (`if`, `elif` and `else`)
- [Lesson 3](lessons/03-loops): `for` loops and `while` loops
- Lesson 4: Lists (*not yet written*)
- Lesson 5: 2D lists (*not yet written*)
- Lesson 6: Functions (*not yet written*)
- Lesson 7: Strings and string formatting (*not yet written*)
- Lesson 8: Errors and exceptions (`try`, `except`, `else` and `finally`) (*not yet written*)
- Lesson 9: Reading and writing files (*not yet written*)
- Lesson 10: Searching and sorting algorithms (*not yet written*)
- Lesson 11: Classes and objects (*not yet written*)
- Lesson 12: Inheritance and encapsulation (including a comparison with C++) (*not yet written*)

### Extras
- Lesson 13: Dictionaries and sets (*not yet written*)
- Lesson 14: Type hints and dataclasses (*not yet written*)
- Lesson 15: Modules and third-party packages (`numpy` and `matplotlib`) (*not yet written*)
- Lesson 16: Recursion, stacks and queues (*not yet written*)
- Lesson 17: Testing your code with `pytest` (*not yet written*)
- Exam board notes: differences between exam boards' pseudocode and requirements (*not yet written*)

## For teachers
This repository is a [`uv`](https://docs.astral.sh/uv/) project. To check that all the examples and model solutions run correctly, use:
```sh
uv run pytest
```

Scripts that ask for user input are given simulated input, which is defined in [`tests/test_solutions.py`](tests/test_solutions.py). If you add a new interactive script, add some input for it there.
