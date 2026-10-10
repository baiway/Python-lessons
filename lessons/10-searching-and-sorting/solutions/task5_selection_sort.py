def selection_sort(items):
    """Sorts `items` using selection sort"""
    for i in range(len(items) - 1):
        # Find the index of the smallest item from position i onwards
        smallest = i
        for j in range(i + 1, len(items)):
            if items[j] < items[smallest]:
                smallest = j

        # Swap it into position i
        items[i], items[smallest] = items[smallest], items[i]


numbers = [5, 1, 4, 2, 8]
selection_sort(numbers)
print(numbers)

words = ["pear", "apple", "fig", "banana", "cherry"]
selection_sort(words)
print(words)
