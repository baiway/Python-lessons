# Prints the mean score, the number of passes (a score of 50 or more is a
# pass) and the highest score
scores = [72, 50, 38, 91, 50, 64]

total = 0
num_passes = 0
highest = 0
for i in range(len(scores)):  # bug 1: range(1, ...) skipped the first score
    total = total + scores[i]
    if scores[i] >= 50:  # bug 2: `> 50` meant that scores of exactly 50 didn't count as passes
        num_passes = num_passes + 1
    if scores[i] > highest:
        highest = scores[i]

mean = total / len(scores)  # bug 3: `//` rounded the mean down to a whole number

print(f"Mean score: {mean:.2f}")
print(f"Number of passes: {num_passes}")
print(f"Highest score: {highest}")
