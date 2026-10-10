num_calls = 0
memo = {0: 0, 1: 1}  # the answers we already know


def fibonacci(n):
    """Returns the nth Fibonacci number, remembering answers as it goes"""
    global num_calls
    num_calls = num_calls + 1

    if n not in memo:
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]


print(f"fibonacci(25) = {fibonacci(25)}")
print(f"That took {num_calls} calls")

# Because each answer is only calculated once, much bigger values are fine.
# (Very big values, like fibonacci(5000), still hit Python's recursion limit,
# unless you work your way up to them gradually.)
print(f"fibonacci(500) = {fibonacci(500)}")

# Python can do this for you! Put `@functools.cache` above a function (after
# `import functools`) and it will remember its answers automatically.
