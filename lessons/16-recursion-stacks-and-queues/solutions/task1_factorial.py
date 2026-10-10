import math


def factorial_recursive(n):
    """Calculates n! using recursion"""
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_loop(n):
    """Calculates n! using a loop"""
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result


for n in range(11):
    print(f"{n}! = {factorial_recursive(n)} = {factorial_loop(n)}")

# Python only allows about 1000 calls to be waiting at once, so this fails
try:
    factorial_recursive(5000)
except RecursionError as error:
    print(f"Error: {error}")

# The loop version has no such problem. The answer is so big that Python won't
# even print it by default, so we use logarithms to count its digits instead.
num_digits = math.floor(math.log10(factorial_loop(5000))) + 1
print(f"5000! has {num_digits:,} digits")
