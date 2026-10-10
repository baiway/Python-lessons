def linear_search(items, target):
    """Returns the index of `target` in `items` (or -1 if it isn't there), and
    the number of comparisons made"""
    comparisons = 0
    for i in range(len(items)):
        comparisons = comparisons + 1
        if items[i] == target:
            return i, comparisons
    return -1, comparisons


numbers = list(range(1, 1001))
for target in [1, 500, 1000, 0]:
    index, comparisons = linear_search(numbers, target)
    print(f"Searching for {target}: index {index}, {comparisons} comparisons")
