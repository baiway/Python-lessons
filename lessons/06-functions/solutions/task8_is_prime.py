import math

def is_prime(n):
    """Returns `True` if `n` is prime and `False` otherwise"""
    if n < 2:
        return False

    # If n = a * b, then a and b can't both be bigger than sqrt(n). So if n
    # has a divisor, it must have one that is at most sqrt(n).
    for divisor in range(2, math.isqrt(n) + 1):
        if n % divisor == 0:
            return False
    return True


# Print the first 20 primes
count = 0
number = 2
while count < 20:
    if is_prime(number):
        print(number)
        count = count + 1
    number = number + 1
