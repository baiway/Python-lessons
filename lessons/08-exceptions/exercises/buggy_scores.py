# This program is supposed to print the mean score, the number of passes (a
# score of 50 or more is a pass) and the highest score. It contains three bugs!
scores = [72, 50, 38, 91, 50, 64]

total = 0
num_passes = 0
highest = 0
for i in range(1, len(scores)):
    total = total + scores[i]
    if scores[i] > 50:
        num_passes = num_passes + 1
    if scores[i] > highest:
        highest = scores[i]

mean = total // len(scores)

print(f"Mean score: {mean}")
print(f"Number of passes: {num_passes}")
print(f"Highest score: {highest}")
