# OCR
OCR offers a GCSE (J277) and an A Level (H446) in Computer Science. Exam questions present code in OCR's own pseudocode, which is called the _Exam Reference Language_ (ERL) at GCSE. It's compared with Python [below](#ocr-exam-reference-language-compared-with-python).

## GCSE (J277)
| Paper   | What it covers                                        | Format  | Length             | Marks | Weighting |
|---------|-------------------------------------------------------|---------|--------------------|-------|-----------|
| Paper 2 | Computational thinking, algorithms and programming    | Written | 1 hour 30 minutes  | 80    | 50%       |

Paper 1 (the other 50%) covers computer systems.

- **Section A** of Paper 2 lets you answer in whatever way is clearest: pseudocode, flowcharts, bullet points, English, ERL or a programming language.
- **Section B** tests your ability to design, write, test and refine programs. Questions that ask you to write or refine code must be answered in **OCR's ERL or a high-level programming language** such as Python. OCR says that it will "avoid penalising [students] for minor errors in syntax", but answers written in pseudocode or English won't get marks for these questions.
- **Which lessons?** [Lessons 0 to 10](../README.md#fundamentals) cover the programming in the specification. The later lessons are extension material.

## A Level (H446)
| Component  | What it covers                                        | Format     | Length             | Marks | Weighting |
|------------|-------------------------------------------------------|------------|--------------------|-------|-----------|
| Paper 1    | Computer systems                                      | Written    | 2 hours 30 minutes | 140   | 40%       |
| Paper 2    | Algorithms and programming                            | Written    | 2 hours 30 minutes | 140   | 40%       |
| Programming project | A project of your own choosing (non-exam assessment) | Coursework | —           | 70    | 20%       |

- **Paper 2** has two sections. Section A covers algorithms, programming and programming techniques. Section B starts with a scenario, followed by longer problem-solving and programming questions.
- **The programming project** can be written in Python, the C family of languages (e.g. C#), Java or Visual Basic. OCR's specification says that "all tasks completed in all languages need to have a suitable graphical interface". These lessons don't cover graphical user interfaces yet, so you'll need to learn a GUI library (such as Python's built-in `tkinter`) for your project.
- OCR's A Level pseudocode guide says that students "are not expected to memorise the syntax of this pseudocode", and can answer in "any style of pseudocode they choose", as long as a competent programmer could work out what it means.

### How the A Level programming content maps onto these lessons
| Topic (specification section)                                                   | Lessons                                                                 |
|---------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| Programming constructs, subroutines, scope (2.2.1)                              | [1](../lessons/01-variables-and-types) to [8](../lessons/08-exceptions) |
| Recursion (2.2.1)                                                               | [16](../lessons/16-recursion-stacks-and-queues)                         |
| Object-oriented programming: classes, objects, methods, attributes, inheritance, encapsulation, polymorphism (1.2.4) | [11](../lessons/11-classes-and-objects) and [12](../lessons/12-inheritance-and-encapsulation) |
| Arrays (up to 3 dimensions), records, lists, tuples (1.4.2)                     | [4](../lessons/04-lists), [5](../lessons/05-2d-lists), [13](../lessons/13-dictionaries-and-sets), [15](../lessons/15-type-hints-and-dataclasses) |
| Stacks and queues (1.4.2, 2.3.1)                                                | [16](../lessons/16-recursion-stacks-and-queues)                         |
| Linked lists (1.4.2, 2.3.1)                                                     | [18](../lessons/18-linked-lists)                                        |
| Trees, binary search trees, depth-first and breadth-first traversal (1.4.2, 2.3.1) | [19](../lessons/19-binary-search-trees)                              |
| Hash tables (1.4.2)                                                             | [20](../lessons/20-hash-tables-and-sets)                                |
| Bubble sort, insertion sort, merge sort, binary search, linear search, Big O (2.3.1) | [10](../lessons/10-searching-and-sorting)                          |
| Graphs, quick sort, Dijkstra's shortest path algorithm, A* algorithm            | Not covered yet                                                         |

## OCR Exam Reference Language compared with Python
The examples below use the GCSE Exam Reference Language. OCR's A Level pseudocode is almost identical, with a few [differences](#differences-in-the-a-level-pseudocode), described at the end.

### The most common gotchas
1. **Loops include the end value.** `for i = 1 to 10` runs with `i` from 1 up to _and including_ 10. In Python, that's `for i in range(1, 11)`. Mixing these up is the classic "off-by-one" error!
2. **Substrings work differently.** Python's slices use a start index and a stop index that _isn't_ included: `"computer"[2:5]` is `"mpu"`. OCR's `"computer".substring(2, 3)` uses a start index and a _number of characters_ (also `"mpu"`).
3. **Integer division and remainders** are `DIV` and `MOD`, rather than `//` and `%`. Powers are written with `^`, rather than `**`.
4. **`do ... until` loops** always run at least once, and stop when the condition becomes _true_. Python doesn't have these, but you can write one using `while True:` and `break`, as in [Lesson 3](../lessons/03-loops).
5. **2D arrays use one pair of brackets:** `board[1, 0]`, rather than Python's `board[1][0]`.

### Quick reference
Both columns below do the same thing. Like Python, OCR's ERL indexes arrays and strings from 0.

| Concept                     | Python                                | OCR Exam Reference Language             |
|-----------------------------|---------------------------------------|-----------------------------------------|
| Comment                     | `# comment`                           | `// comment`                            |
| Assignment                  | `x = 3`                               | `x = 3`                                 |
| Constant                    | `VAT = 0.2` (by convention only)      | `const vat = 0.2`                       |
| Global variable             | `global x` (inside a function, to change a global) | `global userID = "Cust001"` |
| Output                      | `print("Hello")`                      | `print("Hello")`                        |
| Input                       | `name = input("Enter a name")`        | `name = input("Enter a name")`          |
| Equal / not equal           | `==` / `!=`                           | `==` / `!=`                             |
| Logical operators           | `and`, `or`, `not`                    | `AND`, `OR`, `NOT`                      |
| Integer division            | `7 // 2`                              | `7 DIV 2`                               |
| Remainder                   | `7 % 2`                               | `7 MOD 2`                               |
| Power                       | `2 ** 3`                              | `2 ^ 3`                                 |
| Casting                     | `int("16")`, `str(16)`, `float("16.3")` | `int("16")`, `str(16)`, `float("16.3")` or `real("16.3")` |
| Length of a string          | `len(name)`                           | `name.length`                           |
| Character code              | `ord("a")`                            | `ASC("a")`                              |
| Character from code         | `chr(97)`                             | `CHR(97)`                               |
| Upper / lower case          | `name.upper()` / `name.lower()`       | `name.upper` / `name.lower`             |
| First / last 3 characters   | `name[:3]` / `name[-3:]`              | `name.left(3)` / `name.right(3)`        |
| Random integer from 1 to 6  | `random.randint(1, 6)`                | `random(1, 6)`                          |
| Create an array             | `names = [None] * 5`                  | `array names[5]`                        |
| 2D array element            | `board[1][0]`                         | `board[1, 0]`                           |

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
// OCR
for i = 1 to 10
    print(i)
next i

for i = 1 to 9 step 2
    print(i)
next i
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
// OCR
while answer != "yes"
    answer = input("Are we there yet?")
endwhile

do
    answer = input("Are we there yet?")
until answer == "yes"
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
// OCR
if score >= 70 then
    print("Merit")
elseif score >= 50 then
    print("Pass")
else
    print("Fail")
endif
```

OCR's ERL also has a `switch`/`case` statement. You can do the same thing in Python with `if`/`elif`/`else`, or with Python's `match` statement (Python 3.10 onwards), which these lessons don't cover.

### Subroutines
OCR distinguishes between _functions_ (which return a value) and _procedures_ (which don't). In Python, they're all just functions (see [Lesson 6](../lessons/06-functions)).
```python
# Python
def squared(number):
    return number ** 2

def greet(name):
    print("Hello " + name)
```
```
// OCR
function squared(number)
    return number^2
endfunction

procedure greet(name)
    print("Hello " + name)
endprocedure
```

### Files
Compare OCR's file handling with [Lesson 9](../lessons/09-files):
```python
# Python
with open("sample.txt", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

with open("sample.txt", "a", encoding="utf-8") as file:
    file.write("Add new line\n")
```
```
// OCR (GCSE)
myFile = open("sample.txt")
while NOT myFile.endOfFile()
    print(myFile.readLine())
endwhile
myFile.close()

myFile = open("sample.txt")
myFile.writeLine("Add new line")
myFile.close()
```

At GCSE, `writeLine` always adds the line to the _end_ of the file (like Python's `"a"` mode), and `newFile("myText.txt")` creates a new, empty file.

### Arrays vs lists
OCR's ERL uses _arrays_ rather than lists. As we saw in [Lesson 4](../lessons/04-lists), arrays are like Python lists, except that they have a fixed size, and OCR's specification says that "arrays only store a single data type". You declare an array's size up front (`array names[5]`), and you access 2D arrays using a single pair of square brackets (`gameboard[1, 0]`).

### Differences in the A Level pseudocode
OCR's A Level pseudocode guide is almost the same as the GCSE ERL, with these differences and additions:
- **Files** are opened for reading with `openRead`, and for writing with `openWrite`. Writing with `openWrite` replaces anything already in the file (like Python's `"w"` mode).
- **Parameters** are passed by value unless stated otherwise. When it matters, questions use `byVal` and `byRef`, e.g. `procedure foobar(x:byVal, y:byRef)`.
- **Object-oriented code** uses `class ... endclass`, `public` and `private` (attributes and methods are public unless stated otherwise), a constructor procedure called `new`, `inherits` for inheritance, and `super` to call the parent class's methods. Objects are created with `new`, e.g. `myDog = new Dog("Fido", "Scottish Terrier")`. The guide also says that students "aren't expected to be aware of static methods".

Here's a class with a constructor and inheritance in OCR's A Level pseudocode, and in Python (see [Lesson 11](../lessons/11-classes-and-objects) and [Lesson 12](../lessons/12-inheritance-and-encapsulation)):
```
// OCR (A Level)
class Pet
    private name
    public procedure new(givenName)
        name = givenName
    endprocedure
endclass

class Dog inherits Pet
    private breed
    public procedure new(givenName, givenBreed)
        super.new(givenName)
        breed = givenBreed
    endprocedure
endclass

myDog = new Dog("Fido", "Scottish Terrier")
```
```python
# Python
class Pet:
    def __init__(self, given_name):
        self.__name = given_name


class Dog(Pet):
    def __init__(self, given_name, given_breed):
        super().__init__(given_name)
        self.__breed = given_breed


my_dog = Dog("Fido", "Scottish Terrier")
```

## Sources
- [GCSE (9–1) Computer Science J277 specification](https://www.ocr.org.uk/qualifications/gcse/computer-science-j277-from-2020/), version 1, sections 3b and 3c (Exam Reference Language).
- [A Level Computer Science H446 specification](https://www.ocr.org.uk/qualifications/as-and-a-level/computer-science-h046-h446-from-2015/), version 3.0 (April 2026), including appendices 5d (pseudocode guide) and 5e (acceptable programming languages).

---
[Exam board notes](README.md) | [Contents](../README.md)
