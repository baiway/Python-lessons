# Lesson 13: Tuples, dictionaries and sets
Lists are great, but they aren't always the best tool for the job. In this lesson, we'll meet three more of Python's built-in collection types: _tuples_, _dictionaries_ and _sets_. We'll finish off with _comprehensions_, a neat shorthand for building lists, dictionaries and sets.

## Tuples
A _tuple_ is like a list that can't be changed once it's been created (just like strings, tuples are _immutable_). We create tuples using round brackets instead of square brackets:
```python
>>> point = (3, 4)
>>> point[0]
3
>>> len(point)
2
>>> point[0] = 5
TypeError: 'tuple' object does not support item assignment
```

You've actually used tuples already, without realising it! When a function returns several values (as in [Lesson 6](../06-functions)), it's really returning a single tuple, which we then _unpack_ into separate variables:
```python
def min_and_max(numbers):
    return min(numbers), max(numbers)  # the same as `return (min(numbers), max(numbers))`

lowest, highest = min_and_max([4, 8, 1, 9])  # unpacking the tuple (1, 9)
```

Tuples are useful for small, fixed groups of values that belong together, like the coordinates of a point, or a date. Because they can't be changed, you can be sure that nobody changes them by accident. They can also be used as dictionary keys and stored in sets, which lists can't (see below).

## Dictionaries
In a list, each value is stored at a numbered position: its index. A _dictionary_ (or `dict`) instead stores each value under a _key_, which you choose. Each key is linked to exactly one value, which is why dictionaries are sometimes called _maps_ or _associative arrays_ in other languages. We create dictionaries using curly brackets, with a colon between each key and its value:
```python
ages = {"Ada": 36, "Alan": 41, "Grace": 85}
```

We can then look up a value using its key, in the same way that we'd look up an item in a list using its index:
```python
>>> ages["Alan"]
41
>>> ages["Tim"]
KeyError: 'Tim'
```

Asking for a key that isn't in the dictionary gives a `KeyError`. To avoid this, you can check whether the key is there first using `in`, or use the `.get` method, which gives back `None` (or a default value of your choice) instead of raising an exception:
```python
>>> "Tim" in ages
False
>>> print(ages.get("Tim"))
None
>>> ages.get("Tim", 0)
0
```

To add a new key, or change the value of an existing one, just assign to it. To remove a key, use `del`:
```python
ages["Tim"] = 71    # adds a new key
ages["Ada"] = 37    # changes an existing value
del ages["Grace"]   # removes a key (and its value)
print(ages)         # prints {'Ada': 37, 'Alan': 41, 'Tim': 71}
```

Keys must be unique: if you assign to a key that already exists, the old value is replaced. Keys must also be immutable, so you can use strings, numbers and tuples as keys, but not lists. Values can be anything at all, including lists and other dictionaries.

### Looping over dictionaries
Looping over a dictionary gives you its keys. You can also use the `.values()` method to loop over the values, or `.items()` to loop over the keys _and_ values together:
```python
for name in ages:
    print(name)

for age in ages.values():
    print(age)

for name, age in ages.items():
    print(f"{name} is {age} years old")
```

Dictionaries remember the order in which keys were added, so these loops always go through the keys in that order.

### Counting with dictionaries
A very common use of dictionaries is counting things. The pattern looks like this:
```python
words = ["the", "cat", "sat", "on", "the", "mat", "the", "end"]

counts = {}
for word in words:
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1

print(counts)  # prints {'the': 3, 'cat': 1, 'sat': 1, 'on': 1, 'mat': 1, 'end': 1}
```

You can find all of these examples in [`examples/dictionaries.py`](examples/dictionaries.py).

**Task 1:** Write a phone book program. Store the phone book in a dictionary, with names as keys and phone numbers (as strings) as values. Your program should repeatedly ask the user whether they want to add a number, look up a number, delete a number, list everyone (in alphabetical order), or quit. Make sure your program doesn't crash if the user looks up or deletes someone who isn't in the phone book. [Solution](solutions/task1_phone_book.py)

**Task 2:** Write a program that reads [`poem.txt`](data/poem.txt) and counts how many times each word appears. Ignore capital letters and punctuation (hint: `.strip(".,:;!?-")` removes those characters from the start and end of a string). Print the five most common words, along with how many times each appears. Hint: `sorted(counts.items(), key=...)` gives you a list of `(word, count)` tuples, which you can sort by count, as in [Lesson 10](../10-searching-and-sorting). [Solution](solutions/task2_word_frequency.py)

**Task 3:** In Scrabble, each letter is worth a certain number of points, given below. Store these in a dictionary, and write a function `scrabble_score(word)` that returns the score for a word. Test it on a few words: for example, `"python"` should score 14. [Solution](solutions/task3_scrabble.py)

| Points | Letters                       |
|--------|-------------------------------|
| 1      | A, E, I, O, U, L, N, S, T, R  |
| 2      | D, G                          |
| 3      | B, C, M, P                    |
| 4      | F, H, V, W, Y                 |
| 5      | K                             |
| 8      | J, X                          |
| 10     | Q, Z                          |

**Task 4:** A list of dictionaries is a common way of storing records, where each dictionary describes one thing. (This is what you get when you read data from many web services, for example.) Using the list below, write a program that prints each student's name and mean score, and the names of all the students in Year 10. [Solution](solutions/task4_student_records.py)
```python
students = [
    {"name": "Ada", "year": 10, "scores": [72, 85, 64]},
    {"name": "Alan", "year": 11, "scores": [90, 78, 88]},
    {"name": "Grace", "year": 10, "scores": [65, 70, 71]},
    {"name": "Tim", "year": 11, "scores": [81, 93, 77]},
]
```

