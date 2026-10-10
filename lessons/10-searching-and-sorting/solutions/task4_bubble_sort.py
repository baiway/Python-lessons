def bubble_sort(items):
    """Sorts `items` using bubble sort, printing the list after each pass"""
    n = len(items)
    pass_number = 0
    swapped = True
    while swapped:
        swapped = False
        pass_number = pass_number + 1

        # After each pass, one more item at the end is in the right place, so
        # we don't need to check it again
        for i in range(n - pass_number):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
                swapped = True

        print(f"After pass {pass_number}: {items}")


numbers = [6, 2, 9, 4, 1]
bubble_sort(numbers)
print(f"Sorted: {numbers}")
