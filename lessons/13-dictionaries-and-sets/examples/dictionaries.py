ages = {"Ada": 36, "Alan": 41, "Grace": 85}

# Looking up values
print(ages["Alan"])
print("Tim" in ages)
print(ages.get("Tim"))
print(ages.get("Tim", 0))

# Adding, changing and removing keys
ages["Tim"] = 71
ages["Ada"] = 37
del ages["Grace"]
print(ages)

# Looping over keys, values, and both
for name in ages:
    print(name)

for age in ages.values():
    print(age)

for name, age in ages.items():
    print(f"{name} is {age} years old")

# Counting with a dictionary
words = ["the", "cat", "sat", "on", "the", "mat", "the", "end"]

counts = {}
for word in words:
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1

print(counts)
