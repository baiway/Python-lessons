# Task 2 solution
Running the program with `python`, it prints the average score, then crashes on line 8:
```
76.0
Traceback (most recent call last):
  ...
TypeError: can only concatenate str (not "int") to str
```

So Python only finds **one** bug, and only once it reaches that line. If we fixed that line and ran the program again, it would find the next bug, and so on. (Worse, one of the bugs doesn't cause a crash at all: `best_student` returns `1` instead of `"Alan"`, which `print` is perfectly happy to print!)

mypy, on the other hand, finds all four bugs without running the program (it reports five errors, because one bug causes two of them):
```
find_the_bugs.py:8: error: Unsupported operand types for + ("str" and "int")  [operator]
find_the_bugs.py:17: error: Incompatible return value type (got "int", expected "str")  [return-value]
find_the_bugs.py:25: error: Argument 1 to "best_student" has incompatible type "list[int]"; expected "list[str]"  [arg-type]
find_the_bugs.py:25: error: Argument 2 to "best_student" has incompatible type "list[str]"; expected "list[int]"  [arg-type]
find_the_bugs.py:26: error: Argument 1 to "average_score" has incompatible type "str"; expected "list[int]"  [arg-type]
Found 5 errors in 1 file (checked 1 source file)
```

The four bugs are:
1. Line 8: `score` is an `int`, so it can't be joined to a string with `+`. Use an f-string instead.
2. Line 17: `best_student` returns the _index_ of the best student, rather than their name. It should return `names[best]`.
3. Line 25: the arguments to `best_student` are the wrong way round.
4. Line 26: `average_score` is given a string instead of a list.

The fixed program is:
```python
def average_score(scores: list[int]) -> float:
    """Returns the mean of a list of scores"""
    return sum(scores) / len(scores)


def describe_score(name: str, score: int) -> str:
    """Returns a sentence describing someone's score"""
    return f"{name} scored {score} points"


def best_student(names: list[str], scores: list[int]) -> str:
    """Returns the name of the student with the highest score"""
    best = 0
    for i in range(len(scores)):
        if scores[i] > scores[best]:
            best = i
    return names[best]


names = ["Ada", "Alan", "Grace"]
scores = [72, 90, 65]

print(average_score(scores))
print(describe_score("Ada", 72))
print(best_student(names, scores))
print(average_score([72, 90, 65]))
```
