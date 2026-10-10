def factorial(n):
    if n <= 1:
        return 1                    # the base case
    return n * factorial(n - 1)     # the recursive case


for n in range(1, 8):
    print(f"{n}! = {factorial(n)}")
