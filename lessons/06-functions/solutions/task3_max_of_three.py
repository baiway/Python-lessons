def max_of_three(a, b, c):
    """Returns the largest of three numbers"""
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c

print(max_of_three(1, 2, 3))  # 3
print(max_of_three(3, 2, 1))  # 3
print(max_of_three(2, 3, 1))  # 3
print(max_of_three(5, 5, 1))  # 5
print(max_of_three(1, 5, 5))  # 5
print(max_of_three(-4, -2, -9))  # -2
