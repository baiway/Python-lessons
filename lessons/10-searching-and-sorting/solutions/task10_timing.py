import random
import time

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


def insertion_sort(items):
    """Sorts `items` using insertion sort"""
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j - 1] > items[j]:
            items[j - 1], items[j] = items[j], items[j - 1]
            j = j - 1


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
    end = time.perf_counter()
    return end - start


print(f"{'n':>6} {'Bubble':>10} {'Insertion':>10} {'Merge':>10} {'sorted':>10}")
for n in [1000, 2000, 4000]:
    numbers = []
    for i in range(n):
        numbers.append(random.randint(1, 1_000_000))

    bubble_time = time_sort(bubble_sort, numbers)
    insertion_time = time_sort(insertion_sort, numbers)
    merge_time = time_sort(merge_sort, numbers)
    builtin_time = time_sort(sorted, numbers)
    print(f"{n:>6} {bubble_time:>10.4f} {insertion_time:>10.4f} {merge_time:>10.4f} {builtin_time:>10.4f}")

# When n doubles, bubble and insertion sort take roughly 4 times as long
# (because 2^2 = 4), whereas merge sort takes only a little more than twice as
# long. `sorted` is faster than all of them, because it's written in C and uses
# a cleverer algorithm (called Timsort).
