def is_even(n):
    """Returns `True` if `n` is even and `False` otherwise"""
    return n % 2 == 0


def max_of_three(a, b, c):
    """Returns the largest of three numbers"""
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c


def mean(numbers):
    """Returns the mean of a list of numbers"""
    return sum(numbers) / len(numbers)
