def binary_search(items, target, low, high):
    """Returns the index of `target` in the sorted list `items`, searching
    only between the indexes `low` and `high`, or -1 if it isn't there"""
    # Base case: there's nothing left to search
    if low > high:
        return -1

    mid = (low + high) // 2
    if items[mid] == target:
        return mid
    elif target < items[mid]:
        return binary_search(items, target, low, mid - 1)
    else:
        return binary_search(items, target, mid + 1, high)


numbers = [3, 8, 15, 21, 30, 42, 57, 66, 71, 89]
print(binary_search(numbers, 42, 0, len(numbers) - 1))  # 5
print(binary_search(numbers, 3, 0, len(numbers) - 1))   # 0
print(binary_search(numbers, 50, 0, len(numbers) - 1))  # -1
