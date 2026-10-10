def insertion_sort(items):
    """Sorts `items` using insertion sort"""
    for i in range(1, len(items)):
        # Move the item at position i to the left until the item before it is
        # no bigger than it
        j = i
        while j > 0 and items[j - 1] > items[j]:
            items[j - 1], items[j] = items[j], items[j - 1]
            j = j - 1


numbers = [5, 1, 4, 2, 8]
insertion_sort(numbers)
print(numbers)

words = ["pear", "apple", "fig", "banana", "cherry"]
insertion_sort(words)
print(words)
