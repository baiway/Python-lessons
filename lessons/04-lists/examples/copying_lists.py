# `b = a` does NOT copy the list: `a` and `b` are two names for the same list
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # prints [1, 2, 3, 4]

# Use `.copy()` to make a separate copy
a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a)  # prints [1, 2, 3]
print(b)  # prints [1, 2, 3, 4]
