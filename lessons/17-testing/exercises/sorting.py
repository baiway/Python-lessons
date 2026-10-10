def bubble_sort(items):
    """Sorts `items` using bubble sort"""
    n = len(items)
    pass_number = 0
    swapped = True
    while swapped:
        swapped = False
        pass_number = pass_number + 1
        for i in range(n - pass_number - 1):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
                swapped = True
