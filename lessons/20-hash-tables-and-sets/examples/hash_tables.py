def hash_string(key, size):
    """Returns an index between 0 and size - 1 for the string `key`"""
    total = 0
    for char in key:
        total = total + ord(char)
    return total % size


extensions = {"Ada": 120, "Alan": 101, "Grace": 133, "Tim": 155, "Guido": 204, "Margaret": 217}
size = 7

for name in extensions:
    print(f"{name}: index {hash_string(name, size)}")

# Separate chaining: each slot holds a list of (key, value) pairs
chained = []
for i in range(size):
    chained.append([])
for name, extension in extensions.items():
    chained[hash_string(name, size)].append((name, extension))

print("Separate chaining:")
for i, slot in enumerate(chained):
    print(f"  {i}: {slot}")

# Linear probing: if a slot is taken, try the next one along
probed = [None] * size
for name, extension in extensions.items():
    index = hash_string(name, size)
    while probed[index] is not None:
        index = (index + 1) % size  # wrap around to the start of the table
    probed[index] = (name, extension)

print("Linear probing:")
for i, slot in enumerate(probed):
    print(f"  {i}: {slot}")
