def fizzbuzz(n):
    """Returns what should be said for the number `n` in a game of FizzBuzz"""
    if n < 1:
        raise ValueError("FizzBuzz starts at 1")
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)
