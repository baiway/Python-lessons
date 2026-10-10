def linear_search(items, target):
    """Returns the index of `target` in `items`, or -1 if it isn't there"""
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1


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


numbers = [3, 8, 15, 21, 30, 42, 57, 66, 71, 89]
print(linear_search(numbers, 42))  # 5
print(binary_search(numbers, 42))  # 5
print(linear_search(numbers, 50))  # -1
print(binary_search(numbers, 50))  # -1
