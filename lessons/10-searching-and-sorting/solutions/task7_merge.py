def merge(left, right):
    """Merges two sorted lists into one sorted list"""
    merged = []
    i = 0  # index in `left`
    j = 0  # index in `right`

    # Keep taking the smaller of the two front items until one list runs out
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i = i + 1
        else:
            merged.append(right[j])
            j = j + 1

    # One of the lists might have some items left over. They're already
    # sorted, and they're all bigger than everything in `merged`, so we can
    # just add them to the end.
    merged = merged + left[i:] + right[j:]
    return merged


print(merge([2, 4, 6, 9], [1, 3, 7, 8]))  # [1, 2, 3, 4, 6, 7, 8, 9]
print(merge([1, 2, 3], [10, 20]))         # [1, 2, 3, 10, 20]
print(merge([], [5, 6]))                  # [5, 6]
