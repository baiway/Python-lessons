# Exam board notes
The lessons in this repository are deliberately independent of any exam board: everything in them is plain Python, and it's all useful whichever course you're taking. But each exam board assesses programming in its own way, and some of them use their own _pseudocode_ in exam questions. This page summarises the differences, and how the Python you've learnt maps onto each board's pseudocode.

> [!WARNING]
> Exam boards update their specifications and guidance from time to time. I checked everything on this page against each board's published documents in October 2026 (see [Sources](#sources) at the bottom), but you should always check the latest version of your own board's specification, and ask your teacher if you're unsure.

## How is programming assessed?

| Course                          | Programming exam                                    | Format                                 | Language                                                    |
|---------------------------------|-----------------------------------------------------|----------------------------------------|-------------------------------------------------------------|
| AQA GCSE (8525)                 | Paper 1: 2 hours, 90 marks, 50% of the GCSE         | Written                                | Chosen when you're entered: C#, Python or VB.NET            |
| OCR GCSE (J277)                 | Paper 2: 1 hour 30 minutes, 80 marks, 50%           | Written                                | OCR Exam Reference Language, or "a high-level language"     |
| Pearson Edexcel GCSE (1CP2)     | Paper 2: 2 hours, 75 marks, 50%                     | On-screen, using an IDE                | Python 3                                                    |
| Eduqas GCSE (Component 2)       | Component 2: 2 hours, 80 marks, 50%                 | On-screen, plus a word processor       | Python 3                                                    |
| IB Diploma (first exams 2027)   | Paper 2: 1 hour 15 minutes (SL) or 2 hours (HL)     | Written                                | Python or Java (your school chooses)                        |

### Written exams (AQA, OCR and IB)
In a written exam, you'll write code with a pen, without an IDE to spot your mistakes or auto-complete things for you. You'll also be asked to read and _trace_ code (work out what it does, step by step, often using a trace table). Some things to practise:
- **Write code by hand**, under timed conditions. It feels very different to typing!
- **Indentation still matters.** Make it obvious which lines are inside each loop, `if` statement or function. Some students draw faint vertical lines to keep their indentation straight.
- **Small syntax slips are usually forgiven**, but the logic must be right. OCR's specification, for example, says that it will "avoid penalising [students] for minor errors in syntax".
- **Read your board's pseudocode**: exam questions present code in it, even if you answer in Python (see below).

### On-screen exams (Edexcel and Eduqas)
In an on-screen exam, you'll write, run and test real Python 3 code on a computer, without access to the internet. Some things to bear in mind:
- **Practise in the IDE you'll use in the exam.** It may well be IDLE (which comes with Python) or Thonny (see [Lesson 0](../lessons/00-getting-started)) rather than VS Code, so make sure you're comfortable with it, and know how to run your code and read error messages in it.
- **Only the standard library is available.** Don't rely on third-party packages like `numpy` or `matplotlib` ([Lesson 14](../lessons/14-packages)). Eduqas says that "only the standard Python 3 download should be used with no additional libraries installed".
- **Edexcel** gives you a _Programming Language Subset_ (PLS): a document listing the parts of Python that the exam can ask you to use, which you'll have on paper and on screen during the exam. Pearson won't set tasks that go beyond it, so get the latest version from Pearson's website and get to know it well.
- **Eduqas** releases a _scenario_ (a list of requirements) on 1 September of the year before the exam, which you'll work on in advance. In the exam itself, you're given a prototype Python program to use, evaluate and change, and you answer some questions in a word-processed document. The specification also mentions graphical user interfaces built using Python's built-in libraries (i.e. `tkinter`), which these lessons don't cover.

### IB Computer Science
The IB Computer Science course changed for students taking their exams from May 2027 onwards. From what IB has published, and from summaries of the new guide:
- Paper 2 tests computational thinking and programming, and there are two versions of it: one for Python and one for Java. Your school chooses which language you study.
- The IB-specific pseudocode used by the old course is no longer used.
- Object-oriented programming ([Lesson 11](../lessons/11-classes-and-objects) and [Lesson 12](../lessons/12-inheritance-and-encapsulation)) is part of the core course for everyone.
- HL students also study _abstract data types_, such as stacks and queues ([Lesson 16](../lessons/16-recursion-stacks-and-queues)), linked lists and binary search trees, along with recursion. (Linked lists and trees aren't covered in these lessons yet.)
- The internal assessment (worth 30% at SL and 20% at HL) is a "computational solution": a program that you design, build and evaluate, with up to 2,000 words of documentation and a video showing it working.

I wasn't able to check all of these points against the official IB subject guide, which isn't freely available, so treat this as a summary and check the details with your teacher.

## Pseudocode compared with Python
AQA and OCR both present code in exam questions using their own pseudocode. You'll need to be able to read it, and translate between it and Python. (AQA says you don't have to write its pseudo-code yourself, as long as your answer is "clear, consistent and unambiguous". OCR accepts answers in its Exam Reference Language or in a high-level language like Python, depending on the question.)

