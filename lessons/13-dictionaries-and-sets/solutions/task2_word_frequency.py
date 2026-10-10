def get_count(item):
    """Returns the count from a (word, count) tuple"""
    return item[1]


# Count each word, ignoring capital letters and punctuation
counts = {}
with open("poem.txt", encoding="utf-8") as file:
    for line in file:
        for word in line.lower().split():
            word = word.strip(".,:;!?-")
            if word == "":
                continue  # e.g. the "--" before the poet's name
            counts[word] = counts.get(word, 0) + 1

# Sort the (word, count) pairs from most to least common, and print the top 5
most_common = sorted(counts.items(), key=get_count, reverse=True)
for word, count in most_common[:5]:
    print(f"{word}: {count}")
