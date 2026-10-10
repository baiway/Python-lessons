def linear_search(items, target):
    """Returns the index of `target` in `items` (or -1 if it isn't there), and
    the number of comparisons made"""
    comparisons = 0
    for i in range(len(items)):
        comparisons = comparisons + 1
        if items[i] == target:
            return i, comparisons
    return -1, comparisons


def binary_search(items, target):
    """Returns the index of `target` in the sorted list `items` (or -1 if it
    isn't there), and the number of comparisons made"""
    comparisons = 0
    low = 0
    high = len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        comparisons = comparisons + 1
        if items[mid] == target:
            return mid, comparisons
        elif target < items[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1, comparisons


numbers = list(range(1, 1_000_001))
for target in [1, 500_000, 999_999, 0]:
    _, linear_comparisons = linear_search(numbers, target)
    _, binary_comparisons = binary_search(numbers, target)
    print(f"Searching for {target}:")
    print(f"  Linear search: {linear_comparisons:,} comparisons")
    print(f"  Binary search: {binary_comparisons:,} comparisons")