### The most common gotchas
These are the differences that catch people out most often:
1. **Loops include the end value.** `FOR i ← 1 TO 10` (AQA) and `for i = 1 to 10` (OCR) both run with `i` from 1 up to _and including_ 10. In Python, that's `for i in range(1, 11)`. Mixing these up is the classic "off-by-one" error!
2. **`=` means different things.** AQA uses `←` for assignment and `=` for comparison. OCR, like Python, uses `=` for assignment and `==` for comparison.
3. **Substrings work differently.** Python's slices use a start index and a stop index that _isn't_ included: `"computer"[2:5]` is `"mpu"`. AQA's `SUBSTRING(2, 4, 'computer')` uses a start index and an end index that _is_ included (also `'mpu'`). OCR's `"computer".substring(2, 3)` uses a start index and a _number of characters_ (`"mpu"` again!).
4. **Integer division and remainders** are `DIV` and `MOD` in both pseudocodes, rather than `//` and `%`.
5. **"Repeat until" loops** (`REPEAT ... UNTIL` in AQA, `do ... until` in OCR) always run at least once, and stop when the condition becomes _true_. Python doesn't have these, but you can write one using `while True:` and `break`, as in [Lesson 3](../lessons/03-loops).

### Quick reference
All three columns below do the same thing. Both pseudocodes index arrays and strings from 0, like Python.

| Concept                     | Python                                | AQA pseudo-code                       | OCR Exam Reference Language             |
|-----------------------------|---------------------------------------|---------------------------------------|-----------------------------------------|
| Comment                     | `# comment`                           | `# comment`                           | `// comment`                            |
| Assignment                  | `x = 3`                               | `x ← 3`                               | `x = 3`                                 |
| Constant                    | `VAT = 0.2` (by convention only)      | `CONSTANT VAT ← 0.2`                  | `const vat = 0.2`                       |
| Output                      | `print("Hello")`                      | `OUTPUT 'Hello'`                      | `print("Hello")`                        |
| Input                       | `name = input()`                      | `name ← USERINPUT`                    | `name = input("Enter a name")`          |
| Equal / not equal           | `==` / `!=`                           | `=` / `≠`                             | `==` / `!=`                             |
| Less / greater or equal     | `<=` / `>=`                           | `≤` / `≥`                             | `<=` / `>=`                             |
| Logical operators           | `and`, `or`, `not`                    | `AND`, `OR`, `NOT`                    | `AND`, `OR`, `NOT`                      |
| Integer division            | `7 // 2`                              | `7 DIV 2`                             | `7 DIV 2`                               |
| Remainder                   | `7 % 2`                               | `7 MOD 2`                             | `7 MOD 2`                               |
| Power                       | `2 ** 3`                              | (not defined)                         | `2 ^ 3`                                 |
| String to integer           | `int("16")`                           | `STRING_TO_INT('16')`                 | `int("16")`                             |
| Integer to string           | `str(16)`                             | `INT_TO_STRING(16)`                   | `str(16)`                               |
| String to real (float)      | `float("16.3")`                       | `STRING_TO_REAL('16.3')`              | `float("16.3")` or `real("16.3")`       |
| Length of a string or array | `len(name)`                           | `LEN(name)`                           | `name.length`                           |
| Character code              | `ord("a")`                            | `CHAR_TO_CODE('a')`                   | `ASC("a")`                              |
| Character from code         | `chr(97)`                             | `CODE_TO_CHAR(97)`                    | `CHR(97)`                               |
| Upper / lower case          | `name.upper()` / `name.lower()`       | (not defined)                         | `name.upper` / `name.lower`             |
| First 3 characters          | `name[:3]`                            | `SUBSTRING(0, 2, name)`               | `name.left(3)`                          |
| Last 3 characters           | `name[-3:]`                           | `SUBSTRING(LEN(name) - 3, LEN(name) - 1, name)` | `name.right(3)`               |
| Random integer from 1 to 6  | `random.randint(1, 6)`                | `RANDOM_INT(1, 6)`                    | `random(1, 6)`                          |
| Create an array             | `primes = [2, 3, 5]`                  | `primes ← [2, 3, 5]`                  | `array primes[3]` (then assign each)    |
| 2D array element            | `board[1][0]`                         | `board[1][0]`                         | `board[1, 0]`                           |

### Loops
**Count-controlled (`for`) loops**, printing 1 to 10, then the odd numbers from 1 to 9:
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
```
// OCR
for i = 1 to 10
    print(i)
next i

for i = 1 to 9 step 2
    print(i)
next i
```

**Looping over the items in an array (or the characters in a string):**
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

**Condition-controlled loops** (`while`, and "repeat until"):
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
# AQA
IF score ≥ 70 THEN
   OUTPUT 'Merit'
