# Lesson 4: Lists
So far, each of our variables has stored a single value. Very often though, we want to store a whole collection of values — a list of names, a set of test scores, the items in a shopping basket, etc. In Python, we can do this using a _list_.

## Creating lists
We create a list by putting values inside square brackets `[]`, separated by commas:
```python
fruits = ["apple", "banana", "cherry"]
scores = [72, 85, 64, 90]
empty = []
```

Lists can contain any type of value (even other lists — we'll see this in [Lesson 5](../05-2d-lists)!), and the values don't all have to be the same type, although they usually are. We can find out how many items are in a list using `len`:
```python
>>> len(fruits)
3
>>> len(empty)
0
```

> [!NOTE]
> If you've written pseudocode before, you might have come across _arrays_. Arrays are very similar to lists, but they usually have a fixed size, and every item in an array must have the same type. Python lists are more flexible: they can grow and shrink, and they can hold a mixture of types. In most cases, you can use a Python list wherever pseudocode uses an array.

## Indexing
Each item in a list has a position, called its _index_. We can get an item out of a list by putting its index in square brackets after the list's name. In Python (and most other programming languages), indexes start at **0**, not 1. (This is why these lessons start at Lesson 0!)
```python
>>> fruits = ["apple", "banana", "cherry"]
>>> fruits[0]
'apple'
>>> fruits[1]
'banana'
>>> fruits[2]
'cherry'
>>> fruits[3]
IndexError: list index out of range
```

So the _first_ item is at index `0`, and the _last_ item is at index `len(fruits) - 1`. Asking for an index that doesn't exist gives an `IndexError`. Python also lets you use negative indexes to count backwards from the end of the list:
```python
>>> fruits[-1]
'cherry'
>>> fruits[-2]
'banana'
```

We can also use indexing to _change_ an item in a list:
```python
>>> fruits[1] = "blueberry"
>>> fruits
['apple', 'blueberry', 'cherry']
```

## Adding and removing items
Lists have lots of built-in _methods_ (functions that belong to the list) for adding and removing items. To use a method, write the name of the list, a dot, then the name of the method. The most useful ones are:

| Method                 | What it does                                          | Example                   |
|------------------------|-------------------------------------------------------|---------------------------|
| `.append(item)`        | Adds `item` to the end of the list                    | `fruits.append("kiwi")`   |
| `.insert(index, item)` | Inserts `item` at position `index`                    | `fruits.insert(0, "fig")` |
| `.remove(item)`        | Removes the first occurrence of `item`                | `fruits.remove("apple")`  |
| `.pop()`               | Removes the last item and gives it back to you        | `last = fruits.pop()`     |
| `.pop(index)`          | Removes the item at position `index` and gives it back| `first = fruits.pop(0)`   |
| `.index(item)`         | Gives the index of the first occurrence of `item`     | `fruits.index("cherry")`  |
| `.count(item)`         | Counts how many times `item` appears                  | `scores.count(90)`        |
| `.sort()`              | Sorts the list (smallest to largest, or A to Z)       | `scores.sort()`           |
| `.reverse()`           | Reverses the order of the list                        | `scores.reverse()`        |

You can also use the `in` keyword (which we first saw in [Lesson 2](../02-conditionals)) to check whether something is in a list:
```python
if "apple" in fruits:
    print("We have apples!")
```

**Task 1:** Write a program that:
1. Creates a list called `shopping` containing `"eggs"`, `"milk"` and `"bread"`.
2. Prints the first item and the last item in the list.
3. Adds `"cheese"` to the end of the list, then removes `"milk"`.
4. Prints the whole list and how many items it contains.

[Solution](solutions/task1_shopping_list.py)

## Slicing
We can get a section of a list (called a _slice_) using `list[start:stop]`. Just like with `range`, the slice starts at `start` and stops _just before_ `stop`. If you leave out `start` or `stop`, Python starts from the beginning or goes all the way to the end. You can also add a step, just like `range`.
```python
>>> numbers = [10, 20, 30, 40, 50, 60]
>>> numbers[1:4]
[20, 30, 40]
>>> numbers[:3]
[10, 20, 30]
>>> numbers[3:]
[40, 50, 60]
>>> numbers[::2]
[10, 30, 50]
>>> numbers[::-1]
[60, 50, 40, 30, 20, 10]
```

**Task 2:** Create a list containing the twelve months of the year. Then, using slicing, print: [Solution](solutions/task2_months.py)
1. The first three months.
2. The last three months.
3. The summer months (June, July and August).
4. Every other month, starting from January.
5. All the months in reverse order.

## Looping over lists
In [Lesson 3](../03-loops), we saw that we can use a `for` loop to go through each item in a list:
```python
for fruit in fruits:
    print(fruit)
```

Sometimes we need to know the _index_ of each item as well as the item itself. There are two ways to do this. The first is to loop over the indexes using `range` and `len`:
```python
for i in range(len(fruits)):
    print(f"Item {i} is {fruits[i]}")
```

The second, which is a bit neater, is to use `enumerate`. This gives you the index _and_ the item each time around the loop:
```python
for i, fruit in enumerate(fruits):
    print(f"Item {i} is {fruit}")
```

A common pattern is to start with an empty list and add items to it inside a loop:
```python
squares = []
for i in range(1, 6):
    squares.append(i**2)
print(squares)  # prints [1, 4, 9, 16, 25]
```

Python also has some built-in functions that work on lists of numbers: `sum`, `min`, `max` and `sorted` (which gives back a _new_, sorted copy of the list, rather than sorting the original).

**Task 3:** The list below contains the maximum daily temperatures (in °C) in London during one week. Without using `sum`, `min` or `max`, use a `for` loop to work out the total, the mean, the highest and the lowest temperature. Then check your answers using `sum`, `min` and `max`. [Solution](solutions/task3_temperatures.py)
```python
temperatures = [18.2, 21.5, 19.8, 23.1, 25.4, 22.0, 17.6]
```

**Task 4:** A _linear search_ looks through a list one item at a time until it finds what it's looking for. Write a program that asks the user for a name and searches the list below for it. If the name is in the list, print its index; otherwise, print a message saying it wasn't found. Don't use `in` or `.index` — the point is to write the search yourself! [Solution](solutions/task4_linear_search.py)
```python
names = ["Ada", "Alan", "Grace", "Tim", "Margaret", "Linus", "Guido"]
```

**Task 5:** Write a program that asks the user to enter numbers one at a time, stopping when they type `done`. Store the numbers in a list, then print: how many numbers were entered, their mean, and all the numbers that were above the mean. [Solution](solutions/task5_above_average.py)

**Task 6:** Write a program that creates a reversed copy of a list _without_ using `.reverse()`, `reversed` or `[::-1]`. Hint: start with an empty list and loop over the original list. [Solution](solutions/task6_reverse.py)

**Task 7:** Write a program that takes the list below and creates a new list containing each item only once (i.e. removes the duplicates), keeping the items in the same order. [Solution](solutions/task7_remove_duplicates.py)
```python
colours = ["red", "blue", "red", "green", "blue", "blue", "yellow", "red"]
```

## Be careful when copying lists!
This catches everyone out at some point. Look at the code below and predict what it prints before you run it.
```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
```

You might expect it to print `[1, 2, 3]`, but it actually prints `[1, 2, 3, 4]`! This is because `b = a` does not make a copy of the list. Instead, it makes `b` _another name for the same list_. Any change you make using `b` will also show up when you look at `a`, because they're the same thing. If you want a separate copy, use `.copy()`:
```python
a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a)  # prints [1, 2, 3]
print(b)  # prints [1, 2, 3, 4]
```

You can find this example in [`examples/copying_lists.py`](examples/copying_lists.py).

## Static and dynamic data structures
Earlier, I mentioned that many languages use _arrays_, which have a fixed size, rather than lists, which can grow and shrink. Computer scientists call these _static_ and _dynamic_ data structures:
- A **static** data structure has a fixed size, which is decided when it's created. The computer sets aside one block of memory for it straight away, and it never changes. This makes static data structures simple and fast (the computer can work out exactly where each item is stored, so looking an item up by its index is very quick), but you have to know in advance how much space you'll need. If you guess too small, you run out of space; if you guess too big, you waste memory.
- A **dynamic** data structure can change size while your program is running, so you don't need to know how big it will get in advance. The price you pay is a bit of extra work behind the scenes, and usually a bit of extra memory.

Python lists are dynamic. Behind the scenes, a list is stored in a block of memory with some spare space at the end. When you `.append` an item, Python normally just puts it in the spare space, which is very quick. But when the spare space runs out, Python has to find a new, bigger block of memory and copy every item across to it, which takes longer. (Python makes the new block quite a bit bigger each time, so this doesn't happen very often.) We'll meet another dynamic data structure, the _linked list_, in [Lesson 18](../18-linked-lists).

**⭐ Task 8:** Write a lottery program. The computer should pick 6 _different_ random numbers between 1 and 59 (don't use `random.sample` — use a `while` loop and `in` to avoid picking the same number twice). The user should then enter 6 numbers. Print the computer's numbers (sorted), the user's numbers, and how many numbers the user matched. [Solution](solutions/task8_lottery.py)

**⭐ Task 9:** Write a program that finds the _second_ largest number in a list without sorting it and without using `max`. Can you do it by looping over the list only once? Make sure it works for lists like `[5, 5, 3]` (where the answer should be `3`). [Solution](solutions/task9_second_largest.py)

---
[← Previous: Lesson 3](../03-loops) | [Contents](../../README.md) | [Next: Lesson 5 →](../05-2d-lists)
