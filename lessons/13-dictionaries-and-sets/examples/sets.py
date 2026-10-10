colours = {"red", "green", "blue"}
colours.add("red")  # already in the set, so nothing happens
print(colours)

# Creating a set from a list removes the duplicates
print(set(["a", "b", "a", "c", "b"]))

# Set operations
a = {1, 2, 3}
b = {2, 3, 4}
print(a | b)  # union
print(a & b)  # intersection
print(a - b)  # difference
print(a ^ b)  # symmetric difference
