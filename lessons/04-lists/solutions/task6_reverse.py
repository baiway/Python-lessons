original = [1, 2, 3, 4, 5]

# Insert each item at the front of the new list, so the last item ends up first
reversed_copy = []
for item in original:
    reversed_copy.insert(0, item)

print(original)
print(reversed_copy)
