words = ["listen", "silent", "enlist", "google", "inlets", "banana", "stone", "tones", "notes", "onset", "elbow", "below"]

# Words that are anagrams of each other have the same letters, so they have
# the same key when their letters are sorted
groups = {}
for word in words:
    key = "".join(sorted(word))
    if key not in groups:
        groups[key] = []
    groups[key].append(word)

for group in groups.values():
    if len(group) > 1:
        print(", ".join(group))
