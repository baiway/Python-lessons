import random
import time

import matplotlib.pyplot as plt

def bubble_sort(items):
    """Sorts `items` using bubble sort"""
    n = len(items)
    pass_number = 0
    swapped = True
    while swapped:
        swapped = False
        pass_number = pass_number + 1
        for i in range(n - pass_number):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
                swapped = True


def merge(left, right):
    """Merges two sorted lists into one sorted list"""
    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i = i + 1
        else:
            merged.append(right[j])
            j = j + 1
    return merged + left[i:] + right[j:]


def merge_sort(items):
    """Returns a sorted copy of `items`, using merge sort"""
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    return merge(merge_sort(items[:mid]), merge_sort(items[mid:]))


def time_sort(sort_function, items):
    """Returns the time (in seconds) that `sort_function` takes to sort a copy
    of `items`"""
    items = items.copy()
    start = time.perf_counter()
    sort_function(items)
    return time.perf_counter() - start


sizes = list(range(100, 2001, 100))
bubble_times = []
merge_times = []
for n in sizes:
    numbers = [random.randint(1, 1_000_000) for _ in range(n)]
    bubble_times.append(time_sort(bubble_sort, numbers))
    merge_times.append(time_sort(merge_sort, numbers))

plt.plot(sizes, bubble_times, marker="o", label="Bubble sort")
plt.plot(sizes, merge_times, marker="o", label="Merge sort")
plt.xlabel("Number of items")
plt.ylabel("Time (seconds)")
plt.title("How long does sorting take?")
plt.legend()
plt.grid()
plt.savefig("sorting_times.png")
plt.show()

# Bubble sort's line curves upwards (doubling n roughly quadruples the time),
# whereas merge sort's line is almost straight. The `_` in the list
# comprehension above is a common name for a loop variable we don't use.
