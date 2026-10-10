# Lesson 16: Recursion, stacks and queues
In this lesson, we'll look at _recursion_, a powerful (and sometimes mind-bending!) way of solving problems by breaking them down into smaller versions of themselves. We'll then look at two simple but very important data structures, _stacks_ and _queues_, and see how a stack is what makes recursion work behind the scenes.

## Recursion
A _recursive_ function is a function that calls itself. That might sound like a recipe for an infinite loop, but it works as long as each call works on a _smaller_ version of the problem, and there's a version of the problem that's small enough to solve straight away.

The classic example is the _factorial_ of a number, written $n!$, which is the product of all the whole numbers from 1 to $n$. For example, $4! = 4 \times 3 \times 2 \times 1 = 24$. Notice that $4! = 4 \times 3!$, and in general, $n! = n \times (n - 1)!$. In other words, we can work out a factorial using a smaller factorial! We just need somewhere to stop: $1! = 1$.
```python
def factorial(n):
    if n <= 1:
        return 1                    # the base case
    return n * factorial(n - 1)     # the recursive case
```

Every recursive function needs two things:
1. A **base case**: a version of the problem that can be solved straight away, without recursion. This is what stops the recursion.
2. A **recursive case**: where the function calls itself on a smaller version of the problem, moving closer to the base case each time.

Here's what happens when we call `factorial(4)`:
```
factorial(4) = 4 * factorial(3)
                   factorial(3) = 3 * factorial(2)
                                      factorial(2) = 2 * factorial(1)
                                                         factorial(1) = 1
                                      factorial(2) = 2 * 1 = 2
                   factorial(3) = 3 * 2 = 6
factorial(4) = 4 * 6 = 24
```

Each call has to wait for the call inside it to finish before it can work out its own answer. Python keeps track of all these waiting calls on the _call stack_ (more on stacks below). If you forget the base case, or your recursive case doesn't get closer to it, the calls never finish, the call stack fills up, and Python stops with a `RecursionError: maximum recursion depth exceeded`. This is the recursive version of an infinite loop.

You can find this example in [`examples/factorial.py`](examples/factorial.py).

> [!NOTE]
> Anything you can do with recursion, you can also do with a loop (and vice versa). Recursion is often shorter and more elegant, especially for problems that are naturally "self-similar", like merge sort (which we saw in [Lesson 10](../10-searching-and-sorting)), or exploring a family tree or a maze. But it uses more memory, because of all the waiting calls on the call stack, and in Python it's usually a bit slower. For simple problems like factorials, a loop is usually the better choice in practice.

**Task 1:** Write two versions of a function that calculates $n!$: one using recursion, and one using a loop. Check that they give the same answers for $n$ from 0 to 10. What happens if you call the recursive version with $n = 5000$? [Solution](solutions/task1_factorial.py)

**Task 2:** Write recursive functions to: [Solution](solutions/task2_recursion_practice.py)
1. Calculate `power(base, exponent)`, using the fact that $b^e = b \times b^{e-1}$ (and $b^0 = 1$).
2. Add up the digits of a whole number, e.g. `sum_digits(1234)` should return `10`. Hint: `n % 10` gives the last digit, and `n // 10` removes it.
3. Reverse a string, e.g. `reverse("hello")` should return `"olleh"`. Hint: the reverse of a string is the reverse of everything after its first character, followed by its first character.

**Task 3:** The _Fibonacci sequence_ starts 0, 1, 1, 2, 3, 5, 8, 13, ..., where each number is the sum of the two before it. So $F(0) = 0$, $F(1) = 1$, and $F(n) = F(n-1) + F(n-2)$. Write a recursive function `fibonacci(n)` and use it to print the first 20 Fibonacci numbers. Then add a global counter to count how many times the function gets called while calculating `fibonacci(25)`. Why is it so many? [Solution](solutions/task3_fibonacci.py)

**Task 4:** Write a recursive version of binary search (see [Lesson 10](../10-searching-and-sorting)). Your function should take the list, the target, and the `low` and `high` indexes of the section of the list to search. [Solution](solutions/task4_recursive_binary_search.py)

## Stacks
A _stack_ is a collection where items are added and removed from the same end, called the _top_. Think of a stack of plates: you can only put a new plate on the top, and you can only take the top plate off. This means the last item added is always the first one removed, so stacks are sometimes called _LIFO_ (last in, first out) structures. Stacks have a few standard operations:
- **push:** add an item to the top.
- **pop:** remove the item from the top and return it.
- **peek** (or **top**): return the item on the top, without removing it.
- **is empty:** check whether the stack is empty.

Stacks are everywhere in computing. The "undo" button in most programs uses a stack of your recent actions: undoing pops the most recent one. Your web browser's "back" button uses a stack of the pages you've visited. And, as we saw above, Python uses a stack to keep track of function calls.