> [!NOTE]
> You might be wondering when to use a list of dictionaries, and when to use a list of objects (as in [Lesson 11](../11-classes-and-objects)). Dictionaries are quick and easy, but nothing stops you from misspelling a key, or forgetting one. Classes take a bit more work to set up, but they can have methods, and VS Code can spot mistakes for you. As a rule of thumb, if the data is just passing through your program (e.g. you've read it from a file, and you're going to print it), a dictionary is fine. If it's a central part of your program, use a class. We'll see a quick way of writing classes like this in [Lesson 15](../15-type-hints-and-dataclasses).

## Sets
A _set_ is an unordered collection of _unique_ items: each item can only appear once. Sets are created using curly brackets (like dictionaries, but without the colons), or by passing a list (or any other collection) to `set`:
```python
>>> colours = {"red", "green", "blue"}
>>> colours.add("red")  # already in the set, so nothing happens
>>> colours
{'green', 'red', 'blue'}
>>> set(["a", "b", "a", "c", "b"])
{'a', 'c', 'b'}
```

Notice that sets don't keep items in any particular order, so you can't use an index to get an item out of a set. (To create an _empty_ set, you have to write `set()`, because `{}` creates an empty dictionary!)

Sets are very good at two things. Firstly, checking whether something is in a set (using `in`) is _much_ faster than checking whether it's in a list, especially for big collections. Secondly, sets support the same operations as sets in maths:

| Operation            | Operator | Meaning                                      | `{1, 2, 3}` and `{2, 3, 4}` |
|----------------------|----------|----------------------------------------------|-----------------------------|
| Union                | `a \| b` | Items in `a` or `b` (or both)                | `{1, 2, 3, 4}`              |
| Intersection         | `a & b`  | Items in both `a` and `b`                    | `{2, 3}`                    |
| Difference           | `a - b`  | Items in `a` but not `b`                     | `{1}`                       |
| Symmetric difference | `a ^ b`  | Items in `a` or `b`, but not both            | `{1, 4}`                    |

You can find these examples in [`examples/sets.py`](examples/sets.py).

**Task 5:** Two friends have each written a list of their favourite films (below). Use sets to print: the films they both like, the films that at least one of them likes, the films that only Ada likes, and the films that only one of them likes. [Solution](solutions/task5_favourite_films.py)
```python
ada_films = ["Spirited Away", "Paddington 2", "The Matrix", "Up", "Arrival"]
alan_films = ["The Matrix", "Inception", "Up", "Hidden Figures", "Arrival"]
```

**Task 6:** A _pangram_ is a sentence that contains every letter of the alphabet at least once, like "The quick brown fox jumps over the lazy dog". Write a function `is_pangram(sentence)` that uses a set to check whether a sentence is a pangram. If it isn't, print the letters that are missing (in alphabetical order). Hint: the string `"abcdefghijklmnopqrstuvwxyz"` might come in handy. [Solution](solutions/task6_pangrams.py)

## Comprehensions
We've often built up a list by starting with an empty list and appending to it inside a loop:
```python
squares = []
for i in range(1, 6):
    squares.append(i**2)
```

Python has a shorthand for this, called a _list comprehension_:
```python
squares = [i**2 for i in range(1, 6)]
```

You can read this as "make a list of `i**2`, for each `i` in `range(1, 6)`". You can also add an `if` at the end to only include some of the items:
```python
evens = [i for i in range(1, 21) if i % 2 == 0]
long_words = [word for word in words if len(word) > 5]
```

There are dictionary and set comprehensions too:
```python
lengths = {word: len(word) for word in ["cat", "giraffe", "emu"]}  # {'cat': 3, 'giraffe': 7, 'emu': 3}
first_letters = {word[0] for word in ["apple", "avocado", "banana"]}  # {'a', 'b'}
```

Comprehensions are neat, but don't get carried away! If a comprehension doesn't fit comfortably on one line, or you have to read it three times to understand it, a normal loop is probably clearer.

You can find these examples in [`examples/comprehensions.py`](examples/comprehensions.py).

**Task 7:** Use comprehensions to create: [Solution](solutions/task7_comprehensions.py)
1. A list of the cubes of the numbers from 1 to 10.
2. A list of the multiples of 7 below 100.
3. A list of the words in the sentence "the quick brown fox jumps over the lazy dog" that contain the letter "o".
4. A dictionary mapping each of the numbers from 1 to 10 to its square.
5. A set of the vowels that appear in the word "comprehension".

**⭐ Task 8:** Two words are anagrams if they contain the same letters (as in [Lesson 7](../07-strings) Task 9). Write a program that groups the words in the list below into groups of anagrams, and prints each group that contains more than one word. Hint: use a dictionary whose keys are the letters of a word in alphabetical order (e.g. `"".join(sorted("listen"))` is `"eilnst"`), and whose values are lists of words. [Solution](solutions/task8_anagram_groups.py)
```python
words = ["listen", "silent", "enlist", "google", "inlets", "banana", "stone", "tones", "notes", "onset", "elbow", "below"]
```

**⭐ Task 9:** Store the Morse code alphabet (below) in a dictionary, and write functions to encode a message into Morse code (with a space between letters and ` / ` between words) and decode it again. Hint: you can create a dictionary that goes the other way (from Morse code back to letters) using a dictionary comprehension. [Solution](solutions/task9_morse_code.py)
```python
morse = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",
}
```

---
[← Previous: Lesson 12](../12-inheritance-and-encapsulation) | [Contents](../../README.md) | [Next: Lesson 14 →](../14-packages)
