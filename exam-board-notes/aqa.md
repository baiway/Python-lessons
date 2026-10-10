# AQA
AQA offers a GCSE (8525) and an A Level (7517) in Computer Science. Both present algorithms in exam questions using AQA's own _pseudo-code_, which is compared with Python [below](#aqa-pseudo-code-compared-with-python).

## GCSE (8525)
| Paper   | What it covers                                     | Format     | Length   | Marks | Weighting |
|---------|----------------------------------------------------|------------|----------|-------|-----------|
| Paper 1 | Computational thinking and programming skills      | Written    | 2 hours  | 90    | 50%       |

Paper 2 (the other 50%) covers the theory side of the course, such as computer systems, networks and data representation. AQA has removed some of the Paper 2 content for exams from 2027 onwards, but the papers themselves aren't changing.

- When your school enters you for the exam, it chooses which programming language Paper 1 uses: **C#, Python or VB.NET**. Exam questions show code in AQA pseudo-code and in that language.
- AQA says that you don't have to write in its pseudo-code style yourself. Your answers just need to be "clear, consistent and unambiguous".
- **Which lessons?** [Lessons 0 to 10](../README.md#fundamentals) cover the programming in the specification. The later lessons are extension material.

## A Level (7517)
| Component  | What it covers                                                    | Format    | Length            | Weighting |
|------------|-------------------------------------------------------------------|-----------|-------------------|-----------|
| Paper 1    | Programming, data structures, algorithms, theory of computation   | On-screen | 2 hours 30 minutes | 40%      |
| Paper 2    | Computer systems, data representation, networking, databases, etc. | Written  | 2 hours 30 minutes | 40%      |
| NEA        | A practical programming project (75 marks)                        | Coursework | —                 | 20%       |

- **Paper 1** is taken on a computer. AQA releases _preliminary material_ and a _skeleton program_ on 1 September, at the start of the school year in which you take the exam, so that you can study the program in advance. In the exam, you answer questions about it and write, adapt and extend it, in an "Electronic Answer Document". The skeleton program is available in **C#, Java, Python and VB.NET**: your school chooses which.
- **The NEA** (non-exam assessment) is a substantial programming project of your own choosing, worth 20% of the A Level.

### How the A Level programming content maps onto these lessons
| Topic (specification section)                                                   | Lessons                                                                 |
|---------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| Programming fundamentals, exception handling, subroutines (4.1.1)               | [1](../lessons/01-variables-and-types) to [8](../lessons/08-exceptions) |
| Recursion (4.1.1.16)                                                            | [16](../lessons/16-recursion-stacks-and-queues)                         |
| OOP: classes, encapsulation, inheritance, aggregation, composition, polymorphism, overriding; abstract, virtual and static methods; public, private and protected (4.1.2.3) | [11](../lessons/11-classes-and-objects) and [12](../lessons/12-inheritance-and-encapsulation) |
| Class diagrams, including composition (black diamond) and aggregation (white diamond) | [11](../lessons/11-classes-and-objects) and [12](../lessons/12-inheritance-and-encapsulation) |
| Static and dynamic data structures, arrays, records and files (4.2.1)           | [4](../lessons/04-lists), [5](../lessons/05-2d-lists), [9](../lessons/09-files), [15](../lessons/15-type-hints-and-dataclasses) |
| Stacks; linear and circular queues (4.2.2, 4.2.3)                               | [16](../lessons/16-recursion-stacks-and-queues)                         |
| Trees and binary search trees, tree traversals (4.2.5, 4.3.2)                   | [19](../lessons/19-binary-search-trees)                                 |
| Hash tables, including rehashing; dictionaries (4.2.6, 4.2.7)                   | [13](../lessons/13-dictionaries-and-sets) and [20](../lessons/20-hash-tables-and-sets) |
| Linear search, binary search, binary tree search, bubble sort, merge sort, Big O (4.3.4, 4.3.5) | [10](../lessons/10-searching-and-sorting) and [19](../lessons/19-binary-search-trees) |
| Priority queues, graphs and graph traversal, Dijkstra's algorithm, Reverse Polish notation, vectors | Not covered yet                                   |

## AQA pseudo-code compared with Python
You'll need to be able to read AQA's pseudo-code, and translate between it and Python. The examples below are based on AQA's GCSE pseudo-code guide. AQA's A Level papers present algorithms in pseudo-code too, so the guide is a good starting point at A Level as well, but look at past papers to see the conventions used there.

### The most common gotchas
1. **Loops include the end value.** `FOR i ← 1 TO 10` runs with `i` from 1 up to _and including_ 10. In Python, that's `for i in range(1, 11)`. Mixing these up is the classic "off-by-one" error!
2. **`=` means something different.** AQA uses `←` for assignment, and `=` for comparison (Python's `==`).
3. **Substrings work differently.** Python's slices use a start index and a stop index that _isn't_ included: `"computer"[2:5]` is `"mpu"`. AQA's `SUBSTRING(2, 4, 'computer')` uses a start index and an end index that _is_ included (also `'mpu'`).
4. **Integer division and remainders** are `DIV` and `MOD`, rather than `//` and `%`.
5. **`REPEAT ... UNTIL` loops** always run at least once, and stop when the condition becomes _true_. Python doesn't have these, but you can write one using `while True:` and `break`, as in [Lesson 3](../lessons/03-loops).

### Quick reference
Both columns below do the same thing. Like Python, AQA's pseudo-code indexes arrays and strings from 0.

| Concept                     | Python                                | AQA pseudo-code                                  |
|-----------------------------|---------------------------------------|--------------------------------------------------|
| Comment                     | `# comment`                           | `# comment`                                      |
| Assignment                  | `x = 3`                               | `x ← 3`                                          |
| Constant                    | `VAT = 0.2` (by convention only)      | `CONSTANT VAT ← 0.2`                             |
| Output                      | `print("Hello")`                      | `OUTPUT 'Hello'`                                 |
| Input                       | `name = input()`                      | `name ← USERINPUT`                               |
| Equal / not equal           | `==` / `!=`                           | `=` / `≠`                                        |
| Less / greater or equal     | `<=` / `>=`                           | `≤` / `≥`                                        |
| Logical operators           | `and`, `or`, `not`                    | `AND`, `OR`, `NOT`                               |
| Integer division            | `7 // 2`                              | `7 DIV 2`                                        |
| Remainder                   | `7 % 2`                               | `7 MOD 2`                                        |
| Power                       | `2 ** 3`                              | (not defined)                                    |
| String to integer           | `int("16")`                           | `STRING_TO_INT('16')`                            |
| Integer to string           | `str(16)`                             | `INT_TO_STRING(16)`                              |
| String to real (float)      | `float("16.3")`                       | `STRING_TO_REAL('16.3')`                         |
| Length of a string or array | `len(name)`                           | `LEN(name)`                                      |
| Character code              | `ord("a")`                            | `CHAR_TO_CODE('a')`                              |
| Character from code         | `chr(97)`                             | `CODE_TO_CHAR(97)`                               |
| First 3 characters          | `name[:3]`                            | `SUBSTRING(0, 2, name)`                          |
| Last 3 characters           | `name[-3:]`                           | `SUBSTRING(LEN(name) - 3, LEN(name) - 1, name)`  |
| Random integer from 1 to 6  | `random.randint(1, 6)`                | `RANDOM_INT(1, 6)`                               |
| Create an array             | `primes = [2, 3, 5]`                  | `primes ← [2, 3, 5]`                             |
| 2D array element            | `board[1][0]`                         | `board[1][0]`                                    |

### Loops
Count-controlled loops, printing 1 to 10, then the odd numbers from 1 to 9:
```python
# Python
for i in range(1, 11):
    print(i)

for i in range(1, 10, 2):
    print(i)
```
```
# AQA
FOR i ← 1 TO 10
   OUTPUT i
ENDFOR

FOR i ← 1 TO 9 STEP 2
   OUTPUT i
ENDFOR
```

Looping over the items in an array (or the characters in a string):
```python
# Python
for prime in primes:
    total = total + prime
```
```
# AQA
FOR prime IN primes
   total ← total + prime
ENDFOR
```

Condition-controlled loops (`while`, and "repeat until"):
```python
# Python
while answer != "yes":
    answer = input("Are we there yet? ")

while True:
    answer = input("Are we there yet? ")
    if answer == "yes":
        break
```
```
# AQA
WHILE answer ≠ 'yes'
   answer ← USERINPUT
ENDWHILE

REPEAT
   answer ← USERINPUT
UNTIL answer = 'yes'
```

### Selection
```python
# Python
if score >= 70:
    print("Merit")
elif score >= 50:
    print("Pass")
else:
    print("Fail")
```
```
# AQA
IF score ≥ 70 THEN
   OUTPUT 'Merit'
ELSE IF score ≥ 50 THEN
   OUTPUT 'Pass'
ELSE
   OUTPUT 'Fail'
ENDIF
```

### Subroutines
AQA's pseudo-code calls all of these `SUBROUTINE`s. A subroutine that uses `RETURN` is a _function_, and one that doesn't is a _procedure_. In Python, they're all just functions (see [Lesson 6](../lessons/06-functions)).
```python
# Python
def squared(number):
    return number ** 2

def greet(name):
    print("Hello " + name)
```
```
# AQA
SUBROUTINE squared(number)
   RETURN number * number
ENDSUBROUTINE

SUBROUTINE greet(name)
   OUTPUT 'Hello ' + name
ENDSUBROUTINE
```

### Records
AQA's pseudo-code has _records_, which group several named fields together:
```
RECORD Car
   make : String
   price : Real
ENDRECORD

myCar ← Car('Ford', 1399.99)
OUTPUT myCar.make
```

The closest thing in Python is a dataclass ([Lesson 15](../lessons/15-type-hints-and-dataclasses)):
```python
from dataclasses import dataclass

@dataclass
class Car:
    make: str
    price: float

my_car = Car("Ford", 1399.99)
print(my_car.make)
```

## Sources
- [GCSE Computer Science specification](https://www.aqa.org.uk/subjects/computer-science/gcse/computer-science-8525/specification) (8525), [specification changes for exams from 2027](https://www.aqa.org.uk/gcse-computer-science-specification-changes-for-summer-2027), and [Notes and guidance: Pseudo-code](https://filestore.aqa.org.uk/resources/computing/AQA-8525-NG-PC.PDF) (2024).
- [AS and A-level Computer Science specification](https://filestore.aqa.org.uk/resources/computing/specifications/AQA-7516-7517-SP-2015.PDF) (7516/7517), version 1.6.

---
[Exam board notes](README.md) | [Contents](../README.md)