In Python, a list makes a perfectly good stack: `.append()` pushes an item onto the end (the top), and `.pop()` removes it again:
```python
stack = []
stack.append("a")  # push
stack.append("b")
stack.append("c")
print(stack.pop())  # pops "c": the last item pushed
print(stack[-1])    # peeks at "b", without removing it
```

**Task 5:** Write a `Stack` class with methods `push(item)`, `pop()`, `peek()`, `is_empty()` and `__len__`. Store the items in a list. `pop` and `peek` should raise an `IndexError` with a helpful message if the stack is empty. Test it by pushing some items and popping them all off again. [Solution](solutions/task5_stack.py)

**Task 6:** A classic use of a stack is checking whether the brackets in some code or maths are balanced. For example, `(a[b]{c})` is balanced, but `(a[b)]` and `((a)` aren't. The algorithm is: go through the string one character at a time. Whenever you see an opening bracket, push it onto a stack. Whenever you see a closing bracket, pop the top item from the stack and check it's the matching opening bracket. At the end, the stack should be empty. Use your `Stack` class to write a function `is_balanced(text)`. [Solution](solutions/task6_balanced_brackets.py)

## Queues
A _queue_ is like a queue of people waiting to pay in a shop: items join at the _back_, and leave from the _front_. So the first item added is always the first one removed, which is why queues are called _FIFO_ (first in, first out) structures. The standard operations are:
- **enqueue:** add an item to the back.
- **dequeue:** remove the item from the front and return it.
- **peek:** return the item at the front, without removing it.
- **is empty:** check whether the queue is empty.

Queues are used whenever things need to be dealt with in the order they arrived: documents waiting to be printed, keys you've pressed that a program hasn't dealt with yet, players waiting to join an online game, and so on.

You _could_ use a list as a queue, using `.append()` to enqueue and `.pop(0)` to dequeue. But `.pop(0)` is slow for long lists, because every other item has to shuffle along one place. Instead, Python's `collections` module provides a `deque` (short for "double-ended queue", and pronounced "deck"), which can add and remove items quickly at either end:
```python
from collections import deque

queue = deque()
queue.append("Ada")      # enqueue
queue.append("Alan")
queue.append("Grace")
print(queue.popleft())   # dequeues "Ada": the first item added
print(queue[0])          # peeks at "Alan", without removing him
```

You can find the stack and queue examples in [`examples/stacks_and_queues.py`](examples/stacks_and_queues.py).

**Task 7:** Write a `Queue` class (using a `deque` to store the items) with methods `enqueue(item)`, `dequeue()`, `peek()`, `is_empty()` and `__len__`. Then use it to simulate a printer queue: add five documents to the queue, then "print" them one at a time (in the right order), printing how many documents are still waiting after each one. [Solution](solutions/task7_queue.py)

**⭐ Task 8:** Your `fibonacci` function from Task 3 is slow because it calculates the same values over and over again. Fix this using _memoisation_: store each answer in a dictionary the first time you calculate it, and look it up instead of recalculating it next time. How many calls does `fibonacci(25)` take now? How big an `n` can you manage? [Solution](solutions/task8_memoised_fibonacci.py)

**⭐ Task 9:** In the _Towers of Hanoi_ puzzle, there are three pegs, and a tower of $n$ discs of different sizes on the first peg, with the largest at the bottom. The aim is to move the whole tower to the third peg, moving one disc at a time, without ever putting a larger disc on top of a smaller one. The recursive solution is surprisingly short: to move $n$ discs from peg A to peg C, move the top $n - 1$ discs from A to B (using C as a spare), move the largest disc from A to C, then move the $n - 1$ discs from B to C (using A as a spare). Write a recursive function `hanoi(n, source, target, spare)` that prints each move needed. How many moves does it take for $n = 3$, 4 and 5? Can you spot the pattern? [Solution](solutions/task9_towers_of_hanoi.py)

**⭐ Task 10:** Many languages don't have anything like `deque`, and queues are instead built using a fixed-size array, called a _circular queue_. The array has a `front` index (where the next item will be dequeued from) and a `rear` index (where the next item will be enqueued), and both wrap around to the start of the array when they reach the end (hint: `%`!). Write a `CircularQueue` class that stores its items in a list of a fixed `capacity` (e.g. `[None] * capacity`), with methods `enqueue`, `dequeue`, `is_empty` and `is_full`. Test it by filling it up, emptying it partly, then filling it again, so that the indexes wrap around. [Solution](solutions/task10_circular_queue.py)

---
[← Previous: Lesson 15](../15-type-hints-and-dataclasses) | [Contents](../../README.md) | [Next: Lesson 17 →](../17-testing)