ELSE IF score ≥ 50 THEN
   OUTPUT 'Pass'
ELSE
   OUTPUT 'Fail'
ENDIF
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

OCR's Exam Reference Language also has a `switch`/`case` statement. You can do the same thing in Python with `if`/`elif`/`else`, or with Python's `match` statement (Python 3.10 onwards), which these lessons don't cover.

### Subroutines
Both pseudocodes distinguish between _functions_ (which return a value) and _procedures_ (which don't). In Python, they're all just functions (see [Lesson 6](../lessons/06-functions)).
```python
# Python
def squared(number):
    return number ** 2

def greet(name):
    print("Hello " + name)
```
```
# AQA (both are written as SUBROUTINEs; a subroutine with RETURN is a function)
SUBROUTINE squared(number)
   RETURN number * number
ENDSUBROUTINE

SUBROUTINE greet(name)
   OUTPUT 'Hello ' + name
ENDSUBROUTINE
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

OCR also has a `global` keyword, for creating global variables. Python has a `global` keyword too, but it's used differently: inside a function, it lets you _change_ a global variable (we used it in [Lesson 16](../lessons/16-recursion-stacks-and-queues)).

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

### Files (OCR)
OCR's Exam Reference Language includes file handling. Compare it with [Lesson 9](../lessons/09-files):
```python
# Python
with open("sample.txt", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

with open("sample.txt", "a", encoding="utf-8") as file:
    file.write("Add new line\n")
```
```
// OCR
myFile = open("sample.txt")
while NOT myFile.endOfFile()
    print(myFile.readLine())
endwhile
myFile.close()

myFile = open("sample.txt")
myFile.writeLine("Add new line")
myFile.close()
```

Note that OCR's `writeLine` always adds the line to the _end_ of the file (like Python's `"a"` mode), and `newFile("myText.txt")` creates a new, empty file.

### Arrays vs lists
Both pseudocodes talk about _arrays_ rather than lists. As we saw in [Lesson 4](../lessons/04-lists), arrays are like Python lists, except that they usually have a fixed size, and can only store one type of data (OCR's specification says that "arrays only store a single data type"). In OCR's Exam Reference Language, you declare an array's size up front (`array names[5]`), and you access 2D arrays using a single pair of square brackets (`gameboard[1, 0]`, rather than Python's `gameboard[1][0]`).

## Which lessons do I need?
Everyone should work through [Lessons 0 to 10](../README.md#fundamentals), which cover the programming skills that all of these courses have in common: variables, selection, loops, lists and 2D lists, functions, strings, validation and exceptions, files, and searching and sorting algorithms. After that:
- **IB students:** classes and objects ([Lessons 11](../lessons/11-classes-and-objects) and [12](../lessons/12-inheritance-and-encapsulation)) are essential. HL students should also do [Lesson 16](../lessons/16-recursion-stacks-and-queues).
- **GCSE students:** the GCSE programming exams focus on the fundamentals, so Lessons 11 onwards are mostly extension material. They're well worth doing if you're thinking of taking Computer Science further, though! Dictionaries ([Lesson 13](../lessons/13-dictionaries-and-sets)) and testing ([Lesson 17](../lessons/17-testing)) are particularly useful for practical programming, and the ideas of normal, boundary and erroneous test data in Lesson 17 come up in GCSE exams.
- **Eduqas students:** the Eduqas specification asks you to use "lists, tuples and dictionaries", so make sure you do [Lesson 13](../lessons/13-dictionaries-and-sets) too.

## Sources
- AQA: [GCSE Computer Science specification](https://www.aqa.org.uk/subjects/computer-science/gcse/computer-science-8525/specification) (8525), and [Notes and guidance: Pseudo-code](https://filestore.aqa.org.uk/resources/computing/AQA-8525-NG-PC.PDF) (2024).
- OCR: [GCSE (9–1) Computer Science J277 specification](https://www.ocr.org.uk/qualifications/gcse/computer-science-j277-from-2020/), version 1, section 3c (OCR Exam Reference Language).
- Pearson Edexcel: [GCSE (9–1) Computer Science assessment overview](https://qualifications.pearson.com/content/dam/pdf/GCSE/Computer%20Science/2020/teaching-and-learning-materials/pearson-edexcel-computer-science-assessment-overview.pdf).
- Eduqas: [GCSE Computer Science specification](https://www.eduqas.co.uk/qualifications/computer-science/) (teaching from 2020), sections 2.2 and 3.2.
- IB: [Computer science subject brief](https://ibo.org/globalassets/new-structure/university-admission/pdfs/dp_comp_sci_subjectbrief_en.pdf), and summaries of the new guide (first assessment 2027), e.g. [AssessPrep](https://www.assessprep.com/blogs/ib-dp-computer-science-2027-changes).

---
[Contents](../README.md)
