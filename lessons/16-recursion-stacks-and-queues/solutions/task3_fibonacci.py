num_calls = 0


def fibonacci(n):
    """Returns the nth Fibonacci number"""
    global num_calls  # lets us change the global variable `num_calls`
    num_calls = num_calls + 1

    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print([fibonacci(n) for n in range(20)])

num_calls = 0
print(f"fibonacci(25) = {fibonacci(25)}")
print(f"That took {num_calls:,} calls!")

# It takes so many calls because the same values are calculated again and
# again. fibonacci(25) calls fibonacci(24) and fibonacci(23). But
# fibonacci(24) ALSO calls fibonacci(23), so fibonacci(23) is calculated
# twice, fibonacci(22) three times, fibonacci(21) five times, and so on. The
# number of calls roughly doubles every time n goes up by 1 or 2!
