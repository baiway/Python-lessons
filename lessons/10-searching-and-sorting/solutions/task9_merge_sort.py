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
    # A list with 0 or 1 items is already sorted
    if len(items) <= 1:
        return items

    # Split the list in half, sort each half, then merge them back together
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    return merge(left, right)


print(merge_sort([6, 2, 9, 4, 1, 8, 3, 7]))  # [1, 2, 3, 4, 6, 7, 8, 9]
print(merge_sort([5, 1, 4, 2, 8]))           # [1, 2, 4, 5, 8]
print(merge_sort([]))                        # []
