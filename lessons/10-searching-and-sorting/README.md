# Lesson 10: Searching and sorting algorithms
An _algorithm_ is a precise, step-by-step set of instructions for solving a problem. Two of the most common problems in computer science are _searching_ (finding an item in a list) and _sorting_ (putting a list in order). There are lots of algorithms for doing each of these, and some are much faster than others. In this lesson, we'll write some of the classic ones ourselves.

You will rarely need to write your own searching or sorting algorithms in real programs (Python's built-in `in`, `.index()` and `sorted` are faster than anything we'll write here!). But understanding how they work, and why some are faster than others, is a big part of computer science, and these algorithms come up in exams _all the time_.

## Linear search
We've already written a _linear search_ in [Lesson 4](../04-lists) and [Lesson 6](../06-functions): start at the beginning of the list, and check each item in turn until you either find what you're looking for or reach the end.
```python
def linear_search(items, target):
    """Returns the index of `target` in `items`, or -1 if it isn't there"""
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1
```

Linear search is simple, and it works on any list, sorted or not. But it can be slow: if the list contains 1,000,000 items and the one we want is at the end (or isn't there at all), we have to check all 1,000,000 of them.

**Task 1:** Change the `linear_search` function above so that it also counts how many comparisons it makes (i.e. how many times it checks `items[i] == target`), and returns both the index and the number of comparisons. Test it on `list(range(1, 1001))` with a few different targets, including one that isn't in the list. [Solution](solutions/task1_linear_search.py)

## Binary search
If the list is already _sorted_, we can do much better. Think about how you'd look up a word in a dictionary: you wouldn't start at "aardvark" and read every word until you found the one you wanted! Instead, you'd open it somewhere in the middle, see whether your word comes before or after that page, and throw away the half you don't need. Then you'd do the same thing again with the half that's left, and so on.

This is exactly how _binary search_ works:
1. Look at the item in the middle of the list.
2. If it's the item we're looking for, we're done!
3. If the item we're looking for is _smaller_ than the middle item, it must be in the left half (because the list is sorted), so throw away the right half.
4. If it's _bigger_, it must be in the right half, so throw away the left half.
5. Repeat with the half that's left, until either we find the item or there's nothing left to search.

In code, we don't actually throw anything away. Instead, we keep track of the section of the list we're still searching using two indexes, `low` and `high`:
```python
def binary_search(items, target):
    """Returns the index of `target` in the sorted list `items`, or -1 if it
    isn't there"""
    low = 0
    high = len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target:
            return mid
        elif target < items[mid]:
            high = mid - 1  # search the left half
        else:
            low = mid + 1   # search the right half
    return -1
```

Each comparison halves the size of the section we're searching. So even for a list of 1,000,000 items, binary search never needs more than 20 comparisons!

> [!WARNING]
> Binary search _only_ works on sorted lists. If the list isn't sorted, it will happily give you the wrong answer without any error.

You can find both search functions in [`examples/searching.py`](examples/searching.py).

**Task 2:** Add a comparison counter to `binary_search`, as you did for `linear_search` in Task 1. Then compare the number of comparisons each algorithm makes when searching `list(range(1, 1_000_001))` for `1`, `500_000`, `999_999` and `0`. (Python lets you write big numbers with underscores to make them easier to read: `1_000_000` is the same as `1000000`.) [Solution](solutions/task2_binary_search.py)

## Bubble sort
_Bubble sort_ is one of the simplest sorting algorithms. It works by going through the list, comparing each pair of neighbouring items, and swapping them if they're in the wrong order. Each time through the list is called a _pass_. After the first pass, the largest item will have "bubbled up" to the end of the list. After the second pass, the second largest will be in the right place, and so on. We keep doing passes until we get through a whole pass without making any swaps, at which point the list must be sorted.

Here's what happens when we bubble sort the list `[5, 1, 4, 2, 8]`:

| Pass | Comparisons                                                  | List after pass   |
|------|--------------------------------------------------------------|-------------------|
| 1    | 5 > 1, swap. 5 > 4, swap. 5 > 2, swap. 5 < 8, no swap.       | `[1, 4, 2, 5, 8]` |
| 2    | 1 < 4, no swap. 4 > 2, swap. 4 < 5, no swap. 5 < 8, no swap. | `[1, 2, 4, 5, 8]` |
| 3    | No swaps, so the list is sorted!                             | `[1, 2, 4, 5, 8]` |

To swap two items in a list in Python, you can use the neat trick below (which works because of the "returning multiple values" trick we saw in [Lesson 6](../06-functions)):
```python
items[i], items[i + 1] = items[i + 1], items[i]
```

**Task 3:** On paper, trace a bubble sort of the list `[6, 2, 9, 4, 1]`, writing down the list after each pass, like in the table above. How many passes does it take? [Solution](solutions/task3_bubble_sort_trace.md)

**Task 4:** Write a function `bubble_sort(items)` that sorts a list using bubble sort. Make it print the list after each pass, and check that it matches your answer to Task 3. Your function should stop as soon as a pass makes no swaps. [Solution](solutions/task4_bubble_sort.py)

## Selection sort and insertion sort
Two other simple sorting algorithms are _selection sort_ and _insertion sort_. Both of them build up a sorted section at the start of the list, one item at a time.

**Selection sort:** find the smallest item in the list and swap it with the first item. Then find the smallest item in the rest of the list (ignoring the first item, which is now in the right place) and swap it with the second item. Keep going until you reach the end of the list.

**Insertion sort:** this is how most people sort a hand of playing cards. Take the second item and _insert_ it in the right place among the items before it (so the first two items are sorted). Then take the third item and insert it in the right place among the first two, and so on. To insert an item, keep moving it one place to the left while the item before it is bigger.

| Algorithm      | `[5, 1, 4, 2, 8]` after each step                                                    |
|----------------|--------------------------------------------------------------------------------------|
| Selection sort | `[1, 5, 4, 2, 8]` → `[1, 2, 4, 5, 8]` → `[1, 2, 4, 5, 8]` → `[1, 2, 4, 5, 8]`         |
| Insertion sort | `[1, 5, 4, 2, 8]` → `[1, 4, 5, 2, 8]` → `[1, 2, 4, 5, 8]` → `[1, 2, 4, 5, 8]`         |

**Task 5:** Write a function `selection_sort(items)` that sorts a list using selection sort. [Solution](solutions/task5_selection_sort.py)

**Task 6:** Write a function `insertion_sort(items)` that sorts a list using insertion sort. [Solution](solutions/task6_insertion_sort.py)

## Merge sort
Bubble, selection and insertion sort are all fairly slow on big lists, because they compare each item with lots of other items. _Merge sort_ is much faster. It's based on a simple idea: it's very easy to _merge_ two lists that are already sorted into one sorted list. You just keep comparing the first items of each list, and take whichever is smaller.

Merge sort works like this:
1. Split the list in half, then split each half in half, and so on, until every list contains just one item. (A list containing one item is always sorted!)
2. Merge the lists back together in pairs, keeping them sorted, until there's only one list left.

```
              [6, 2, 9, 4, 1, 8, 3, 7]
             /                        \
      [6, 2, 9, 4]                [1, 8, 3, 7]          split
       /       \                   /       \
   [6, 2]     [9, 4]           [1, 8]     [3, 7]        split
   /   \      /   \            /   \      /   \
 [6]   [2]  [9]   [4]        [1]   [8]  [3]   [7]       split
   \   /      \   /            \   /      \   /
   [2, 6]     [4, 9]           [1, 8]     [3, 7]        merge
       \       /                   \       /
      [2, 4, 6, 9]                [1, 3, 7, 8]          merge
             \                        /
              [1, 2, 3, 4, 6, 7, 8, 9]                  merge
```

**Task 7:** Write a function `merge(left, right)` that takes two _sorted_ lists and returns a single sorted list containing all of their items. For example, `merge([2, 4, 6, 9], [1, 3, 7, 8])` should return `[1, 2, 3, 4, 6, 7, 8, 9]`. Hint: use two indexes, one for each list. Don't forget about the items left over when you reach the end of one of the lists! [Solution](solutions/task7_merge.py)

## Sorting in real life
In real programs, you should use Python's built-in sorting tools, which are very fast:
- `sorted(items)` gives back a new sorted list, and leaves `items` unchanged.
- `items.sort()` sorts `items` itself, and gives back nothing (`None`).

Both of these accept two useful keyword arguments. `reverse=True` sorts from largest to smallest. `key` lets you choose _what_ to sort by: you give it a function, and Python sorts the items by whatever that function returns. For example, to sort a list of words by their length, we can use `key=len`:
```python
>>> words = ["banana", "fig", "apple", "kiwi"]
>>> sorted(words)
['apple', 'banana', 'fig', 'kiwi']
>>> sorted(words, key=len)
['fig', 'kiwi', 'apple', 'banana']
>>> sorted(words, key=len, reverse=True)
['banana', 'apple', 'kiwi', 'fig']
```

**Task 8:** The 2D list below stores some players' names and scores. Use `sorted` with `key` to print the players from highest to lowest score. Hint: write a function `get_score(player)` that returns a player's score, and pass it as the `key`. (Notice that we pass the function itself, `get_score`, _without_ brackets. We're not calling it ourselves: `sorted` calls it for us, once for each item.) [Solution](solutions/task8_sort_with_key.py)
```python
players = [["Ada", 4300], ["Margaret", 9800], ["Guido", 7200], ["Linus", 8650]]
```

## How fast are these algorithms?
Computer scientists compare algorithms by thinking about how the number of steps grows as the input gets bigger. The table below shows the (worst-case) number of comparisons each algorithm needs for a list of $n$ items.

| Algorithm      | Comparisons (roughly) | $n = 10$ | $n = 1{,}000$ | $n = 1{,}000{,}000$ |
|----------------|-----------------------|----------|---------------|---------------------|
| Linear search  | $n$                   | 10       | 1,000         | 1,000,000           |
| Binary search  | $\log_2 n$            | 4        | 10            | 20                  |
| Bubble sort    | $n^2$                 | 100      | 1,000,000     | 1,000,000,000,000   |
| Selection sort | $n^2$                 | 100      | 1,000,000     | 1,000,000,000,000   |
| Insertion sort | $n^2$                 | 100      | 1,000,000     | 1,000,000,000,000   |
| Merge sort     | $n \log_2 n$          | 33       | 10,000        | 20,000,000          |

Notice how much the gap grows as $n$ gets bigger! Even though bubble sort is easier to write, merge sort is _much_ faster on big lists. (Bubble sort and insertion sort do have one advantage though: if the list is already sorted, or almost sorted, they finish very quickly, because they can stop as soon as a pass makes no changes.) Merge sort's main downside is that it needs extra memory to store all the smaller lists it creates along the way.

> [!NOTE]
> You may see this written using _Big O notation_: linear search is $O(n)$, binary search is $O(\log n)$, bubble, selection and insertion sort are $O(n^2)$, and merge sort is $O(n \log n)$. Big O describes how the running time grows as $n$ gets large, ignoring constant factors. Whether you need to know this depends on your course, so check your specification.

**⭐ Task 9:** Use your `merge` function from Task 7 to write a function `merge_sort(items)`. The neatest way to do this uses _recursion_: a function that calls itself. In outline, your function should:
1. If the list has 0 or 1 items, return it (it's already sorted!).
2. Otherwise, split the list into a left half and a right half.
3. Call `merge_sort` on each half to sort them.
4. Return the result of merging the two sorted halves.

It might feel like cheating to use `merge_sort` inside `merge_sort`, but it works because each call works on a smaller list, until eventually the lists are small enough to return straight away (step 1). We'll learn more about recursion in [Lesson 16](../16-recursion-stacks-and-queues). [Solution](solutions/task9_merge_sort.py)

**⭐ Task 10:** Let's test the table above! You can time how long some code takes using the `time` module:
```python
import time

start = time.perf_counter()
# ... the code you want to time ...
end = time.perf_counter()
print(f"That took {end - start:.3f} seconds")
```

Time your bubble sort, insertion sort and merge sort functions (and Python's `sorted`) on lists of 1000, 2000 and 4000 random numbers. What happens to the time taken by each algorithm when you double the size of the list? Does this match what you'd expect from the table? Hint: make sure you give each algorithm its own copy of the list (using `.copy()`), otherwise the later algorithms will be sorting a list that's already sorted! [Solution](solutions/task10_timing.py)

---
[← Previous: Lesson 9](../09-files) | [Contents](../../README.md) | [Next: Lesson 11 →](../11-classes-and-objects)
