import random

def roll_dice(num_dice, sides=6):
    """Simulates rolling `num_dice` dice with `sides` sides and returns the total"""
    total = 0
    for i in range(num_dice):
        total = total + random.randint(1, sides)
    return total


# counts[t] is the number of times we rolled a total of t. Totals of 0 and 1
# are impossible with two dice, but including them means the index of each
# count is the same as its total, which makes life easier.
counts = []
for i in range(13):
    counts.append(0)

num_rolls = 10_000
for i in range(num_rolls):
    total = roll_dice(2)
    counts[total] = counts[total] + 1

# Print a bar chart, with one # for every 100 rolls
for total in range(2, 13):
    bar = "#" * (counts[total] // 100)
    print(f"{total:2}: {counts[total]:4} {bar}")
