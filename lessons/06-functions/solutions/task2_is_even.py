def is_even(n):
    """Returns `True` if `n` is even and `False` otherwise"""
    return n % 2 == 0

for i in range(1, 21):
    if is_even(i):
        print(i)
